import allure
import pytest
from allure_commons._allure import step

import configs
import constants
from constants.wallet import ARBITRUM_ADDRESS
from gui.components.signing_phrase_popup import SigningPhrasePopup
from gui.components.wallet.authenticate_popup import AuthenticatePopup
from gui.main_window import MainWindow


@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/view/704527', 'Wallet.Send.')
@pytest.mark.case(704527)
@pytest.mark.parametrize('user_data', [configs.testpath.TEST_USER_DATA / 'squisher'])
def test_wallet_main_screen_send_0_eth(main_screen: MainWindow):
    with step('Set testnet mode'):
        wallet_settings = main_screen.left_panel.open_settings().left_panel.open_wallet_settings()
        wallet_settings.open_networks().set_testnet_mode(True)
    with step('Send token'):
        wallet = main_screen.left_panel.open_wallet()
        SigningPhrasePopup().wait_until_appears().confirm_phrase()
        wallet_account = wallet.left_panel.select_account('Status account')
        wallet_account.open_send_popup().send(ARBITRUM_ADDRESS, 0, 'Ether')
        AuthenticatePopup().wait_until_appears().authenticate(constants.user_account_one.password)
    with step('Verify transaction pending'):
        assert 'Transaction pending' in main_screen.wait_for_notification()
