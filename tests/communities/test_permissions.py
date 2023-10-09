import allure
import pytest
from allure_commons._allure import step

import constants
import driver
from gui.main_window import MainWindow

pytestmark = allure.suite("Communities")


@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/view/703632', 'Manage community: Adding new permissions')
@pytest.mark.case(703632)
@pytest.mark.parametrize('params', [constants.community_params])
@pytest.mark.parametrize(
    'checkbox_state, first_asset, second_asset, amount, allowed_to, in_general, asset_title, second_asset_title, allowed_to_title',
    [
        pytest.param('On', 'Dai Stablecoin', 'No', '10', 'becomeMember', 'No', '10 DAI', 'No', 'Become member'),
        pytest.param('On', 'Ether', 'No', '1', 'becomeAdmin', 'No', '1 ETH', 'No', 'Become an admin'),
        pytest.param('On', 'Ether', 'Dai Stablecoin', '10', 'viewAndPost', '#general', '10 ETH', '10 DAI',
                     'View and post'),
        pytest.param('On', 'Ether', 'Dai Stablecoin', '10', 'viewOnly', '#general', '10 ETH', '10 DAI', 'View only'),
        pytest.param('Off', 'No', 'No', 'No', 'becomeAdmin', 'No', 'No', 'No', 'Become an admin')
    ])
def test_adding_permissions(main_screen: MainWindow, params, checkbox_state, first_asset, second_asset, amount,
                            allowed_to, in_general, asset_title, second_asset_title, allowed_to_title):
    main_screen.create_community(params)

    with step('Open add new permission page'):
        community_screen = main_screen.left_panel.select_community(params['name'])
        community_setting = community_screen.left_panel.open_community_settings()
        permissions_settings = community_setting.left_panel.open_permissions().add_new_permission()

    with step('Create new permission'):
        permissions_settings.set_who_holds_checkbox_state(checkbox_state)
        permissions_settings.set_who_holds_asset_and_amount(first_asset, amount)
        permissions_settings.set_who_holds_asset_and_amount(second_asset, amount)
        permissions_settings.set_is_allowed_to(allowed_to)
        permissions_settings.set_in(in_general)
        permissions_settings.create_permission()

    with step('Created permission is displayed on permission page'):
        if asset_title != 'No':
            assert driver.waitFor(lambda: asset_title in permissions_settings.tags)
        if second_asset_title != 'No':
            assert driver.waitFor(lambda: second_asset_title in permissions_settings.tags)
        if allowed_to_title != 'No':
            assert driver.waitFor(lambda: allowed_to_title in permissions_settings.tags)
