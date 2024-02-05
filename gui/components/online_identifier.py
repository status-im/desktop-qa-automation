import time

import allure

import configs
import constants
import driver
from gui.components.profile_popup import ProfilePopup
from gui.elements.button import Button
from gui.elements.object import QObject
from gui.elements.text_label import TextLabel


class OnlineIdentifier(QObject):

    def __init__(self):
        super(OnlineIdentifier, self).__init__('onlineIdentifierProfileHeader')
        self._always_active_button = Button('userContextmenu_AlwaysActiveButton')
        self._inactive_button = Button('userContextmenu_InActiveButton')
        self._automatic_button = Button('userContextmenu_AutomaticButton')
        self._view_my_profile_button = Button('userContextMenu_ViewMyProfileAction')
        self._user_name_text_label = TextLabel('userLabel_StyledText')
        self._identicon_ring = QObject('o_StatusIdenticonRing')

    @allure.step('Wait until appears {0}')
    def wait_until_appears(self, timeout_msec: int = configs.timeouts.UI_LOAD_TIMEOUT_MSEC):
        driver.waitFor(lambda: self._view_my_profile_button.is_visible, timeout_msec)
        return self

    @property
    @allure.step('Check identicon ring visibility')
    def is_identicon_ring_visible(self):
        return self._identicon_ring.is_visible

    @property
    @allure.step('Get user name')
    def get_user_name(self) -> str:
        return self._user_name_text_label.text

    @allure.step('Set user state online')
    def set_user_state_online(self):
        self._always_active_button.click()
        self.wait_until_hidden()

    @allure.step('Set user state offline')
    def set_user_state_offline(self):
        self._inactive_button.click()
        self.wait_until_hidden()

    @allure.step('Set user automatic state')
    def set_user_automatic_state(self):
        self._automatic_button.click()
        self.wait_until_hidden()

    @allure.step('Open Profile popup from online identifier')
    def open_profile_popup_from_online_identifier(self, attempts: int = 2) -> ProfilePopup:
        self._view_my_profile_button.click()
        time.sleep(0.5)
        try:
            return ProfilePopup()
        except Exception as ex:
            if attempts:
                self.open_profile_popup_from_online_identifier(attempts - 1)
            else:
                raise ex
