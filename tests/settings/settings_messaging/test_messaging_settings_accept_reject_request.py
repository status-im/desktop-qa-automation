import allure
import pytest
from allure_commons._allure import step

import configs.testpath
import constants
from constants import UserAccount
from constants.messaging import Messaging
from gui.components.toast_message import ToastMessage
from gui.main_window import MainWindow


@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/view/703011', 'Add a contact with a chat key')
@pytest.mark.case(703011)
@pytest.mark.parametrize('user_data_one, user_data_two', [
    (configs.testpath.TEST_USER_DATA / 'user_account_one', configs.testpath.TEST_USER_DATA / 'user_account_two')
])
def test_messaging_settings_accepting_request(multiple_instance, user_data_one, user_data_two):
    user_one: UserAccount = constants.user_account_one
    user_two: UserAccount = constants.user_account_two
    main_window = MainWindow()

    with multiple_instance() as aut_one, multiple_instance() as aut_two:
        with step(f'Launch multiple instances with authorized users {user_one.name} and {user_two.name}'):
            for aut, account in zip([aut_one, aut_two], [user_one, user_two]):
                aut.attach()
                main_window.wait_until_appears(configs.timeouts.APP_LOAD_TIMEOUT_MSEC).prepare()
                main_window.authorize_user(account)
                main_window.hide()

        with step(f'User {user_two.name}, get chat key'):
            aut_two.attach()
            main_window.prepare()
            profile_popup = main_window.left_panel.open_user_canvas().open_profile_popup()
            chat_key = profile_popup.chat_key
            profile_popup.close()
            main_window.hide()

        with step(f'User {user_one.name}, send contact request to {user_two.name}'):
            aut_one.attach()
            main_window.prepare()
            settings = main_window.left_panel.open_settings()
            messaging_settings = settings.left_panel.open_messaging_settings()
            contacts_settings = messaging_settings.open_contacts_settings()
            contact_request_popup = contacts_settings.open_contact_request_form()
            contact_request_popup.send(chat_key, f'Hello {user_two.name}')

        with step('Verify that contact request was sent and is in pending requests'):
            contacts_settings.open_pending_requests()
            assert Messaging.CONTACT_REQUEST_SENT.value == contacts_settings.contact_items[0].object.contactText
            assert len(contacts_settings.contact_items) == 1
            assert contacts_settings.pending_request_sent_list_title == 'Sent'
            main_window.hide()

        with step(f'Verify that contact request was received by {user_two.name}'):
            aut_two.attach()
            main_window.prepare()
            settings = main_window.left_panel.open_settings()
            messaging_settings = settings.left_panel.open_messaging_settings()
            contacts_settings = messaging_settings.open_contacts_settings()
            contacts_settings.open_pending_requests()
            assert contacts_settings.pending_request_received_list_title == 'Received'
            assert user_one.name == contacts_settings.contact_items[0].contact
            assert len(contacts_settings.contact_items) == 1

        with step('Verify toast message about new contact request received'):
            assert len(ToastMessage().get_toast_messages) == 1, \
                f"Multiple toast messages appeared"
            message = ToastMessage().get_toast_messages[0]
            assert message == Messaging.NEW_CONTACT_REQUEST.value, \
                f"Toast message is incorrect, current message is {message}"

        with step(f'User {user_two.name}, accept contact request from {user_one.name}'):
            contacts_settings.accept_contact_request(user_one.name)

        with step(f'Verify that contact appeared in contacts list of {user_two.name} in messaging settings'):
            contacts_settings = main_window.left_panel.open_settings().left_panel.open_messaging_settings().open_contacts_settings()
            contacts_settings.open_contacts()
            assert contacts_settings.contacts_list_title == 'Contacts'
            assert user_one.name == contacts_settings.contact_items[0].contact
            assert len(contacts_settings.contact_items) == 1
            main_window.hide()

        with step(f'Verify that contact appeared in contacts list of {user_one.name} in messaging settings'):
            aut_one.attach()
            main_window.prepare()
            contacts_settings = main_window.left_panel.open_settings().left_panel.open_messaging_settings().open_contacts_settings()
            contacts_settings.open_contacts()
            assert contacts_settings.contacts_list_title == 'Contacts'
            assert user_two.name == contacts_settings.contact_items[0].contact
            assert len(contacts_settings.contact_items) == 1


@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/view/704610', 'Reject a contact request with a chat key')
@pytest.mark.case(704610)
@pytest.mark.parametrize('user_data_one, user_data_two', [
    (configs.testpath.TEST_USER_DATA / 'user_account_one', configs.testpath.TEST_USER_DATA / 'user_account_two')
])
def test_messaging_settings_rejecting_request(multiple_instance, user_data_one, user_data_two):
    user_one: UserAccount = constants.user_account_one
    user_two: UserAccount = constants.user_account_two
    main_window = MainWindow()

    with multiple_instance() as aut_one, multiple_instance() as aut_two:
        with step(f'Launch multiple instances with authorized users {user_one.name} and {user_two.name}'):
            for aut, account in zip([aut_one, aut_two], [user_one, user_two]):
                aut.attach()
                main_window.wait_until_appears(configs.timeouts.APP_LOAD_TIMEOUT_MSEC).prepare()
                main_window.authorize_user(account)
                main_window.hide()

        with step(f'User {user_two.name}, get chat key'):
            aut_two.attach()
            main_window.prepare()
            profile_popup = main_window.left_panel.open_user_canvas().open_profile_popup()
            chat_key = profile_popup.chat_key
            profile_popup.close()
            main_window.hide()

        with step(f'User {user_one.name}, send contact request to {user_two.name}'):
            aut_one.attach()
            main_window.prepare()
            settings = main_window.left_panel.open_settings()
            messaging_settings = settings.left_panel.open_messaging_settings()
            contacts_settings = messaging_settings.open_contacts_settings()
            contact_request_popup = contacts_settings.open_contact_request_form()
            contact_request_popup.send(chat_key, f'Hello {user_two.name}')

            main_window.hide()

        with step(f'Verify that contact request from user {user_two.name} was received and reject contact request'):
            aut_two.attach()
            main_window.prepare()
            settings = main_window.left_panel.open_settings()
            messaging_settings = settings.left_panel.open_messaging_settings()
            contacts_settings = messaging_settings.open_contacts_settings()
            contacts_settings.open_pending_requests()
            contacts_settings.reject_contact_request(user_one.name)

        with step(f'Verify that contacts list of {user_two.name} is empty in messaging settings'):
            contacts_settings = main_window.left_panel.open_settings().left_panel.open_messaging_settings().open_contacts_settings()
            contacts_settings.open_contacts()
            assert contacts_settings.no_friends_item_text == Messaging.NO_FRIENDS_ITEM.value
            assert contacts_settings.is_invite_friends_button_visible
            main_window.hide()

        with step(f'Verify that contacts list of {user_one.name} is empty in messaging settings'):
            aut_one.attach()
            main_window.prepare()
            contacts_settings = main_window.left_panel.open_settings().left_panel.open_messaging_settings().open_contacts_settings()
            contacts_settings.open_contacts()
            assert contacts_settings.no_friends_item_text == Messaging.NO_FRIENDS_ITEM.value
            assert contacts_settings.is_invite_friends_button_visible