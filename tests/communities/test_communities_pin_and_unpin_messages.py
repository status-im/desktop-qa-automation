import time
from copy import deepcopy
from datetime import datetime

import allure
import pytest
from allure_commons._allure import step

import driver
from gui.main_window import MainWindow
from . import marks

import configs
import constants
from constants import ColorCodes, UserAccount
from gui.screens.community_settings import CommunitySettingsScreen
from gui.screens.messages import MessagesScreen

pytestmark = marks


@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/view/703255',
                 'Edit chat - Add pinned message (when any member can pin is disabled)')
@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/view/703256',
                 'Edit chat - Remove pinned message (when any member can pin is disabled)')
@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/view/703510', 'Join community via owner invite')
@pytest.mark.case(703255, 703256, 703510)
@pytest.mark.parametrize('user_data_one, user_data_two', [
    (configs.testpath.TEST_USER_DATA / 'community_user_1', configs.testpath.TEST_USER_DATA / 'community_user_2')
])
@pytest.mark.skip(reason='https://github.com/status-im/desktop-qa-automation/issues/618')
def test_join_community_and_pin_unpin_message(multiple_instances, user_data_one, user_data_two):
    user_one: UserAccount = constants.community_user_1
    user_two: UserAccount = constants.community_user_2
    community_params = deepcopy(constants.community_params)
    community_params['name'] = f'{datetime.now():%d%m%Y_%H%M%S}'
    main_screen = MainWindow()

    with multiple_instances(user_data=user_data_one) as aut_one, multiple_instances(user_data=user_data_two) as aut_two:
        with step(f'Launch multiple instances with authorized users {user_one.name} and {user_two.name}'):
            for aut, account in zip([aut_one, aut_two], [user_one, user_two]):
                aut.attach()
                main_screen.wait_until_appears(configs.timeouts.APP_LOAD_TIMEOUT_MSEC).prepare()
                main_screen.authorize_user(account)
                main_screen.hide()

        with step(f'User {user_two.name}, create community and invite {user_one.name}'):
            aut_two.attach()
            main_screen.prepare()
            main_screen.create_community(community_params['name'], community_params['description'],
                                         community_params['intro'], community_params['outro'],
                                         community_params['logo']['fp'], community_params['banner']['fp'])
            main_screen.left_panel.invite_people_in_community([user_one.name], 'Message', community_params['name'])
            main_screen.hide()

        with step(f'User {user_one.name}, accept invitation from {user_two.name}'):
            aut_one.attach()
            main_screen.prepare()
            messages_view = main_screen.left_panel.open_messages_screen()
            chat = messages_view.left_panel.click_chat_by_name(user_two.name)
            community_screen = chat.accept_community_invite(community_params['name'], '0')

        with step(f'User {user_one.name}, verify welcome community popup'):
            welcome_popup = community_screen.left_panel.open_welcome_community_popup()
            assert community_params['name'] in welcome_popup.title
            assert community_params['intro'] == welcome_popup.intro
            welcome_popup.join().authenticate(user_one.password)
            assert driver.waitFor(lambda: not community_screen.left_panel.is_join_community_visible,
                                  configs.timeouts.UI_LOAD_TIMEOUT_MSEC), 'Join community button not hidden'

        with step(f'User {user_one.name}, see two members in community members list'):
            assert driver.waitFor(lambda: user_two.name in community_screen.right_panel.members)
            assert driver.waitFor(lambda: '2' in community_screen.left_panel.members)
            main_screen.hide()

        with step(f'User {user_two.name}, see two members in community members list'):
            aut_two.attach()
            main_screen.prepare()
            assert driver.waitFor(lambda: user_one.name in community_screen.right_panel.members)
            assert '2' in community_screen.left_panel.members

        with step(f'Go to edit community for {user_two.name} and check that pin message checkbox is not checked'):
            community_screen = main_screen.left_panel.select_community(community_params['name'])
            community_setting = community_screen.left_panel.open_community_settings()
            edit_community_form = community_setting.left_panel.open_overview().open_edit_community_view()
            assert not edit_community_form.pin_message_checkbox_state

        with step('Go back to community and send a couple of message in general channel'):
            CommunitySettingsScreen().left_panel.back_to_community()
            messages_screen = MessagesScreen()
            message_text = "Hi"
            messages_screen.group_chat.send_message_to_group_chat(message_text)
            second_message_text = "Hi again"
            messages_screen.group_chat.send_message_to_group_chat(second_message_text)
            newest_message_object = messages_screen.chat.messages('0')
            message_items = [message.text for message in newest_message_object]
            for message_item in message_items:
                assert second_message_text in message_item, f'Message {message_text} is not visible'

        with step(f'Hover message {second_message_text} and pin it'):
            message = messages_screen.chat.find_message_by_text(second_message_text, '0')
            message.hover_message().toggle_pin()
            main_screen.hide()

        with step(f'User {user_one.name} see the {second_message_text} as pinned'):
            aut_one.attach()
            main_screen.prepare()
            message = messages_screen.chat.find_message_by_text(second_message_text, '1')
            assert message.message_is_pinned
            assert message.pinned_info_text + message.user_name_in_pinned_message == 'Pinned by' + user_two.name
            assert message.get_message_color() == ColorCodes.ORANGE.value
            main_screen.hide()

        with step(f'User {user_two.name} hover message and unpin it'):
            aut_two.attach()
            main_screen.prepare()
            message = messages_screen.chat.find_message_by_text(second_message_text, '0')
            message.hover_message().toggle_pin()

        with step(f'User {user_one.name} see the {second_message_text} as unpinned'):
            aut_one.attach()
            main_screen.prepare()
            time.sleep(2)
            message = messages_screen.chat.find_message_by_text(second_message_text, '1')
            assert driver.waitFor(lambda: message.message_is_pinned) is False
            assert message.user_name_in_pinned_message == ''
            assert driver.waitFor(lambda: messages_screen.tool_bar.is_pin_message_tooltip_visible) is False
