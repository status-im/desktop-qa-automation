import allure

from gui.components.base_popup import BasePopup
from gui.elements.button import Button
from gui.elements.check_box import CheckBox
from gui.elements.object import QObject


class BeforeStartedPopUp(BasePopup):

    def __init__(self):
        super(BeforeStartedPopUp, self).__init__()
        self._acknowledge_checkbox = CheckBox('acknowledge_checkbox')
        self._terms_of_use_checkBox = CheckBox('termsOfUseCheckBox_StatusCheckBox')
        self._get_started_button = Button('getStartedStatusButton_StatusButton')
        self._terms_of_use_link = QObject('termsOfUseLink_StatusBaseText')
        self._privacy_policy_link = QObject('privacyPolicyLink_StatusBaseText')

    @property
    @allure.step('Get visible attribute')
    def is_visible(self) -> bool:
        return self._get_started_button.is_visible

    @allure.step('Allow all and get started')
    def get_started(self):
        self._acknowledge_checkbox.set(True)
        self._terms_of_use_checkBox.set(True, x=10)
        assert self._terms_of_use_link.is_visible, f"Terms of use link is missing"
        assert self._privacy_policy_link.is_visible, f"Privacy Policy link is missing"
        self._get_started_button.click()
        self.wait_until_hidden()
