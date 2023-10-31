import allure

from gui.components.back_up_your_seed_phrase_popup import BackUpYourSeedPhrasePopUp
from gui.elements.object import QObject
from gui.screens.settings_communities import CommunitiesSettingsView
from gui.screens.settings_keycard import KeycardSettingsView
from gui.screens.settings_messaging import MessagingSettingsView
from gui.screens.settings_profile import ProfileSettingsView
from gui.screens.settings_syncing import SyncingSettingsView
from gui.screens.settings_wallet import WalletSettingsView


class LeftPanel(QObject):

    def __init__(self):
        super().__init__('mainWindow_LeftTabView')
        self._settings_section_template = QObject('scrollView_MenuItem_StatusNavigationListItem')

    def _open_settings(self, object_name: str):
        self._settings_section_template.real_name['objectName'] = object_name
        self._settings_section_template.click()

    @allure.step('Check back up seed option menu item presence')
    def check_back_up_seed_option_present(self):
        self._settings_section_template.real_name['objectName'] = '17-MainMenuItem'
        return self._settings_section_template.is_visible

    @allure.step('Open messaging settings')
    def open_messaging_settings(self) -> 'MessagingSettingsView':
        self._open_settings('3-AppMenuItem')
        return MessagingSettingsView()

    @allure.step('Open communities settings')
    def open_communities_settings(self) -> 'CommunitiesSettingsView':
        self._open_settings('12-AppMenuItem')
        return CommunitiesSettingsView()

    @allure.step('Open wallet settings')
    def open_wallet_settings(self):
        self._open_settings('4-AppMenuItem')
        return WalletSettingsView()

    @allure.step('Open profile settings')
    def open_profile_settings(self):
        self._open_settings('0-MainMenuItem')
        return ProfileSettingsView()

    @allure.step('Choose back up seed phrase in settings')
    def open_back_up_seed_phrase(self):
        self._open_settings('17-MainMenuItem')
        return BackUpYourSeedPhrasePopUp()

    @allure.step('Open syncing settings')
    def open_syncing_settings(self):
        self._open_settings('8-MainMenuItem')
        return SyncingSettingsView()

    @allure.step('Open keycard settings')
    def open_keycard_settings(self):
        self._open_settings('13-MainMenuItem')
        return KeycardSettingsView()


class SettingsScreen(QObject):

    def __init__(self):
        super().__init__('mainWindow_ProfileLayout')
        self.left_panel = LeftPanel()
