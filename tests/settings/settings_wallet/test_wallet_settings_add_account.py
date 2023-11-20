import random
import string
import time

import allure
import pytest
from allure_commons._allure import step

import constants
from gui.components.signing_phrase_popup import SigningPhrasePopup
from gui.components.wallet.authenticate_popup import AuthenticatePopup
from gui.components.wallet.wallet_toast_message import WalletToastMessage
from gui.main_window import MainWindow


@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/edit/703598',
                 'Add new account from wallet settings screen')
@pytest.mark.case(703598)
@pytest.mark.parametrize('user_account', [constants.user.user_account_one])
@pytest.mark.parametrize('account_name, color, emoji, emoji_unicode',
                         [
                             pytest.param(''.join(random.choices(string.ascii_letters +
                                                                 string.digits, k=15)), '#2a4af5', 'sunglasses', '1f60e')
                         ])
@pytest.mark.skip(reason="https://github.com/status-im/status-desktop/issues/12777")
def test_add_new_account_from_wallet_settings(
        main_screen: MainWindow, user_account, account_name: str, color: str, emoji: str, emoji_unicode: str):
    with step('Open add account pop up from wallet settings'):
        add_account_popup = \
            main_screen.left_panel.open_settings().left_panel.open_wallet_settings().open_add_account_pop_up()

    with step('Add a new generated account from wallet settings screen'):
        add_account_popup.set_name(account_name).set_emoji(emoji).set_color(color).save()
        AuthenticatePopup().wait_until_appears().authenticate(user_account.password)
        add_account_popup.wait_until_hidden()

    with step('Verify toast message notification when adding account'):
        assert len(WalletToastMessage().get_toast_messages) == 1, \
            f"Multiple toast messages appeared"
        message = WalletToastMessage().get_toast_messages[0]
        assert message == f'"{account_name}" successfully added'

    with step('Verify that the account is correctly displayed in accounts list on main wallet screen'):

        wallet = main_screen.left_panel.open_wallet()
        SigningPhrasePopup().wait_until_appears().confirm_phrase()
        expected_account = constants.user.account_list_item(account_name, color.lower(), emoji_unicode)
        started_at = time.monotonic()
        while expected_account not in wallet.left_panel.accounts:
            time.sleep(1)
        if time.monotonic() - started_at > 15:
            raise LookupError(f'Account {account_name} not found in {wallet.left_panel.accounts}')
