import allure
import pytest
from allure import step

import configs
import constants
import driver
from constants import ColorCodes
from constants.keycard import Keycard
from gui.main_window import MainWindow
from gui.mocked_keycard_controller import MockedKeycardController


@allure.testcase('https://ethstatus.testrail.net/index.php?/cases/view/703625',
                 'Import or restore a Keycard via a seed phrase')
@pytest.mark.case(703625)
@pytest.mark.parametrize('user_account', [constants.user.user_account_one])
def test_import_restore_keycard_via_seed_phrase(main_screen: MainWindow, user_account):
    with step('Choose option Import or restore account via seed phrase in settings'):
        main_screen.prepare()
        keycard_settings = main_screen.left_panel.open_settings().left_panel.open_keycard_settings()
        keycard_popup = keycard_settings.click_import_restore_via_seed_phrase()

    with (step('Verify displayed keycard popup instructions are correct')):
        with step('Verify header is correct'):
            assert keycard_popup.keycard_header == Keycard.KEYCARD_POPUP_HEADER.value, "The header is incorrect"
        with step('Verify instructions are correct'):
            assert Keycard.KEYCARD_INSTRUCTIONS_PLUG_IN.value in keycard_popup.keycard_instructions, \
                "There is no correct keycard instruction"

    with step('Plug in reader'):
        main_screen.hide()
        keycard_controller = MockedKeycardController().wait_until_appears()
        keycard_controller.plugin_reader()
        main_screen.show()

    with step('Verify displayed keycard popup instructions are correct'):
        assert driver.waitFor(
            lambda: Keycard.KEYCARD_INSTRUCTIONS_INSERT_KEYCARD.value in keycard_popup.keycard_instructions,
            configs.timeouts.UI_LOAD_TIMEOUT_MSEC), "There is no correct keycard instruction"

    with step('Register and insert keycard'):
        main_screen.hide()
        keycard_controller.register_keycard()
        keycard_controller.insert_keycard_1()
        main_screen.show()

    with step('Verify displayed keycard popup instructions are correct'):
        with step('Verify keycard is recognized'):
            assert driver.waitFor(lambda: Keycard.KEYCARD_RECOGNIZED.value in keycard_popup.keycard_instructions,
                                  configs.timeouts.UI_LOAD_TIMEOUT_MSEC), "There is no correct keycard instruction"
        with step('Verify that asked to choose PIN'):
            assert driver.waitFor(lambda: Keycard.KEYCARD_CHOOSE_PIN.value in keycard_popup.keycard_instructions,
                                  configs.timeouts.UI_LOAD_TIMEOUT_MSEC), "There is no correct keycard instruction"
            assert Keycard.KEYCARD_NOTE.value in keycard_popup.keycard_instructions

    with step('Insert PIN and repeat PIN and verify keycard popup instructions are correct'):
        pin = Keycard.KEYCARD_PIN.value
        keycard_popup.input_pin(pin)
        assert driver.waitFor(lambda: Keycard.KEYCARD_REPEAT_PIN.value in keycard_popup.keycard_instructions), \
            "There is no correct keycard instruction"
        keycard_popup.input_pin(pin)
        assert driver.waitFor(lambda: Keycard.KEYCARD_PIN_SET.value in keycard_popup.keycard_instructions), \
            "There is no correct keycard instruction"

    with step('Import keycard via seed phrase'):
        keycard_name = Keycard.KEYCARD_NAME.value
        account_name = Keycard.ACCOUNT_NAME.value
        keycard_popup.import_keycard_via_seed_phrase(keycard_name, account_name)

    with step('Verify that preview shows correct keycard and account name and color and instructions are correct'):
        assert driver.waitFor(lambda: Keycard.KEYCARD_NEW_ACCOUNT_CREATED.value in keycard_popup.keycard_instructions), \
            "There is no correct keycard instruction"

        assert keycard_popup.keycard_preview_name == keycard_name, "Keycard name in preview is incorrect"
        assert keycard_popup.account_preview_name == account_name, "Account name in preview is incorrect"
        assert keycard_popup.preview_color == ColorCodes.BLUE.value, "Color in preview is incorrect"

        keycard_popup.click_next()

