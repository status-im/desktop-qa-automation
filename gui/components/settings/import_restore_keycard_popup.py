import time
import typing

import allure

import driver
from gui.components.base_popup import BasePopup
from gui.elements.button import Button
from gui.elements.object import QObject
from gui.elements.text_label import TextLabel


class ImportRestoreViaSeedPhrasePopup(BasePopup):

    def __init__(self):
        super().__init__()
        self._keycard_image = QObject('image_KeycardImage')
        self._keycard_popup_header = TextLabel('headerTitle')
        self._keycard_instruction_text = TextLabel('keycard_reader_instruction_text')
        self._next_button = Button('nextStatusButton')