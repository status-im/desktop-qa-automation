import time
import typing
from typing import List

import allure

import configs
import driver
from driver.objects_access import walk_children
from gui.components.context_menu import ContextMenu
from gui.components.messaging.edit_group_name_and_image_popup import EditGroupNameAndImagePopup
from gui.components.messaging.leave_group_popup import LeaveGroupPopup
from gui.elements.button import Button
from gui.elements.list import List
from gui.elements.object import QObject
from gui.elements.scroll import Scroll
from gui.elements.text_edit import TextEdit
from gui.elements.text_label import TextLabel
from gui.screens.community import CommunityScreen
from scripts.tools.image import Image


class LeftPanel(QObject):

    def __init__(self):
        super().__init__('mainWindow_contactColumnLoader_Loader')
        self._start_chat_button = Button('mainWindow_startChatButton_StatusIconTabButton')
        self._search_text_edit = TextEdit('mainWindow_search_edit_TextEdit')
        self._scroll = Scroll('scrollView_Flickable')
        self._contacts_list = List('chatList_ListView')
        self._contact_item = QObject('scrollView_StatusChatListItem')

    @property
    @allure.step('Get contacts')
    def contacts(self) -> typing.List[str]:
        return self._contacts_list.get_values('objectName')

    @allure.step('Open chat')
    def open_chat(self, contact: str):
        assert driver.waitFor(lambda: contact in self.contacts), f'Contact: {contact} not found in {self.contacts}'
        self._contacts_list.select(contact, 'objectName')
        return ChatView()

    @allure.step('Click start chat button')
    def start_chat(self):
        self._start_chat_button.click(x=1, y=1)
        return CreateChatView()

    @allure.step('Open context menu group chat')
    def _open_context_menu_for_chat(self, chat_name: str) -> ContextMenu:
        self._contact_item.real_name['objectName'] = chat_name
        self._contact_item.open_context_menu()
        return ContextMenu().wait_until_appears()

    @allure.step('Open leave popup')
    def open_leave_group_popup(self, chat_name: str, attempt: int = 2) -> LeaveGroupPopup:
        try:
            self._open_context_menu_for_chat(chat_name).select('Leave group')
            return LeaveGroupPopup().wait_until_appears()
        except Exception as ex:
            if attempt:
                return self.open_leave_group_popup(chat_name, attempt - 1)
            else:
                raise ex


class ToolBar(QObject):

    def __init__(self):
        super().__init__('mainWindow_statusToolBar_StatusToolBar')


class Message:

    def __init__(self, obj):
        self.object = obj
        self.date: typing.Optional[str] = None
        self.time: typing.Optional[str] = None
        self.icon: typing.Optional[Image] = None
        self.from_user: typing.Optional[str] = None
        self.text: typing.Optional[str] = None
        self.banner_image: typing.Optional[Button] = None
        self.community_invitation: dict = {}
        self.init_ui()

    def init_ui(self):
        for child in walk_children(self.object):
            if getattr(child, 'objectName', '') == 'StatusDateGroupLabel':
                self.date = str(child.text)
            elif getattr(child, 'id', '') == 'title':
                self.community_invitation['name'] = str(child.text)
            elif getattr(child, 'id', '') == 'description':
                self.community_invitation['description'] = str(child.text)
            else:
                match getattr(child, 'id', ''):
                    case 'profileImage':
                        self.icon = Image(driver.objectMap.realName(child))
                    case 'primaryDisplayName':
                        self.from_user = str(child.text)
                    case 'timestampText':
                        self.time = str(child.text)
                    case 'chatText':
                        self.text = str(child.text)
                    case 'bannerImage':
                        self.banner_image = Button(name='', real_name=driver.objectMap.realName(child))

    @allure.step('Open community invitation')
    def open_community_invitation(self):
        self.banner_image.click()
        return CommunityScreen().wait_until_appears()


class ChatView(QObject):

    def __init__(self):
        super().__init__('mainWindow_ChatColumnView')
        self._message_list_item = QObject('chatLogView_chatMessageViewDelegate_MessageView')

    @property
    @allure.step('Get messages')
    def messages(self) -> typing.List[Message]:
        _messages = []
        for item in driver.findAllObjects(self._message_list_item.real_name):
            if getattr(item, 'isMessage', False):
                _messages.append(Message(item))
        return _messages

    @allure.step('Accept community invitation')
    def accept_community_invite(self, community: str) -> 'CommunityScreen':
        message = None
        started_at = time.monotonic()
        while message is None:
            for _message in self.messages:
                if _message.community_invitation.get('name', '') == community:
                    message = _message
                    break
            if time.monotonic() - started_at > configs.timeouts.MESSAGING_TIMEOUT_SEC:
                raise LookupError(f'Invitation not found')

        return message.open_community_invitation()


class CreateChatView(QObject):

    def __init__(self):
        super().__init__('mainWindow_CreateChatView')
        self._confirm_button = Button('createChatView_confirmBtn')
        self._cancel_button = Button('mainWindow_Cancel_StatusButton')
        self._create_chat_contacts_list = List('createChatView_contactsList')

    @property
    @allure.step('Get contacts')
    def contacts(self) -> typing.List[str]:
        return self._create_chat_contacts_list.get_values('title')

    @allure.step('Select contact in the list')
    def select_contact(self, contact: str):
        assert driver.waitFor(lambda: contact in self.contacts), f'Contact: {contact} not found in {self.contacts}'
        self._create_chat_contacts_list.select(contact, 'title')

    @allure.step('Create chat by adding contacts from contact list')
    def create_chat(self, members):
        for member in members[0:]:
            time.sleep(0.2)
            self.select_contact(member)
        self._confirm_button.click()
        return ChatMessagesView().wait_until_appears()


class ChatMessagesView(QObject):

    def __init__(self):
        super().__init__('mainWindow_ChatMessagesView')
        self._group_chat_message_item = TextLabel('chatLogView_Item')
        self._group_name_label = TextLabel('statusChatInfoButton')
        self._more_button = Button('moreOptionsButton_StatusFlatRoundButton')
        self._edit_menu_item = QObject('edit_name_and_image_StatusMenuItem')
        self._leave_group_item = QObject('leave_group_StatusMenuItem')
        self._message_field = TextEdit('inputScrollView_Message_PlaceholderText')

    @property
    @allure.step('Get group name')
    def group_name(self) -> str:
        return self._group_name_label.text

    @property
    @allure.step('Get group welcome message')
    def group_welcome_message(self) -> str:
        for delegate in walk_children(self._group_chat_message_item.object):
            if getattr(delegate, 'id', '') == 'msgDelegate':
                for item in walk_children(delegate):
                    if getattr(item, 'id', '') == 'descText':
                        return str(item.text)

    @allure.step('Click more options button')
    def open_more_options(self):
        self._more_button.click()

    @allure.step('Choose edit group name option')
    def open_edit_group_name_form(self):
        time.sleep(2)
        self.open_more_options()
        time.sleep(2)
        self._edit_menu_item.click()
        return EditGroupNameAndImagePopup().wait_until_appears()

    @allure.step('Choose leave group option')
    def leave_group(self):
        time.sleep(2)
        self.open_more_options()
        time.sleep(2)
        self._leave_group_item.click()
        return LeaveGroupPopup().wait_until_appears()

    @allure.step('Send message to group chat')
    def send_message_to_group_chat(self, message: str):
        self._message_field.type_text(message)
        driver.nativeType('<Return>')


class Members(QObject):

    def __init__(self):
        super().__init__('mainWindow_userListPanel_StatusListView')
        self._member_item = QObject('groupUserListPanel_StatusMemberListItem')

    @property
    @allure.step('Get group members')
    def members(self) -> typing.List[str]:
        return [str(member.title) for member in driver.findAllObjects(self._member_item.real_name)]


class MessagesScreen(QObject):

    def __init__(self):
        super().__init__('mainWindow_chatView_ChatView')
        self.left_panel = LeftPanel()
        self.tool_bar = ToolBar()
        self.chat = ChatView()
        self.right_panel = Members()
        self.group_chat = ChatMessagesView()
