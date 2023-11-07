import time

import configs.timeouts


def waitFor(condition, timeout_msec: int = configs.timeouts.UI_LOAD_TIMEOUT_MSEC) -> bool:
    started_at = time.monotonic()
    while not condition():
        time.sleep(1)
        if time.monotonic() - started_at > timeout_msec/1000:
            return False
    return True
