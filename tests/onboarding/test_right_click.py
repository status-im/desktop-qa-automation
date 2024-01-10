import allure
import psutil
import pytest
from allure_commons._allure import step

import driver
from gui.elements.native_mac import NativeMac
from gui.main_window import MainWindow
from tests.onboarding import marks

pytestmark = marks


@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/view/704621','Quitting Status by click')
@pytest.mark.case(704621)
def test_quit_by_click(aut, main_screen: MainWindow):
    with step('Open Status menu and select Quit Status option'):
        native = NativeMac()
        app = NativeMac().get_app(aut.pid)
        native.get_menu_item_by_name(app, 'Status').Press()
        driver.nativeType('<Command+q>')

    with step('Check that app was closed'):
        psutil.Process(aut.pid).wait(timeout=10)

    with step('Check that crash report did not appear after quiting'):
        for text in native.get_text(app):
            assert 'quit unexpectedly' in text
