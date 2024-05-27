import time

import allure
import pytest
from allure_commons._allure import step

import configs
import constants
import driver
from gui.components.onboarding.before_started_popup import BeforeStartedPopUp
from gui.components.onboarding.beta_consent_popup import BetaConsentPopup
from gui.components.signing_phrase_popup import SigningPhrasePopup
from gui.components.splash_screen import SplashScreen
from gui.screens.onboarding import KeysView, WelcomeToStatusView, BiometricsView, \
    YourEmojihashAndIdenticonRingView
from gui.screens.wallet import WalletAccountView


@pytest.fixture
def keys_screen(main_window) -> KeysView:
    with step('Open Generate new keys view'):
        BeforeStartedPopUp().get_started()
        welcome_screen = WelcomeToStatusView().wait_until_appears()
        return welcome_screen.get_keys()


@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/view/736365', 'Market data and chart are not empty')
@pytest.mark.case(736365)
@pytest.mark.transaction
@pytest.mark.parametrize('user_account', [constants.user.user_with_funds])
@pytest.mark.parametrize('asset_name', [pytest.param('Ether')])
def test_wallet_check_market_data(keys_screen, main_window, user_account, asset_name: str):
    with step('Open import seed phrase view and enter seed phrase'):
        input_view = keys_screen.open_import_seed_phrase_view().open_seed_phrase_input_view()
        input_view.input_seed_phrase(user_account.seed_phrase, True)
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

    with step('Verify that restored account reveals correct status wallet address'):
        wallet_settings = main_window.left_panel.open_settings().left_panel.open_wallet_settings()
        status_acc_view = wallet_settings.open_account_in_settings('Account 1', '0')
        address = status_acc_view.get_account_address_value()
        assert address == user_account.status_address, \
            f"Recovered account should have address {user_account.status_address}, but has {address}"
        status_acc_view.click_back_button()

    with step('Set testnet mode'):
        wallet_settings.open_networks().switch_testnet_mode_toggle().turn_on_testnet_mode_in_testnet_modal()

    with step('Click asset Ether in the list of assets'):
        main_window.left_panel.open_wallet()
        SigningPhrasePopup().wait_until_appears().confirm_phrase()
        wallet_account_view = WalletAccountView()
        asset_view = wallet_account_view.click_asset(asset_name)

    time.sleep(20)

    with step('Verify that all market data fields are not empty'):
        assert driver.waitFor(lambda: asset_view.get_asset_eth_header_numbers() != 0,
                              configs.timeouts.UI_LOAD_TIMEOUT_MSEC)
        assert driver.waitFor(lambda: asset_view.get_asset_usd_header_numbers() != 0,
                              configs.timeouts.UI_LOAD_TIMEOUT_MSEC)
        assert driver.waitFor(lambda: asset_view.get_asset_market_cap_numbers() != 0,
                              configs.timeouts.UI_LOAD_TIMEOUT_MSEC)
        assert driver.waitFor(lambda: asset_view.get_asset_day_low_numbers() != 0,
                              configs.timeouts.UI_LOAD_TIMEOUT_MSEC)
        assert driver.waitFor(lambda: asset_view.get_asset_day_high_numbers() != 0,
                              configs.timeouts.UI_LOAD_TIMEOUT_MSEC)
        assert driver.waitFor(lambda: asset_view.get_asset_hour_numbers() != 0, configs.timeouts.UI_LOAD_TIMEOUT_MSEC)
        assert driver.waitFor(lambda: asset_view.get_asset_day_numbers() != 0, configs.timeouts.UI_LOAD_TIMEOUT_MSEC)
        assert driver.waitFor(lambda: asset_view.get_asset_24_hours_numbers() != 0,
                              configs.timeouts.UI_LOAD_TIMEOUT_MSEC)
