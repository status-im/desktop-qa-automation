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

    @allure.step('Select emoji')
    def select(self, name: str, attempts: int = 2):
        self._search_text_edit.text = name
        self._emoji_item.real_name['objectName'] = 'statusEmoji_' + name
        try:
            self._emoji_item.click()
        except LookupError as err:
            if attempts:
                return self.select(name, attempts - 1)
            else:
                raise err
        EmojiPopup().wait_until_hidden()
