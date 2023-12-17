import allure
import pytest
from allure_commons._allure import step
from . import marks

import constants
from driver.aut import AUT
from gui.main_window import MainWindow

pytestmark = marks


@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/view/703005',
                 'Change the password and login with new password')
@pytest.mark.case(703005)
@pytest.mark.parametrize('user_account, user_account_changed_password',
                         [pytest.param(constants.user.user_account_one,
                                       constants.user.user_account_one_changed_password)])
def test_change_password_and_login(aut: AUT, main_window: MainWindow,
                                   user_account, user_account_changed_password):
    with step('Open profile settings and change password'):
        main_window.create_new_user_password_auth()
        main_window.left_panel.open_settings().left_panel.open_profile_settings().open_change_password_popup().change_password(
            user_account.password, user_account_changed_password.password)

    with step('Restart application'):
        aut.restart()
        main_window.log_in_returning_user_password_auth(user_account_changed_password)

    with step('Verify that the user logged in correctly'):
        user_canvas = main_window.left_panel.open_online_identifier()
        profile_popup = user_canvas.open_profile_popup_from_online_identifier()
        assert profile_popup.user_name == user_account.name
