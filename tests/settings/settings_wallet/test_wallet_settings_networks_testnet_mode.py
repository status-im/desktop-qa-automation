import allure
import pytest
from allure import step

from constants.wallet import WalletNetworkSettings, WalletNetworkNaming
from gui.components.wallet.testnet_mode_banner import TestnetModeBanner
from gui.components.wallet.wallet_toast_message import WalletToastMessage
from gui.main_window import MainWindow

pytestmark = allure.suite("Wallet")


@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/view/703505', 'Network: Testnet switching')
@pytest.mark.case(703505)
def test_switch_testnet_mode(main_screen: MainWindow):
    with step('Verify that Testnet toggle has subtitle'):
        networks = main_screen.left_panel.open_settings().left_panel.open_wallet_settings().open_networks()
        subtitle = networks.get_testnet_toggle_subtitle()
        assert subtitle == WalletNetworkSettings.TESTNET_SUBTITLE.value, \
            f"Testnet title is incorrect, current subtitle is {subtitle}"

    with step('Verify back to Wallet settings button is present and text on top is correct'):
        assert networks.is_back_to_wallet_settings_button_present(), \
            f"Back to Wallet settings button is not visible on Networks screen"

    with step('Verify that Testnet mode toggle is turned off'):
        assert not networks.is_testnet_mode_toggle_checked(), f"Testnet toggle is on when it should not"

    with step('Turn on Testnet mode'):
        networks.switch_testnet_mode_toggle().click_turn_on_testnet_mode_in_testnet_modal()

    with step('Verify that Testnet mode turned on'):
        WalletToastMessage().get_toast_message(WalletNetworkSettings.TESTNET_ENABLED_TOAST_MESSAGE.value)
        TestnetModeBanner().wait_until_appears()
        assert networks.is_testnet_mode_toggle_checked(), f"Testnet toggle if off when it should not"

    with step('Verify networks are switched to testnets'):
        assert networks.get_network_item_attribute_by_id_and_attr_name('title',
                                                                       WalletNetworkNaming.ETHEREUM_GOERLI_NETWORK_ID.value) == WalletNetworkNaming.LAYER1_ETHEREUM.value
        assert networks.get_network_item_attribute_by_id_and_attr_name('title',
                                                                       WalletNetworkNaming.OPTIMISM_GOERLI_NETWORK_ID.value) == WalletNetworkNaming.LAYER2_OPTIMISIM.value
        assert networks.get_network_item_attribute_by_id_and_attr_name('title',
                                                                       WalletNetworkNaming.ARBITRUM_GOERLI_NETWORK_ID.value) == WalletNetworkNaming.LAYER2_ARBITRUM.value
        # TODO: add verificatin for test net label

    with step('Turn off Testnet mode in wallet settings'):
        networks.switch_testnet_mode_toggle().turn_off_testnet_mode_in_testnet_modal()

    with step('Verify that Testnet mode turned off'):
        WalletToastMessage().get_toast_message(WalletNetworkSettings.TESTNET_DISABLED_TOAST_MESSAGE.value)
        TestnetModeBanner().wait_until_hidden()
        assert not networks.is_testnet_mode_toggle_checked(), f"Testnet toggle is on when it should not"


@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/view/703621',
                 'Network: Enable testnet toggle and click cross button in confirmation')
@pytest.mark.case(703621)
def test_toggle_testnet_toggle_on_and_close_the_confirmation(main_screen: MainWindow):
    networks = main_screen.left_panel.open_settings().left_panel.open_wallet_settings().open_networks()

    with step('Verify that Testnet mode toggle is turned off'):
        assert not networks.is_testnet_mode_toggle_checked(), f"Testnet toggle is enabled when it should not"

    with step('Check Mainnet network item title'):
        networks.get_network_item_attribute_by_id_and_attr_name('title',
                                                                WalletNetworkNaming.ETHEREUM_MAINNET_NETWORK_ID.value)

    with step('Toggle the Testnet mode toggle ON'):
        testnet_modal = networks.switch_testnet_mode_toggle()

    with step('Click cross button on the Testnet modal'):
        testnet_modal.close_testnet_modal_with_cross_button()
        assert not networks.is_testnet_mode_toggle_checked()

    with step('Verify that Testnet mode is not turned off'):
        assert not WalletToastMessage().is_visible
        assert not TestnetModeBanner().is_visible, f"Testnet banner is present when it should not"
        assert not networks.is_testnet_mode_toggle_checked(), \
            f"Testnet toggle is turned on when it should not"


@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/view/703622',
                 'Network:  Network: Enable Testnets, toggle testnet toggle OFF, click cancel in confirmation')
@pytest.mark.case(703621)
# @pytest.mark.skip(reason="https://github.com/status-im/status-desktop/issues/12247"), bug is now fixed
def test_switch_testnet_off_by_toggle_and_cancel_in_confirmation(main_screen: MainWindow):
    networks = main_screen.left_panel.open_settings().left_panel.open_wallet_settings().open_networks()

    with step('Verify that Testnet mode toggle is turned off'):
        assert not networks.is_testnet_mode_toggle_checked(), f"Testnet toggle is enabled when it should not"

    with step('Toggle the Testnet mode toggle ON'):
        testnet_modal = networks.switch_testnet_mode_toggle()

    with step('Confirm enabling testnet mode in testnet modal'):
        testnet_modal.click_turn_on_testnet_mode_in_testnet_modal()

    with step('Verify testnet mode is enabled'):
        WalletToastMessage().get_toast_message(WalletNetworkSettings.TESTNET_ENABLED_TOAST_MESSAGE.value)
        TestnetModeBanner().wait_until_appears()
        assert networks.is_testnet_mode_toggle_checked(), f"testnet toggle is off"

    with step('Toggle the Testnet mode toggle Off'):
        testnet_modal = networks.switch_testnet_mode_toggle()

    with step('Click Cancel button on the Testnet modal'):
        testnet_modal.click_cancel_button_in_testnet_modal()
        assert networks.is_testnet_mode_toggle_checked(), f"Testnet toggle is turned OFF when it should not"

    with step('Verify that Testnet mode is not turned off'):
        assert TestnetModeBanner().is_visible, f"Testnet banner is not present when it should"