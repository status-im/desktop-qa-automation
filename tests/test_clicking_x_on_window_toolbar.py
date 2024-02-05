import allure
import pytest
import psutil
from allure_commons._allure import step
from gui.main_window import MainWindow
from . import marks

pytestmark = marks


@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/view/704966', 'Clicking X on the window toolbar')
@pytest.mark.case(704966)
def test_clicking_x_on_window_toolbar(aut, main_screen: MainWindow):
    with step('Open settings and turn on minimize on close checkbox'):
        settings = main_screen.left_panel.open_settings()
        advanced_settings = settings.left_panel.open_advanced_settings()
        advanced_settings.turn_on_minimize_switch(True)

    with step('Click X button on the app window toolbar'):
        main_screen.click_close_button()

    with step('Check that the app window was minimized'):
        assert psutil.Process(aut.pid).is_running()
        assert not main_screen.is_visible

    with step('Maximize the app window'):
        main_screen.show()

    with step('Open settings and turn off minimize on close checkbox'):
        advanced_settings.turn_on_minimize_switch(False)

    with step('Click X button on the app window toolbar'):
        main_screen.click_close_button()

    with step('Check that app was closed'):
        psutil.Process(aut.pid).wait(timeout=10)
