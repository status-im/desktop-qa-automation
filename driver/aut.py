import logging
from datetime import datetime

import allure
import cv2
import numpy as np
import squish
from PIL import ImageGrab

import configs
import driver
from configs.system import IS_LIN
from driver import context
from driver.server import SquishServer
from gui.objects_map import statusDesktop_mainWindow
from scripts.utils import system_path, local_system
from scripts.utils.system_path import SystemPath

_logger = logging.getLogger(__name__)


class AUT:
    def __init__(
            self,
            app_path: system_path.SystemPath = configs.APP_DIR,
            user_data: SystemPath = None
    ):
        super(AUT, self).__init__()
        self.path = app_path
        self.ctx = None
        self.pid = None
        self.port = None
        self.aut_id = f'AUT_{datetime.now():%H%M%S}'
        self.app_data = configs.testpath.STATUS_DATA / f'app_{datetime.now():%H%M%S_%f}'
        if user_data is not None:
            user_data.copy_to(self.app_data / 'data')
        self.options = ''
        driver.testSettings.setWrappersForApplication(self.aut_id, ['Qt'])

    def __str__(self):
        return type(self).__qualname__

    def __enter__(self):
        return self.launch()

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            try:
                self.attach()
                driver.waitForObjectExists(statusDesktop_mainWindow).setVisible(True)
                configs.testpath.TEST.mkdir(parents=True, exist_ok=True)
                screenshot = configs.testpath.TEST / f'{self.aut_id}.png'

                rect = driver.object.globalBounds(driver.waitForObject(statusDesktop_mainWindow))
                img = ImageGrab.grab(
                    bbox=(rect.x, rect.y, rect.x + rect.width, rect.y + rect.height),
                    xdisplay=configs.system.DISPLAY if IS_LIN else None)
                view = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
                cv2.imwrite(str(screenshot), view)

                allure.attach(
                    name=f'Screenshot on fail: {self.aut_id}',
                    body=screenshot.read_bytes(),
                    attachment_type=allure.attachment_type.PNG)
            except Exception as err:
                _logger.info(err)

        self.stop()

    @allure.step('Attach Squish to Test Application')
    def attach(self, timeout_sec: int = configs.timeouts.PROCESS_TIMEOUT_SEC):
        if self.ctx is None:
            self.ctx = context.attach(self.aut_id, timeout_sec)
        squish.setApplicationContext(self.ctx)

    @allure.step('Close application')
    def stop(self):
        if self.ctx is not None:
            squish.currentApplicationContext().detach()
            self.ctx = None

        if self.port is not None:
            pid_list = local_system.find_process_by_port(self.port)
            if pid_list:
                for pid in pid_list:
                    local_system.kill_process(pid, verify=True)
            assert driver.waitFor(
                lambda: not local_system.find_process_by_port(self.port), configs.timeouts.PROCESS_TIMEOUT_SEC), \
                f'Port {self.port} still in use by process: {local_system.find_process_by_port(self.port)}'
            self.port = None
            if self.pid in pid_list:
                self.pid = None

        if self.pid is not None:
            local_system.kill_process(self.pid, verify=True)
            self.pid = None

    @allure.step("Start application")
    def launch(self, options='', attempt: int = 2) -> 'AUT':
        self.options = options

        self.port = local_system.find_free_port(configs.squish.AUT_PORT, 1000)
        if configs.ATTACH_MODE:
            SquishServer().add_attachable_aut(self.aut_id, self.port)
            command = [
                configs.testpath.SQUISH_DIR / 'bin' / 'startaut',
                f'--port={self.port}',
                f'"{self.path}"',
                f'-d={self.app_data}',
                f'--LOG_LEVEL={configs.testpath.LOG_LEVEL}',
                options
            ]
            self.pid = local_system.execute(command)
        else:
            SquishServer().add_executable_aut(self.aut_id, self.path.parent)
            command = [self.aut_id, f'-d={self.app_data}']
            self.ctx = squish.startApplication(' '.join(command), configs.timeouts.PROCESS_TIMEOUT_SEC)
            self.pid = self.ctx.pid
        try:
            self.attach()
            assert squish.waitFor(lambda: self.ctx.isRunning, configs.timeouts.PROCESS_TIMEOUT_SEC) is True, \
                f'{self} is not running'
            return self
        except Exception as err:
            _logger.debug(err)
            self.stop()
            if attempt:
                return self.launch(options, attempt - 1)
            else:
                raise err

    @allure.step('Restart application')
    def restart(self):
        self.stop()
        self.launch()
