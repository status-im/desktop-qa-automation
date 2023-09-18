import time
import typing

import allure

import configs.timeouts
import driver
from constants import UserCommunityInfo, wallet_account_list_item
from driver import objects_access
from driver.objects_access import walk_children
from gui.components.change_password_popup import ChangePasswordPopup
from gui.components.settings.send_contact_request_popup import SendContactRequest
from gui.components.wallet.testnet_mode_popup import TestnetModePopup
from gui.elements.qt.button import Button
from gui.elements.qt.list import List
from gui.elements.qt.object import QObject
from gui.elements.qt.scroll import Scroll
from gui.elements.qt.text_edit import TextEdit
from gui.elements.qt.text_label import TextLabel
from gui.screens.community_settings import CommunitySettingsScreen
from gui.screens.messages import MessagesScreen
from scripts.tools.image import Image


class LeftPanel(QObject):

    def __init__(self):
        super().__init__('mainWindow_LeftTabView')
        self._settings_section_template = QObject('scrollView_MenuItem_StatusNavigationListItem')

    def _open_settings(self, index: int, section_name: str):
        self._settings_section_template.real_name['objectName'] = f'{index}-{section_name}MenuItem'
        self._settings_section_template.click()

    @allure.step('Open messaging settings')
    def open_messaging_settings(self) -> 'MessagingSettingsView':
        self._open_settings(3, 'App')
        return MessagingSettingsView()

    @allure.step('Open communities settings')
    def open_communities_settings(self) -> 'CommunitiesSettingsView':
        self._open_settings(12, 'App')
        return CommunitiesSettingsView()

    @allure.step('Open wallet settings')
    def open_wallet_settings(self):
        self._open_settings(4, 'App')
        return WalletSettingsView()

    @allure.step('Open profile settings')
    def open_profile_settings(self):
        self._open_settings(0, 'Main')
        return ProfileSettingsView()


class SettingsScreen(QObject):

    def __init__(self):
        super().__init__('mainWindow_ProfileLayout')
        self.left_panel = LeftPanel()


class ProfileSettingsView(QObject):

    def __init__(self):
        super().__init__('mainWindow_MyProfileView')
        self._scroll_view = Scroll('settingsContentBaseScrollView_Flickable')
        self._display_name_text_field = TextEdit('displayName_TextEdit')
        self._save_button = Button('settingsSave_StatusButton')
        self._change_password_button = Button('change_password_button')

    @property
    @allure.step('Get display name')
    def display_name(self) -> str:
        self._scroll_view.vertical_scroll_to(self._display_name_text_field)
        return self._display_name_text_field.text

    @allure.step('Set user name')
    def set_name(self, value: str):
        self._scroll_view.vertical_scroll_to(self._display_name_text_field)
        self._display_name_text_field.text = value
        self.save_changes()

    @allure.step('Save changes')
    def save_changes(self):
        self._save_button.click()

    @allure.step('Open change password form')
    def open_change_password_popup(self):
        self._change_password_button.click()
        return ChangePasswordPopup().wait_until_appears()


class MessagingSettingsView(QObject):

    def __init__(self):
        super().__init__('mainWindow_MessagingView')
        self._contacts_button = Button('contactsListItem_btn_StatusContactRequestsIndicatorListItem')

    @allure.step('Open contacts settings')
    def open_contacts_settings(self) -> 'ContactsSettingsView':
        self._contacts_button.click()
        return ContactsSettingsView().wait_until_appears()


class PendingRequest:

    def __init__(self, obj):
        self.object = obj
        self.icon: typing.Optional[Image] = None
        self.contact: typing.Optional[Image] = None
        self._accept_button: typing.Optional[Button] = None
        self._reject_button: typing.Optional[Button] = None
        self._open_canvas_button: typing.Optional[Button] = None
        self.init_ui()

    def __repr__(self):
        return self.contact

    def init_ui(self):
        for child in walk_children(self.object):
            if str(getattr(child, 'id', '')) == 'iconOrImage':
                self.icon = Image(driver.objectMap.realName(child))
            elif str(getattr(child, 'id', '')) == 'menuButton':
                self._open_canvas_button = Button(name='', real_name=driver.objectMap.realName(child))
            elif str(getattr(child, 'objectName', '')) == 'checkmark-circle-icon':
                self._accept_button = Button(name='', real_name=driver.objectMap.realName(child))
            elif str(getattr(child, 'objectName', '')) == 'close-circle-icon':
                self._reject_button = Button(name='', real_name=driver.objectMap.realName(child))
            elif str(getattr(child, 'id', '')) == 'statusListItemTitle':
                self.contact = str(child.text)

    def accept(self) -> MessagesScreen:
        assert self._accept_button is not None, 'Button not found'
        self._accept_button.click()
        return MessagesScreen().wait_until_appears()


class ContactsSettingsView(QObject):

    def __init__(self):
        super().__init__('mainWindow_ContactsView')
        self._contact_request_button = Button('mainWindow_Send_contact_request_to_chat_key_StatusButton')
        self._pending_request_tab = Button('contactsTabBar_Pending_Requests_StatusTabButton')
        self._pending_requests_list = List('settingsContentBaseScrollView_ContactListPanel')

    @property
    @allure.step('Get all pending requests')
    def pending_requests(self) -> typing.List[PendingRequest]:
        self._pending_request_tab.click()
        return [PendingRequest(item) for item in self._pending_requests_list.items]

    @allure.step('Open contacts request form')
    def open_contact_request_form(self) -> SendContactRequest:
        self._contact_request_button.click()
        return SendContactRequest().wait_until_appears()

    @allure.step('Accept contact request')
    def accept_contact_request(
            self, contact: str, timeout_sec: int = configs.timeouts.MESSAGING_TIMEOUT_SEC) -> MessagesScreen:
        self._pending_request_tab.click()
        started_at = time.monotonic()
        request = None
        while request is None:
            requests = self.pending_requests
            for _request in requests:
                if _request.contact == contact:
                    request = _request
            assert time.monotonic() - started_at < timeout_sec, f'Contact: {contact} not found in {requests}'
        return request.accept()


class CommunitiesSettingsView(QObject):

    def __init__(self):
        super().__init__('mainWindow_CommunitiesView')
        self._community_item = QObject('settingsContentBaseScrollView_listItem_StatusListItem')
        self._community_template_image = QObject('settings_iconOrImage_StatusSmartIdenticon')
        self._community_template_name = TextLabel('settings_Name_StatusTextWithLoadingState')
        self._community_template_description = TextLabel('settings_statusListItemSubTitle')
        self._community_template_members = TextLabel('settings_member_StatusTextWithLoadingState')
        self._community_template_button = Button('settings_StatusFlatButton')

    @property
    @allure.step('Get communities')
    def communities(self) -> typing.List[UserCommunityInfo]:
        _communities = []
        for obj in driver.findAllObjects(self._community_item.real_name):
            container = driver.objectMap.realName(obj)
            self._community_template_image.real_name['container'] = container
            self._community_template_name.real_name['container'] = container
            self._community_template_description.real_name['container'] = container
            self._community_template_members.real_name['container'] = container

            _communities.append(UserCommunityInfo(
                self._community_template_name.text,
                self._community_template_description.text,
                self._community_template_members.text,
                self._community_template_image.image
            ))
        return _communities

    def _get_community_item(self, name: str):
        for obj in driver.findAllObjects(self._community_item.real_name):
            for item in objects_access.walk_children(obj):
                if getattr(item, 'text', '') == name:
                    return obj
        raise LookupError(f'Community item: {name} not found')

    @allure.step('Open community info')
    def get_community_info(self, name: str) -> UserCommunityInfo:
        for community in self.communities:
            if community.name == name:
                return community
        raise LookupError(f'Community item: {name} not found')

    @allure.step('Open community overview settings')
    def open_community_overview_settings(self, name: str):
        driver.mouseClick(self._get_community_item(name))
        return CommunitySettingsScreen().wait_until_appears()


class KeycardSettingsView(QObject):

    def __init__(self):
        super(KeycardSettingsView, self).__init__('mainWindow_KeycardView')
        self._scroll = Scroll('settingsContentBaseScrollView_Flickable')
        self._setup_keycard_with_existing_account_button = Button('setupFromExistingKeycardAccount_StatusListItem')
        self._create_new_keycard_account_button = Button('createNewKeycardAccount_StatusListItem')
        self._import_restore_via_seed_phrase_button = Button('importRestoreKeycard_StatusListItem')
        self._import_from_keycard_button = Button('importFromKeycard_StatusListItem')
        self._check_whats_on_keycard_button = Button('checkWhatsNewKeycard_StatusListItem')
        self._factory_reset_keycard_button = Button('factoryResetKeycard_StatusListItem')

    @allure.step('Check that keycard screen displayed')
    def check_keycard_screen_loaded(self):
        assert KeycardSettingsView().is_visible

    @allure.step('Check that all keycard options displayed')
    def all_keycard_options_available(self):
        assert self._setup_keycard_with_existing_account_button.is_visible, f'Setup keycard with existing account not visible'
        assert self._create_new_keycard_account_button.is_visible, f'Create new keycard button not visible'
        assert self._import_restore_via_seed_phrase_button.is_visible, f'Import and restore via seed phrase button not visible'
        self._scroll.vertical_scroll_to(self._import_from_keycard_button)
        assert driver.waitFor(lambda: self._import_from_keycard_button.is_visible,
                              configs.timeouts.UI_LOAD_TIMEOUT_MSEC), f'Import keycard button not visible'
        assert driver.waitFor(lambda: self._check_whats_on_keycard_button.is_visible,
                              configs.timeouts.UI_LOAD_TIMEOUT_MSEC ), f'Check whats new keycard button not visible'
        assert driver.waitFor(lambda: self._factory_reset_keycard_button.is_visible,
                              configs.timeouts.UI_LOAD_TIMEOUT_MSEC ), f'Factory reset keycard button not visible'


class WalletSettingsView(QObject):

    def __init__(self):
        super().__init__('mainWindow_WalletView')
        self._wallet_network_button = Button('settings_Wallet_MainView_Networks')
        self._account_order_button = Button('settingsContentBaseScrollView_accountOrderItem_StatusListItem')

    @allure.step('Open networks in wallet settings')
    def open_networks(self):
        self._wallet_network_button.click()
        return NetworkWalletSettings().wait_until_appears()

    @allure.step('Open account order in wallet settings')
    def open_account_order(self):
        self._account_order_button.click()
        return EditAccountOrderSettings().wait_until_appears()


class NetworkWalletSettings(WalletSettingsView):

    def __init__(self):
        super(NetworkWalletSettings, self).__init__()
        self._wallet_networks_item = QObject('settingsContentBaseScrollView_WalletNetworkDelegate')
        self._testnet_text_item = QObject('settingsContentBaseScrollView_Goerli_testnet_active_StatusBaseText')
        self._testnet_mode_button = Button('settings_Wallet_NetworksView_TestNet_Toggle')

    @property
    @allure.step('Get wallet networks items')
    def networks_names(self) -> typing.List[str]:
        return [str(network.title) for network in driver.findAllObjects(self._wallet_networks_item.real_name)]

    @property
    @allure.step('Get amount of testnet active items')
    def testnet_items_amount(self) -> int:
        items_amount = 0
        for item in driver.findAllObjects(self._testnet_text_item.real_name):
            if item.text == 'Goerli testnet active':
                items_amount += 1
        return items_amount

    @allure.step('Switch testnet mode')
    def switch_testnet_mode(self):
        self._testnet_mode_button.click()
        return TestnetModePopup().wait_until_appears()

    @allure.step('Check state of testnet mode switch')
    def get_testnet_mode_button_checked_state(self):
        return self._testnet_mode_button.is_checked


class EditAccountOrderSettings(WalletSettingsView):

    def __init__(self):
        super(EditAccountOrderSettings, self).__init__()
        self._account_item = QObject('settingsContentBaseScrollView_draggableDelegate_StatusDraggableListItem')
        self._accounts_list = QObject('statusDesktop_mainWindow')

    @property
    @allure.step('Get accounts')
    def accounts(self) -> typing.List[wallet_account_list_item]:
        _accounts = []
        for account_item in driver.findAllObjects(self._account_item.real_name):
            element = QObject(name='', real_name=driver.objectMap.realName(account_item))
            name = str(account_item.title)
            icon = None
            for child in objects_access.walk_children(account_item):
                if getattr(child, 'objectName', '') == 'identicon':
                    icon = Image(driver.objectMap.realName(child))
                    break
            _accounts.append(wallet_account_list_item(name, icon, element))

        return sorted(_accounts, key=lambda account: account.object.y)

    @allure.step('Get account in accounts list')
    def _get_account_item(self, name: str):
        for obj in driver.findAllObjects(self._account_item.real_name):
            if getattr(obj, 'title', '') == name:
                return obj
        raise LookupError(f'Account item: {name} not found')

    @allure.step('Get eye icon on watch-only account')
    def get_eye_icon(self, name: str):
        for child in objects_access.walk_children(self._get_account_item(name)):
            if getattr(child, 'objectName', '') == 'show-icon':
                return child
        raise LookupError(f'Eye icon not found on {name} account item')

    @allure.step('Drag account to change the order')
    def drag_account(self, name: str, index: int):
        assert driver.waitFor(lambda: len([account for account in self.accounts if account.name == name]) == 1), \
            'Account not found or found more then one'
        bounds = [account for account in self.accounts if account.name == name][0].object.bounds
        d_bounds = self.accounts[index].object.bounds
        driver.mouse.press_and_move(self._accounts_list.object, bounds.x, bounds.y, d_bounds.x, d_bounds.y)
