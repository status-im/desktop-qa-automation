import time

import allure

from gui.elements.button import Button
from gui.elements.object import QObject
from gui.elements.window import Window


class MockedKeycardController(Window):

    def __init__(self):
        super(MockedKeycardController, self).__init__('QQuickApplicationWindow')
        self._plugin_reader_button = Button('plugin_Reader_StatusButton')
        self._unplug_reader_button = Button('unplug_Reader_StatusButton')
        self._insert_keycard_1_button = Button('insert_Keycard_1_StatusButton')
        self._insert_keycard_2_button = Button('insert_Keycard_2_StatusButton')
        self._remove_keycard_button = Button('remove_Keycard_StatusButton')
        self._reader_unplugged_button = Button('set_initial_reader_state_StatusButton')
        self._empty_keycard_button = Button('set_initial_keycard_state_StatusButton')
        self._register_keycard_button = Button('register_Keycard_StatusButton')
        self._reader_unplugged_item = QObject('reader_Unplugged_StatusMenuItem')
        self._keycard_not_inserted_item = QObject('keycard_Not_Inserted_StatusMenuItem')
        self._keycard_inserted_item = QObject('keycard_Inserted_StatusMenuItem')

    @allure.step('Click Plug in reader')
    def plugin_reader(self):
        time.sleep(1)
        self._plugin_reader_button.click()
        time.sleep(2)
        return self

    @allure.step('Click Register keycard')
    def register_keycard(self):
        time.sleep(1)
        self._register_keycard_button.click()
        time.sleep(1)
        return self

    @allure.step('Click Insert Keycard 1')
    def insert_keycard_1(self):
        self._insert_keycard_1_button.click()
        time.sleep(1)
        return self
