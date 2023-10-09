from .main_names import statusDesktop_mainWindow, statusDesktop_mainWindow_overlay

# Community Portal
mainWindow_communitiesPortalLayout_CommunitiesPortalLayout = {"container": statusDesktop_mainWindow, "objectName": "communitiesPortalLayout", "type": "CommunitiesPortalLayout", "visible": True}
mainWindow_Create_New_Community_StatusButton = {"checkable": False, "container": mainWindow_communitiesPortalLayout_CommunitiesPortalLayout, "objectName": "createCommunityButton", "type": "StatusButton", "visible": True}

# Community View
mainWindow_communityLoader_Loader = {"container": statusDesktop_mainWindow, "id": "communityLoader", "type": "Loader", "unnamed": 1, "visible": True}
# Left Panel
mainWindow_communityColumnView_CommunityColumnView = {"container": mainWindow_communityLoader_Loader, "objectName": "communityColumnView", "type": "CommunityColumnView", "visible": True}
mainWindow_communityHeaderButton_StatusChatInfoButton = {"checkable": False, "container": mainWindow_communityColumnView_CommunityColumnView, "objectName": "communityHeaderButton", "type": "StatusChatInfoButton", "visible": True}
mainWindow_identicon_StatusSmartIdenticon = {"container": mainWindow_communityHeaderButton_StatusChatInfoButton, "id": "identicon", "type": "StatusSmartIdenticon", "unnamed": 1, "visible": True}
mainWindow_statusChatInfoButtonNameText_TruncatedTextWithTooltip = {"container": mainWindow_communityHeaderButton_StatusChatInfoButton, "objectName": "statusChatInfoButtonNameText", "type": "TruncatedTextWithTooltip", "visible": True}
mainWindow_Members_TruncatedTextWithTooltip = {"container": mainWindow_communityHeaderButton_StatusChatInfoButton, "type": "TruncatedTextWithTooltip", "unnamed": 1, "visible": True}
mainWindow_startChatButton_StatusIconTabButton = {"checkable": True, "container": mainWindow_communityColumnView_CommunityColumnView, "objectName": "startChatButton", "type": "StatusIconTabButton", "visible": True}
mainWindow_createChatOrCommunity_Loader = {"container": mainWindow_communityColumnView_CommunityColumnView, "id": "createChatOrCommunity", "type": "Loader", "unnamed": 1, "visible": True}
mainWindow_scrollView_StatusScrollView = {"container": mainWindow_communityColumnView_CommunityColumnView, "id": "scrollView", "type": "StatusScrollView", "unnamed": 1, "visible": True}
scrollView_Flickable = {"container": mainWindow_scrollView_StatusScrollView, "type": "Flickable", "unnamed": 1, "visible": True}
scrollView_chatListItems_StatusListView = {"container": scrollView_Flickable, "objectName": "chatListItems", "type": "StatusListView", "visible": True}
channel_listItem = {"container": scrollView_chatListItems_StatusListView, "id": "chatListDelegate", "type": "DropArea", "isCategory": False, "visible": True}
channel_identicon_StatusSmartIdenticon = {"container": None, "id": "identicon", "type": "StatusSmartIdenticon", "unnamed": 1, "visible": True}
channel_name_StatusBaseText = {"container": None, "type": "StatusBaseText", "unnamed": 1, "visible": True}
mainWindow_createChannelOrCategoryBtn_StatusBaseText = {"container": mainWindow_communityColumnView_CommunityColumnView, "objectName": "createChannelOrCategoryBtn", "type": "StatusBaseText", "visible": True}
create_channel_StatusMenuItem = {"container": statusDesktop_mainWindow_overlay, "enabled": True, "objectName": "createCommunityChannelBtn", "type": "StatusMenuItem", "visible": True}
mainWindow_Join_Community_StatusButton = {"checkable": False, "container": mainWindow_communityColumnView_CommunityColumnView, "id": "joinCommunityButton", "text": "Join Community", "type": "StatusButton", "unnamed": 1, "visible": True}

# Tool Bar
mainWindow_statusToolBar_StatusToolBar = {"container": mainWindow_communityLoader_Loader, "objectName": "statusToolBar", "type": "StatusToolBar", "visible": True}
statusToolBar_chatToolbarMoreOptionsButton = {"container": mainWindow_statusToolBar_StatusToolBar, "objectName": "chatToolbarMoreOptionsButton", "type": "StatusFlatRoundButton", "visible": True}
delete_Channel_StatusMenuItem = {"checkable": False, "container": statusDesktop_mainWindow_overlay, "enabled": True, "objectName": "deleteOrLeaveMenuItem", "type": "StatusMenuItem", "visible": True}
edit_Channel_StatusMenuItem = {"checkable": False, "container": statusDesktop_mainWindow_overlay, "enabled": True, "objectName": "editChannelMenuItem", "type": "StatusMenuItem", "visible": True}
statusToolBar_statusSmartIdenticonLetter_StatusLetterIdenticon = {"container": mainWindow_statusToolBar_StatusToolBar, "objectName": "statusSmartIdenticonLetter", "type": "StatusLetterIdenticon", "visible": True}
statusToolBar_statusChatInfoButtonNameText_TruncatedTextWithTooltip = {"container": mainWindow_statusToolBar_StatusToolBar, "objectName": "statusChatInfoButtonNameText", "type": "TruncatedTextWithTooltip", "visible": True}
statusToolBar_TruncatedTextWithTooltip = {"container": mainWindow_statusToolBar_StatusToolBar, "type": "TruncatedTextWithTooltip", "unnamed": 1, "visible": True}

# Chat
mainWindow_ChatColumnView = {"container": mainWindow_communityLoader_Loader, "type": "ChatColumnView", "unnamed": 1, "visible": True}
chatMessageViewDelegate_channelIdentifierNameText_StyledText = {"container": mainWindow_ChatColumnView, "objectName": "channelIdentifierNameText", "type": "StyledText", "visible": True}
chatMessageViewDelegate_Welcome = {"container": mainWindow_ChatColumnView, "type": "StatusBaseText", "unnamed": 1, "visible": True}
chatMessageViewDelegate_channelIdentifierSmartIdenticon_StatusSmartIdenticon = {"container": mainWindow_ChatColumnView, "objectName": "channelIdentifierSmartIdenticon", "type": "StatusSmartIdenticon", "visible": True}

# Community Settings
mainWindow_communitySettingsBackToCommunityButton_StatusBaseText = {"container": mainWindow_communityLoader_Loader, "objectName": "communitySettingsBackToCommunityButton", "type": "StatusBaseText", "visible": True}
mainWindow_listView_StatusListView = {"container": mainWindow_communityLoader_Loader, "id": "listView", "type": "StatusListView", "unnamed": 1, "visible": True}
overview_StatusNavigationListItem = {"container": mainWindow_listView_StatusListView, "objectName": "CommunitySettingsView_NavigationListItem_Overview", "type": "StatusNavigationListItem", "visible": True}
members_StatusNavigationListItem = {"container": mainWindow_listView_StatusListView, "index": 1, "objectName": "CommunitySettingsView_NavigationListItem_Members", "type": "StatusNavigationListItem", "visible": True}
permissions_StatusNavigationListItem = {"container": mainWindow_listView_StatusListView, "index": 2, "objectName": "CommunitySettingsView_NavigationListItem_Permissions", "type": "StatusNavigationListItem", "visible": True}

# Overview Settings View
mainWindow_OverviewSettingsPanel = {"container": mainWindow_communityLoader_Loader, "type": "OverviewSettingsPanel", "unnamed": 1, "visible": True}
communityOverviewSettingsCommunityName_StatusBaseText = {"container": mainWindow_OverviewSettingsPanel, "objectName": "communityOverviewSettingsCommunityName", "type": "StatusBaseText", "visible": True}
communityOverviewSettingsCommunityDescription_StatusBaseText = {"container": mainWindow_OverviewSettingsPanel,  "objectName": "communityOverviewSettingsCommunityDescription", "type": "StatusBaseText", "visible": True}
mainWindow_Edit_Community_StatusButton = {"checkable": False, "container": mainWindow_OverviewSettingsPanel, "objectName": "communityOverviewSettingsEditCommunityButton", "text": "Edit Community", "type": "StatusButton", "visible": True}
# Members Settings View
mainWindow_MembersSettingsPanel = {"container": mainWindow_communityLoader_Loader, "type": "MembersSettingsPanel", "unnamed": 1, "visible": True}
embersListViews_ListView = {"container": mainWindow_MembersSettingsPanel, "objectName": "CommunityMembersTabPanel_MembersListViews", "type": "ListView", "visible": True}
memberItem_StatusMemberListItem = {"container": embersListViews_ListView, "id": "memberItem", "type": "StatusMemberListItem", "unnamed": 1, "visible": True}
# Permissions Intro View
add_new_permission_button = {"container": statusDesktop_mainWindow, "objectName": "addNewItemButton", "type": "StatusButton", "visible": True}
# Permissions Settings View
mainWindow_editPermissionView_EditPermissionView = {"container": statusDesktop_mainWindow, "id": "editPermissionView", "type": "EditPermissionView", "unnamed": 1, "visible": True}
editPermissionView_Who_holds_StatusItemSelector = {"container": mainWindow_editPermissionView_EditPermissionView, "id": "tokensSelector", "type": "StatusItemSelector", "unnamed": 1, "visible": True}
editPermissionView_Is_allowed_to_StatusFlowSelector = {"container": mainWindow_editPermissionView_EditPermissionView, "id": "permissionsSelector", "type": "StatusFlowSelector", "unnamed": 1, "visible": True}
editPermissionView_In_StatusItemSelector = {"container": mainWindow_editPermissionView_EditPermissionView, "id": "inSelector", "type": "StatusItemSelector", "unnamed": 1, "visible": True}
editPermissionView_whoHoldsSwitch_StatusSwitch = {"checkable": True, "container": mainWindow_editPermissionView_EditPermissionView, "id": "whoHoldsSwitch", "type": "StatusSwitch", "unnamed": 1, "visible": True}
edit_TextEdit = {"container": statusDesktop_mainWindow_overlay, "type": "TextEdit", "unnamed": 1, "visible": True}
inputValue_StyledTextField = {"container": statusDesktop_mainWindow_overlay, "echoMode": 0, "id": "inputValue", "type": "StyledTextField", "unnamed": 1, "visible": True}
o_TokenItem = {"container": statusDesktop_mainWindow_overlay, "index": 0, "type": "TokenItem", "unnamed": 1, "visible": True}
add_StatusButton = {"checkable": False, "container": statusDesktop_mainWindow_overlay, "type": "StatusButton", "unnamed": 1, "visible": True}
customPermissionListItem = {"container": statusDesktop_mainWindow_overlay, "objectName": "becomeAdmin", "type": "CustomPermissionListItem", "visible": True}
communityItem_CommunityListItem = {"container": statusDesktop_mainWindow_overlay, "id": "communityItem", "type": "CommunityListItem", "unnamed": 1, "visible": True}
editPermissionView_switchItem_StatusSwitch = {"checkable": True, "container": mainWindow_editPermissionView_EditPermissionView, "id": "switchItem", "type": "StatusSwitch", "unnamed": 1, "visible": True}
editPermissionView_Create_permission_StatusButton = {"checkable": False, "container": mainWindow_editPermissionView_EditPermissionView, "text": "Create permission", "type": "StatusButton", "unnamed": 1, "visible": True}
mainWindow_PermissionsView = {"container": statusDesktop_mainWindow, "type": "PermissionsView", "unnamed": 1, "visible": True}
o_StatusListItemTag = {"container": mainWindow_PermissionsView, "type": "StatusListItemTag", "unnamed": 1, "visible": True}
o_IntroPanel = {"container": mainWindow_PermissionsView, "type": "IntroPanel", "unnamed": 1, "visible": True}
mainWindow_PermissionsSettingsPanel = {"container": statusDesktop_mainWindow, "type": "PermissionsSettingsPanel", "unnamed": 1, "visible": True}

# Edit Community
mainWindow_communityEditPanelScrollView_EditSettingsPanel = {"container": statusDesktop_mainWindow, "objectName": "communityEditPanelScrollView", "type": "EditSettingsPanel", "visible": True}
communityEditPanelScrollView_Flickable = {"container": mainWindow_communityEditPanelScrollView_EditSettingsPanel, "type": "Flickable", "unnamed": 1, "visible": True}
communityEditPanelScrollView_communityNameInput_TextEdit = {"container": mainWindow_communityEditPanelScrollView_EditSettingsPanel, "objectName": "communityNameInput", "type": "TextEdit", "visible": True}
communityEditPanelScrollView_communityDescriptionInput_TextEdit = {"container": mainWindow_communityEditPanelScrollView_EditSettingsPanel, "objectName": "communityDescriptionInput", "type": "TextEdit", "visible": True}
communityEditPanelScrollView_communityLogoPicker_LogoPicker = {"container": mainWindow_communityEditPanelScrollView_EditSettingsPanel, "objectName": "communityLogoPicker", "type": "LogoPicker", "visible": True}
communityEditPanelScrollView_image_StatusImage = {"container": communityEditPanelScrollView_communityLogoPicker_LogoPicker, "id": "image", "type": "StatusImage", "unnamed": 1, "visible": True}
communityEditPanelScrollView_editButton_StatusRoundButton = {"container": communityEditPanelScrollView_communityLogoPicker_LogoPicker, "id": "editButton", "type": "StatusRoundButton", "unnamed": 1, "visible": True}
communityEditPanelScrollView_communityBannerPicker_BannerPicker = {"container": mainWindow_communityEditPanelScrollView_EditSettingsPanel, "objectName": "communityBannerPicker", "type": "BannerPicker", "visible": True}
communityEditPanelScrollView_image_StatusImage_2 = {"container": communityEditPanelScrollView_communityBannerPicker_BannerPicker, "id": "image", "type": "StatusImage", "unnamed": 1, "visible": True}
communityEditPanelScrollView_editButton_StatusRoundButton_2 = {"container": communityEditPanelScrollView_communityBannerPicker_BannerPicker, "id": "editButton", "type": "StatusRoundButton", "unnamed": 1, "visible": True}
communityEditPanelScrollView_StatusPickerButton = {"checkable": False, "container": mainWindow_communityEditPanelScrollView_EditSettingsPanel, "type": "StatusPickerButton", "unnamed": 1, "visible": True}
communityEditPanelScrollView_communityTagsPicker_TagsPicker = {"container": mainWindow_communityEditPanelScrollView_EditSettingsPanel, "objectName": "communityTagsPicker", "type": "TagsPicker", "visible": True}
communityEditPanelScrollView_flow_Flow = {"container": communityEditPanelScrollView_communityTagsPicker_TagsPicker, "id": "flow", "type": "Flow", "unnamed": 1, "visible": True}
communityEditPanelScrollView_StatusCommunityTag = {"container": communityEditPanelScrollView_communityTagsPicker_TagsPicker, "type": "StatusCommunityTag", "unnamed": 1, "visible": True}
communityEditPanelScrollView_Choose_StatusPickerButton = {"checkable": False, "container": communityEditPanelScrollView_communityTagsPicker_TagsPicker, "type": "StatusPickerButton", "unnamed": 1, "visible": True}
communityEditPanelScrollView_archiveSupportToggle_StatusCheckBox = {"checkable": True, "container": mainWindow_communityEditPanelScrollView_EditSettingsPanel, "id": "archiveSupportToggle", "type": "StatusCheckBox", "unnamed": 1, "visible": True}
communityEditPanelScrollView_requestToJoinToggle_StatusCheckBox = {"checkable": True, "container": mainWindow_communityEditPanelScrollView_EditSettingsPanel, "id": "requestToJoinToggle", "type": "StatusCheckBox", "unnamed": 1, "visible": True}
communityEditPanelScrollView_pinMessagesToggle_StatusCheckBox = {"checkable": True, "container": mainWindow_communityEditPanelScrollView_EditSettingsPanel, "id": "pinMessagesToggle", "type": "StatusCheckBox", "unnamed": 1, "visible": True}
communityEditPanelScrollView_editCommunityIntroInput_TextEdit = {"container": mainWindow_communityEditPanelScrollView_EditSettingsPanel, "objectName": "editCommunityIntroInput", "type": "TextEdit", "visible": True}
communityEditPanelScrollView_editCommunityOutroInput_TextEdit = {"container": mainWindow_communityEditPanelScrollView_EditSettingsPanel, "objectName": "editCommunityOutroInput", "type": "TextEdit", "visible": True}
mainWindow_Save_changes_StatusButton = {"checkable": False, "container": statusDesktop_mainWindow, "objectName": "settingsDirtyToastMessageSaveButton", "text": "Save changes", "type": "StatusButton", "visible": True}

# User List Panel
mainWindow_UserListPanel = {"container": statusDesktop_mainWindow, "type": "UserListPanel", "unnamed": 1, "visible": True}
userListPanel_StatusMemberListItem = {"container": mainWindow_UserListPanel, "type": "StatusMemberListItem", "unnamed": 1, "visible": True}
