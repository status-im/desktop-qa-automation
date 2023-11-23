import allure

from constants.syncing import SyncingSettings
from gui.components.community.authenticate_popup import AuthenticatePopup
from gui.components.settings.sync_new_device_popup import SyncNewDevicePopup
from gui.elements.button import Button
from gui.elements.object import QObject
from gui.elements.text_label import TextLabel


class SyncingSettingsView(QObject):

    def __init__(self):
        super().__init__('mainWindow_SyncingView')
        self._setup_syncing_button = Button('settings_Setup_Syncing_StatusButton')
        self._backup_data_button = Button('settings_Backup_Data_StatusButton')
        self._sync_new_device_instructions_header = TextLabel('settings_Sync_New_Device_Header')
        self._sync_new_device_instructions_subtitle = TextLabel('settings_Sync_New_Device_SubTitle')

    @allure.step('Checking instructions elements: back up button presence')
    def is_backup_button_present(self):
        assert self._backup_data_button.is_visible, f"Backup button is not visible"

    @allure.step('Checking instructions elements: header presence')
    def is_instructions_header_present(self):
        assert (self._sync_new_device_instructions_header.text
                == SyncingSettings.SYNC_A_NEW_DEVICE_INSTRUCTIONS_HEADER.value), f"Sync a new device title is incorrect"

    @allure.step('Checking instructions elements: subtitle presence')
    def is_instructions_subtitle_present(self):
        assert (self._sync_new_device_instructions_subtitle.text
                == SyncingSettings.SYNC_A_NEW_DEVICE_INSTRUCTIONS_SUBTITLE.value), f"Sync a new device subtitle is incorrect"

    @allure.step('Setup syncing')
    def set_up_syncing(self, password: str):
        self._setup_syncing_button.click()
        AuthenticatePopup().authenticate(password)
        return SyncNewDevicePopup()
