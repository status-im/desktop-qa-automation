import allure

import configs
from gui.elements.object import QObject
from gui.elements.text_edit import TextEdit
from .base_popup import BasePopup


class EmojiPopup(QObject):
    def __init__(self):
        super(EmojiPopup, self).__init__('mainWallet_AddEditAccountPopup_AccountEmojiSearchBox')
        self._search_text_edit = TextEdit('mainWallet_AddEditAccountPopup_AccountEmojiSearchBox')
        self._emoji_item = QObject('mainWallet_AddEditAccountPopup_AccountEmoji')

    @allure.step('Wait until appears {0}')
    def wait_until_appears(self, timeout_msec: int = configs.timeouts.UI_LOAD_TIMEOUT_MSEC):
        self._search_text_edit.wait_until_appears(timeout_msec)
        return self

    @allure.step('Select emoji')
    def select(self, name: str, attempts: int = 2):
        self._search_text_edit.text = name
        self._emoji_item.real_name['objectName'] = 'statusEmoji_' + name
        try:
            self._emoji_item.click()
        except AssertionError as err:
            if attempts:
                return self.select(name, attempts - 1)
            else:
                raise err
        EmojiPopup().wait_until_hidden()
