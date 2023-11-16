import time
import typing

import allure

import configs
import driver
from gui.elements.button import Button
from gui.elements.object import QObject
from gui.elements.scroll import Scroll
from gui.elements.window import Window


class MockedKeycardController(Window):

    def __init__(self):
        super(MockedKeycardController, self).__init__('QQuickApplicationWindow')
        self._plugin_reader_button = Button('plugin_Reader_StatusButton')
        self._unplug_reader_button = Button('unplug_Reader_StatusButton')
        self._insert_keycard_1_button = Button('insert_Keycard_1_StatusButton')
        self._insert_keycard_2_button = Button('insert_Keycard_2_StatusButton')
        self._remove_keycard_button = Button('remove_Keycard_StatusButton')
        self._reader_state_button = Button('set_initial_reader_state_StatusButton')
        self._keycard_state_button = Button('set_initial_keycard_state_StatusButton')
        self._register_keycard_button = Button('register_Keycard_StatusButton')
        self._reader_unplugged_item = QObject('reader_Unplugged_StatusMenuItem')
        self._keycard_not_inserted_item = QObject('keycard_Not_Inserted_StatusMenuItem')
        self._keycard_inserted_item = QObject('keycard_Inserted_StatusMenuItem')
        self._custom_keycard_item = QObject('custom_Keycard_StatusMenuItem')
        self._not_status_keycard_item = QObject('not_Status_Keycard_StatusMenuItem')
        self._empty_keycard_item = QObject('empty_Keycard_StatusMenuItem')
        self._max_slots_reached_item = QObject('max_Pairing_Slots_Reached_StatusMenuItem')
        self._mnemonic_metadata_item = QObject('keycard_With_Mnemonic_Metadata_StatusMenuItem')
        self._field_object = QObject('keycard_edit_TextEdit')
        self._scroll = Scroll('keycardFlickable')

    def wait_until_appears(self, timeout_msec: int = configs.timeouts.UI_LOAD_TIMEOUT_MSEC):
        self._plugin_reader_button.wait_until_appears()
        return self

    @property
    @allure.step('Get text fields')
    def get_text_fields(self) -> typing.List[str]:
        return driver.findAllObjects(self._field_object.real_name)

    @allure.step('Click Plug in reader')
    def plugin_reader(self):
        time.sleep(1)
        self._plugin_reader_button.click()
        time.sleep(2)
        return self

    @allure.step('Click Register keycard')
    def register_keycard(self):
        time.sleep(1)
        if not self._register_keycard_button.is_visible:
            self._scroll.vertical_down_to(self._register_keycard_button)
        self._register_keycard_button.click()
        time.sleep(1)
        return self

    @allure.step('Click Remove keycard')
    def remove_keycard(self):
        time.sleep(1)
        if not self._remove_keycard_button.is_visible:
            self._scroll.vertical_down_to(self._remove_keycard_button)
        self._remove_keycard_button.click()
        time.sleep(1)
        return self

    @allure.step('Click Insert Keycard 1')
    def insert_keycard_1(self):
        self._insert_keycard_1_button.click()
        time.sleep(1)
        return self

    @allure.step('Choose custom keycard from initial keycard state dropdown')
    def choose_custom_keycard(self):
        if not self._keycard_state_button.is_visible:
            self._scroll.vertical_scroll_to(self._keycard_state_button)
        self._keycard_state_button.click()
        self._custom_keycard_item.click()
        time.sleep(1)
        return self

    @allure.step('Input custom keycard details to custom text field')
    def input_custom_keycard_details(self, details: str, index: int):
        fields = self.get_text_fields
        self._scroll.vertical_scroll_to(QObject(name='', real_name=driver.objectMap.realName(fields[index])))
        driver.type(fields[index], details)
        time.sleep(1)

    @allure.step('Choose not Status keycard from initial keycard state dropdown')
    def choose_not_status_keycard(self):
        if not self._keycard_state_button.is_visible:
            self._scroll.vertical_scroll_to(self._keycard_state_button)
        self._keycard_state_button.click()
        self._not_status_keycard_item.click()
        time.sleep(1)
        return self

    @allure.step('Choose empty keycard from initial keycard state dropdown')
    def choose_empty_keycard(self):
        if not self._keycard_state_button.is_visible:
            self._scroll.vertical_scroll_to(self._keycard_state_button)
        self._keycard_state_button.click()
        self._empty_keycard_item.click()
        time.sleep(1)
        return self

    @allure.step('Choose keycard with MAX pairing slots reached from initial keycard state dropdown')
    def choose_max_slots_reached_keycard(self):
        if not self._keycard_state_button.is_visible:
            self._scroll.vertical_scroll_to(self._keycard_state_button)
        self._keycard_state_button.click()
        self._max_slots_reached_item.click()
        time.sleep(1)
        return self

    @allure.step('Choose keycard with mnemonic and metadata from initial keycard state dropdown')
    def choose_mnemonic_metadata_keycard(self):
        if not self._keycard_state_button.is_visible:
            self._scroll.vertical_scroll_to(self._keycard_state_button)
        self._keycard_state_button.click()
        self._mnemonic_metadata_item.click()
        time.sleep(1)
        return self
