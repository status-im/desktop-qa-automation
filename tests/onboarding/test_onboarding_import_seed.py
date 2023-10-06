import allure
import pytest
from allure_commons._allure import step

import configs.system
import constants
from driver.aut import AUT
from gui.components.onboarding.before_started_popup import BeforeStartedPopUp
from gui.components.onboarding.beta_consent_popup import BetaConsentPopup
from gui.components.splash_screen import SplashScreen
from gui.screens.onboarding import BiometricsView, AllowNotificationsView, WelcomeToStatusView, KeysView


@pytest.fixture
def keys_screen(main_window) -> KeysView:
    with step('Open Generate new keys view'):
        if configs.system.IS_MAC:
            AllowNotificationsView().wait_until_appears().allow()
        BeforeStartedPopUp().get_started()
        wellcome_screen = WelcomeToStatusView().wait_until_appears()
        return wellcome_screen.get_keys()


@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/view/703040', 'Import: 12 word seed phrase')
@pytest.mark.case(703040)
@pytest.mark.parametrize('user_account', [constants.user.user_account_two])
def test_import_seed_phrase(aut: AUT, keys_screen, main_window, user_account):
    with step('Open import seed phrase view and enter seed phrase'):
        input_view = keys_screen.open_import_seed_phrase_view().open_seed_phrase_input_view()
        profile_view = input_view.input_seed_phrase(user_account.seed_phrase)
        profile_view.set_display_name(user_account.name)

    with step('Finalize onboarding and open main screen'):
        details_view = profile_view.next()
        create_password_view = details_view.next()
        confirm_password_view = create_password_view.create_password(user_account.password)
        confirm_password_view.confirm_password(user_account.password)
        if configs.system.IS_MAC:
            BiometricsView().wait_until_appears().prefer_password()
        SplashScreen().wait_until_appears().wait_until_hidden()
        if not configs.DEV_BUILD:
            BetaConsentPopup().confirm()

    with step('Verify that the user logged in via seed phrase correctly'):
        user_canvas = main_window.left_panel.open_user_canvas()
        profile_popup = user_canvas.open_profile_popup()
        assert profile_popup.user_name == user_account.name

    aut.restart()
    main_window.authorize_user(user_account)