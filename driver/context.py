import logging
import time

import allure
import squish

import configs
from driver.server import SquishServer

LOG = logging.getLogger(__name__)


@allure.step('Attaching to "{0}"')
def attach(aut_id: str, attempts: int = 3):
    LOG.debug('Attaching to: %s', aut_id)
    for i in range (attempts + 1):
        try:
            context = squish.attachToApplication(aut_id, SquishServer().host, SquishServer().port)
            LOG.info('AUT %s attached', aut_id)
            return context
        except RuntimeError:
            time.sleep(4)
            continue
        except Exception as ex:
            raise ex


@allure.step('Detaching')
def detach():
    for ctx in squish.applicationContextList():
        ctx.detach()
        assert squish.waitFor(lambda: not ctx.isRunning, configs.timeouts.APP_LOAD_TIMEOUT_MSEC)
    LOG.info('All AUTs detached')
