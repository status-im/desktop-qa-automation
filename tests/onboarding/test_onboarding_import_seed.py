import allure
import pytest
from allure_commons._allure import step

from gui.mocked_keycard_controller import MockedKeycardController
from . import marks

import configs.system
import constants
from gui.components.onboarding.before_started_popup import BeforeStartedPopUp
from gui.components.onboarding.beta_consent_popup import BetaConsentPopup
from gui.components.splash_screen import SplashScreen
from gui.main_window import LeftPanel
from gui.screens.onboarding import BiometricsView, WelcomeToStatusView, KeysView, \
    YourEmojihashAndIdenticonRingView

pytestmark = marks


@pytest.fixture
def keys_screen(main_window) -> KeysView:
    with step('Open Generate new keys view'):
        BeforeStartedPopUp().get_started()
        welcome_screen = WelcomeToStatusView().wait_until_appears()
        return welcome_screen.get_keys()


@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/view/703040', 'Import: 12 word seed phrase')
@pytest.mark.case(703040)
@pytest.mark.parametrize('user_account', [constants.user.user_account_one])
@pytest.mark.parametrize('autocomplete, default_name', [
    pytest.param(False, 'Account 1'),
    pytest.param(True, 'Account 1', marks=pytest.mark.critical)
])
def test_import_seed_phrase(keys_screen, main_window, user_account, default_name: str, autocomplete: bool):
    with step('Open import seed phrase view and enter seed phrase'):
        input_view = keys_screen.open_import_seed_phrase_view().open_seed_phrase_input_view()
        input_view.input_seed_phrase(user_account.seed_phrase, autocomplete)
        profile_view = input_view.import_seed_phrase()
        profile_view.set_display_name(user_account.name)

    with step('Finalize onboarding and open main screen'):
        create_password_view = profile_view.next()
        confirm_password_view = create_password_view.create_password(user_account.password)
        confirm_password_view.confirm_password(user_account.password)
        if configs.system.IS_MAC:
            BiometricsView().wait_until_appears().prefer_password()
        SplashScreen().wait_until_appears().wait_until_hidden()
        next_view = YourEmojihashAndIdenticonRingView().verify_emojihash_view_present().next()
        if configs.system.IS_MAC:
            next_view.start_using_status()
        SplashScreen().wait_until_appears().wait_until_hidden()
        if not configs.system.TEST_MODE:
            BetaConsentPopup().confirm()
        mocked_keycard = MockedKeycardController()
        if configs.system.TEST_MODE and configs.system.CLOSE_KEYCARD_CONTROLLER:
            if mocked_keycard.is_visible:
                mocked_keycard.hide()

    with (step('Verify that restored account reveals correct status wallet address')):
        status_account_index = 0
        status_acc_view = (
            LeftPanel().open_settings().left_panel.open_wallet_settings().open_account_in_settings(default_name,
                                                                                                   status_account_index))
        address = status_acc_view.get_account_address_value()
        assert address == user_account.status_address, \
            f"Recovered account should have address {user_account.status_address}, but has {address}"

    with step('Verify that the user logged in via seed phrase correctly'):
        user_canvas = main_window.left_panel.open_online_identifier()
        profile_popup = user_canvas.open_profile_popup_from_online_identifier()
        assert profile_popup.user_name == user_account.name
