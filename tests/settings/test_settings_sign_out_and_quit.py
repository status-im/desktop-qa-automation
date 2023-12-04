import allure
import pytest
import psutil
from allure_commons._allure import step
from gui.main_window import MainWindow


@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/view/703010', 'Settings - Sign out & Quit')
@pytest.mark.case(703010)
def test_sign_out_and_quit(aut, main_screen: MainWindow):
    with step('Open settings'):
        settings = main_screen.left_panel.open_settings()

    with step('Click sign out and quit in settings'):
        sign_out_screen = settings.left_panel.open_sign_out_and_quit()
        sign_out_screen.sign_out_and_quit()

    with step('Check that app was closed'):
        psutil.Process(aut.pid).wait(timeout=5)
        assert aut.pid not in psutil.pids(), f"{aut.pid} is still running"
