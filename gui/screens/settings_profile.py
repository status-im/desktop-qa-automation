import allure

import configs.timeouts
import driver
from driver.objects_access import walk_children
from gui.components.change_password_popup import ChangePasswordPopup
from gui.components.social_links_popup import SocialLinksPopup
from gui.elements.button import Button
from gui.elements.object import QObject
from gui.elements.scroll import Scroll
from gui.elements.text_edit import TextEdit
from gui.elements.text_label import TextLabel


class ProfileSettingsView(QObject):

    def __init__(self):
        super().__init__('mainWindow_MyProfileView')
        self._scroll_view = Scroll('settingsContentBaseScrollView_Flickable')
        self._display_name_text_field = TextEdit('displayName_TextEdit')
        self._save_button = Button('settingsSave_StatusButton')
        self._bio_text_field = TextEdit('bio_TextEdit')
        self._add_more_links_label = TextLabel('addMoreSocialLinks')
        self._links_list = QObject('linksView')
        self._web_tab_button = Button('profileTabBar_Web_StatusTabButton')
        self._identity_tab_button = Button('profileTabBar_Identity_StatusTabButton')

    @property
    @allure.step('Get display name')
    def display_name(self) -> str:
        self._identity_tab_button.click()
        return self._display_name_text_field.text

    @allure.step('Set user name')
    def set_name(self, value: str):
        self._identity_tab_button.click()
        self._display_name_text_field.text = value
        self.save_changes()

    @property
    @allure.step('Get bio')
    def bio(self) -> str:
        self._identity_tab_button.click()
        return self._bio_text_field.text

    @bio.setter
    @allure.step('Set bio')
    def bio(self, value: str):
        self._identity_tab_button.click()
        self._bio_text_field.text = value
        self.save_changes()

    @property
    @allure.step('Get social links')
    def social_links(self) -> dict:
        self._web_tab_button.click()
        links = {}
        for link_name in walk_children(
                driver.waitForObjectExists(self._links_list.real_name, configs.timeouts.UI_LOAD_TIMEOUT_MSEC)):
            if getattr(link_name, 'id', '') == 'draggableDelegate':
                for link_value in walk_children(link_name):
                    if getattr(link_value, 'id', '') == 'textMouseArea':
                        links[str(link_name.title)] = str(driver.object.parent(link_value).text)
        return links

    @social_links.setter
    @allure.step('Set social links')
    def social_links(self, links):
        links = {
            'Twitter': [links[0]],
            'Personal site': [links[1]],
            'Github': [links[2]],
            'YouTube channel': [links[3]],
            'Discord handle': [links[4]],
            'Telegram handle': [links[5]],
            'Custom link': [links[6], links[7]],
        }

        for network, link in links.items():
            social_links_popup = self.open_social_links_popup()
            social_links_popup.add_link(network, link)

    @allure.step('Verify social links')
    def verify_social_links(self, links):
        self._web_tab_button.click()
        twitter = links[0]
        personal_site = links[1]
        github = links[2]
        youtube = links[3]
        discord = links[4]
        telegram = links[5]
        custom_link_text = links[6]
        custom_link = links[7]

        actual_links = self.social_links

        assert actual_links['Twitter'] == twitter
        assert actual_links['Personal site'] == personal_site
        assert actual_links['Github'] == github
        assert actual_links['YouTube channel'] == youtube
        assert actual_links['Discord handle'] == discord
        assert actual_links['Telegram handle'] == telegram
        assert actual_links[custom_link_text] == custom_link

    @allure.step('Open social links form')
    def open_social_links_popup(self):
        self._web_tab_button.click()
        self._add_more_links_label.click()
        return SocialLinksPopup().wait_until_appears()

    @allure.step('Save changes')
    def save_changes(self):
        self._save_button.click()

