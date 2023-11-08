import random
import string

import allure
import pytest

from constants.wallet import WalletNetworkSettings, DerivationPath, WalletAccountSettings
from gui.main_window import MainWindow


@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/view/703508',
                 'Watched addresses: Excl. / Include in total balance functionality for watched address')
@pytest.mark.case(703508)
@pytest.mark.parametrize('new_name', [
    pytest.param(''.join(random.choices(string.ascii_letters +
                                        string.digits, k=40)))
])
def test_settings_include_in_total_balance(main_screen: MainWindow):

