from gui.elements.check_box import CheckBox
from gui.screens.settings import *


class AdvancedSettingsView(QObject):

    def __init__(self):
        super().__init__('mainWindow_AdvancedView')
        self._minimize_on_close_switch = CheckBox('settingsContentBaseScrollView_switchItem_StatusSwitch')

    @allure.step('Switch minimize on close checkbox')
    def turn_on_minimize_switch(self, state):
        self._minimize_on_close_switch.set(state)
