import logging
import time

import allure
import squish

import configs
from driver.server import SquishServer

LOG = logging.getLogger(__name__)


@allure.step('Get application context of "{0}"')
def get_context(aut_id: str, timeout, retries: int = 0):
    LOG.debug('Getting context: %s', aut_id)
    for i in range(retries + 1):
        try:
            context = squish.attachToApplication(aut_id, SquishServer().host, SquishServer().port, timeout)
            if context is not None:
                LOG.info('AUT %s context found', aut_id)
                return context
        except RuntimeError:
            time.sleep(timeout)
            continue
        except Exception as ex:
            raise ex


@allure.step('Detaching')
def detach():
    for ctx in squish.applicationContextList():
        ctx.detach()
        assert squish.waitFor(lambda: not ctx.isRunning, configs.timeouts.APP_LOAD_TIMEOUT_MSEC)
    LOG.info('All AUTs detached')
