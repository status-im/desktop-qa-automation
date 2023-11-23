import allure

from gui.components.community.create_community_popups import CreateCommunitiesBanner, CreateCommunityPopup
from gui.elements.button import Button
from gui.elements.object import QObject


class CommunitiesPortal(QObject):

    def __init__(self):
        super().__init__('mainWindow_communitiesPortalLayout_CommunitiesPortalLayout')
        self._create_community_button = Button('mainWindow_Create_New_Community_StatusButton')

    @allure.step('Open create community popup')
    def open_create_community_popup(self) -> CreateCommunityPopup:
        self._create_community_button.click()
        return CreateCommunitiesBanner().open_create_community_popup()
