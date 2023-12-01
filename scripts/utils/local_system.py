import logging
import os
import signal
import subprocess
import time
import typing

import allure
import psutil

import configs
from configs.system import IS_WIN

_logger = logging.getLogger(__name__)


def find_process_by_port(port: int) -> typing.List[int]:
    pid_list = []
    for proc in psutil.process_iter():
        try:
            for conns in proc.connections(kind='inet'):
                if conns.laddr.port == port:
                    pid_list.append(proc.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return pid_list


def find_free_port(start: int, step: int):
    while find_process_by_port(start):
        start+=step
    return start

def wait_for_close(pid: int, timeout_sec: int = configs.timeouts.PROCESS_TIMEOUT_SEC):
    started_at = time.monotonic()
    while psutil.pid_exists(pid):
        time.sleep(1)
        if time.monotonic() - started_at > timeout_sec:
            raise RuntimeError(f'Process with PID: {pid} not closed')
    return True

@allure.step('Kill process')
def kill_process(pid, sig: signal.Signals = signal.SIGKILL):
    try:
        os.kill(pid, sig)
    except ProcessLookupError as err:
        _logger.error('Failed to find process %d: %s', pid, err)
        raise err

@allure.step('Kill process with retries')
def kill_process_with_retries(pid, sig: signal.Signals = signal.SIGTERM, attempts: int = 3):
    try:
        p = psutil.Process(pid)
    except psutil.NoSuchProcess:
        return

    p.terminate()

    while attempts > 0:
        attempts -= 1
        try:
            p.wait()
        except TimeoutError as err:
            p.kill()
        else:
            return

    raise RuntimeError('Failed to kill proicess: %d' % pid)

@allure.step('System execute command')
def execute(
        command: list,
        stderr=subprocess.STDOUT,
        stdout=subprocess.STDOUT,
        shell=False,
):
    _logger.info(f'Execute: %s', command)
    process = subprocess.Popen(command, shell=shell, stderr=stderr, stdout=stdout)
    return process.pid

def execute_with_log_files(
        command: list,
        stderr_log=configs.AUT_LOGS_STDERR,
        stdout_log=configs.AUT_LOGS_STDOUT,
        shell=False,
):
    with (
        open(stderr_log, "ab") as out_file,
        open(stdout_log, "ab") as err_file,
    ):
        return execute(command, shell=shell, stderr=err_file, stdout=out_file)

@allure.step('System run command')
def run(
        command: list,
        stderr=subprocess.STDOUT,
        stdout=subprocess.STDOUT,
        shell=False,
        timeout_sec=configs.timeouts.PROCESS_TIMEOUT_SEC
):
    _logger.info(f'Execute: %s', command)
    process = subprocess.run(
        command,
        shell=shell,
        stderr=stderr,
        stdout=stdout,
        timeout=timeout_sec,
        check=True
    )
