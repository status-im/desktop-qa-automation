import allure
import pytest
from allure_commons._allure import step

import constants
import driver
from constants.permissions import PermissionsElements
from gui.main_window import MainWindow
from scripts.tools import image



@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/view/703198',
                 'Manage community: Manage Permissions screen overview')
@pytest.mark.case(703198)
@pytest.mark.parametrize('params', [constants.community_params])
@pytest.mark.skip(reason='https://github.com/status-im/desktop-qa-automation/issues/186')
def test_permissions_screen_overview(main_screen: MainWindow, params):
    main_screen.create_community(params)

    with step('Open permissions in community settings'):
        community_screen = main_screen.left_panel.select_community(params['name'])
        community_setting = community_screen.left_panel.open_community_settings()
        permissions_settings = community_setting.left_panel.open_permissions()

    with step('Verify all elements on permissions screen'):
        with step('Permission welcome image is correct'):
            welcome_image = permissions_settings.permission_welcome_image
            image.compare(welcome_image, 'permission_welcome_image.png')
        with step('Permission welcome title is correct'):
            assert permissions_settings.permission_welcome_title == PermissionsElements.WELCOME_TITLE.value
        with step('Permission welcome subtitle is correct'):
            assert permissions_settings.permission_welcome_subtitle == PermissionsElements.WELCOME_SUBTITLE.value
        with step('Permission welcome checklist is correct'):
            assert PermissionsElements.WELCOME_CHECKLIST_ELEMENT_1.value == permissions_settings.permission_checklist[0]
            assert PermissionsElements.WELCOME_CHECKLIST_ELEMENT_2.value == permissions_settings.permission_checklist[1]
            assert PermissionsElements.WELCOME_CHECKLIST_ELEMENT_3.value == permissions_settings.permission_checklist[2]


@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/view/703632',
                 'Manage community: Adding new permissions')
@pytest.mark.case(703632)
@pytest.mark.parametrize('params', [constants.community_params])
@pytest.mark.parametrize(
    'checkbox_state, first_asset, second_asset, amount, allowed_to, in_general, asset_title, second_asset_title, allowed_to_title',
    [
        pytest.param(True, 'Dai Stablecoin', False, '10', 'becomeMember', False, '10 DAI', False, 'Become member'),
        pytest.param(True, 'Ether', False, '1', 'becomeAdmin', False, '1 ETH', False, 'Become an admin'),
        pytest.param(True, 'Ether', 'Dai Stablecoin', '10', 'viewAndPost', '#general', '10 ETH', '10 DAI',
                     'View and post'),
        pytest.param(True, 'Ether', 'Dai Stablecoin', '10', 'viewOnly', '#general', '10 ETH', '10 DAI', 'View only'),
        pytest.param(False, False, False, False, 'becomeAdmin', False, False, False, 'Become an admin')
    ])
@pytest.mark.skip(reason="https://github.com/status-im/desktop-qa-automation/issues/167")
def test_adding_permissions(main_screen: MainWindow, params, checkbox_state: bool, first_asset, second_asset, amount,
                            allowed_to: str, in_general, asset_title, second_asset_title, allowed_to_title: str):
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
        if asset_title is not False:
            assert driver.waitFor(lambda: asset_title in permissions_settings.tags)
        if second_asset_title is not False:
            assert driver.waitFor(lambda: second_asset_title in permissions_settings.tags)
        if allowed_to_title is not False:
            assert driver.waitFor(lambda: allowed_to_title in permissions_settings.tags)
