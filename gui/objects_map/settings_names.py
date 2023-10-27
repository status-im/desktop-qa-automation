from gui.objects_map.main_names import statusDesktop_mainWindow
from objectmaphelper import *

mainWindow_ProfileLayout = {"container": statusDesktop_mainWindow, "type": "ProfileLayout", "unnamed": 1, "visible": True}
mainWindow_StatusSectionLayout_ContentItem = {"container": mainWindow_ProfileLayout, "objectName": "StatusSectionLayout", "type": "ContentItem", "visible": True}
settingsContentBase_ScrollView = {"container": statusDesktop_mainWindow, "objectName": "settingsContentBaseScrollView", "type": "StatusScrollView", "visible": True}
settingsContentBaseScrollView_Flickable = {"container": settingsContentBase_ScrollView, "type": "Flickable", "unnamed": 1, "visible": True}

# Left Panel
mainWindow_LeftTabView = {"container": mainWindow_StatusSectionLayout_ContentItem, "type": "LeftTabView", "unnamed": 1, "visible": True}
mainWindow_Settings_StatusNavigationPanelHeadline = {"container": mainWindow_LeftTabView, "type": "StatusNavigationPanelHeadline", "unnamed": 1, "visible": True}
mainWindow_scrollView_StatusScrollView = {"container": mainWindow_LeftTabView, "id": "scrollView", "type": "StatusScrollView", "unnamed": 1, "visible": True}
scrollView_MenuItem_StatusNavigationListItem = {"container": mainWindow_scrollView_StatusScrollView, "type": "StatusNavigationListItem", "visible": True}
scrollView_Flickable = {"container": mainWindow_scrollView_StatusScrollView, "type": "Flickable", "unnamed": 1, "visible": True}

# Communities View
mainWindow_CommunitiesView = {"container": statusDesktop_mainWindow, "type": "CommunitiesView", "unnamed": 1, "visible": True}
mainWindow_settingsContentBaseScrollView_StatusScrollView = {"container": mainWindow_CommunitiesView, "objectName": "settingsContentBaseScrollView", "type": "StatusScrollView", "visible": True}
settingsContentBaseScrollView_listItem_StatusListItem = {"container": mainWindow_settingsContentBaseScrollView_StatusScrollView, "id": "listItem", "type": "StatusListItem", "unnamed": 1, "visible": True}
# Templates to generate Real Name in test
settings_iconOrImage_StatusSmartIdenticon = {"id": "iconOrImage", "type": "StatusSmartIdenticon", "unnamed": 1, "visible": True}
settings_Name_StatusTextWithLoadingState = {"type": "StatusTextWithLoadingState", "unnamed": 1, "visible": True}
settings_statusListItemSubTitle = {"objectName": "statusListItemSubTitle", "type": "StatusTextWithLoadingState", "visible": True}
settings_member_StatusTextWithLoadingState = {"text": "1 member", "type": "StatusTextWithLoadingState", "unnamed": 1, "visible": True}
settings_StatusFlatButton = {"type": "StatusFlatButton", "unnamed": 1, "visible": True}

# Messaging View
mainWindow_MessagingView = {"container": statusDesktop_mainWindow, "type": "MessagingView", "unnamed": 1, "visible": True}
contactsListItem_btn_StatusContactRequestsIndicatorListItem = {"container": mainWindow_MessagingView, "objectName": "MessagingView_ContactsListItem_btn", "type": "StatusContactRequestsIndicatorListItem", "visible": True}

# Contacts View
mainWindow_ContactsView = {"container": statusDesktop_mainWindow, "type": "ContactsView", "unnamed": 1, "visible": True}
mainWindow_Send_contact_request_to_chat_key_StatusButton = {"checkable": False, "container": mainWindow_ContactsView, "objectName": "ContactsView_ContactRequest_Button", "type": "StatusButton", "visible": True}
contactsTabBar_Pending_Requests_StatusTabButton = {"checkable": True, "container": mainWindow_ContactsView, "objectName": "ContactsView_PendingRequest_Button", "type": "StatusTabButton", "visible": True}
settingsContentBaseScrollView_ContactListPanel = {"container": mainWindow_ContactsView, "objectName": "ContactListPanel_ListView", "type": "StatusListView", "visible": True}

# Keycard Settings View
mainWindow_KeycardView = {"container": statusDesktop_mainWindow, "type": "KeycardView", "unnamed": 1, "visible": True}
setupFromExistingKeycardAccount_StatusListItem = {"container": settingsContentBase_ScrollView, "objectName": "setupFromExistingKeycardAccount", "type": "StatusListItem", "visible": True}
createNewKeycardAccount_StatusListItem = {"container": settingsContentBase_ScrollView, "objectName": "createNewKeycardAccount", "type": "StatusListItem", "visible": True}
importRestoreKeycard_StatusListItem = {"container": settingsContentBase_ScrollView, "objectName": "importRestoreKeycard", "type": "StatusListItem", "visible": True}
importFromKeycard_StatusListItem = {"container": settingsContentBase_ScrollView, "objectName": "importFromKeycard", "type": "StatusListItem", "visible": True}
checkWhatsNewKeycard_StatusListItem = {"container": settingsContentBase_ScrollView, "objectName": "checkWhatsNewKeycard", "type": "StatusListItem", "visible": True}
factoryResetKeycard_StatusListItem = {"container": settingsContentBase_ScrollView, "objectName": "factoryResetKeycard", "type": "StatusListItem", "visible": True}

# Wallet Settings View
mainWindow_WalletView = {"container": statusDesktop_mainWindow, "type": "WalletView", "unnamed": 1, "visible": True}
settings_Wallet_MainView_Networks = {"container": statusDesktop_mainWindow, "objectName": "networksItem", "type": "StatusListItem"}
settings_Wallet_MainView_AddNewAccountButton = {"container": statusDesktop_mainWindow, "objectName": "settings_Wallet_MainView_AddNewAccountButton", "type": "StatusButton", "visible": True}
settingsContentBaseScrollView_accountOrderItem_StatusListItem = {"container": settingsContentBase_ScrollView, "objectName": "accountOrderItem", "type": "StatusListItem", "visible": True}
settingsContentBaseScrollView_StatusListItem = {"container": settingsContentBase_ScrollView, "type": "StatusListItem", "unnamed": 1, "visible": True}
settings_Wallet_NetworksView_TestNet_Toggle = {"container": statusDesktop_mainWindow, "objectName": "testnetModeSwitch", "type": "StatusSwitch"}
settings_Wallet_NetworksView_TestNet_Toggle_Title = {"container": settingsContentBase_ScrollView, "objectName": "statusListItemSubTitle", "type": "StatusTextWithLoadingState", "visible": True}
settingsContentBaseScrollView_Goerli_testnet_active_StatusBaseText = {"container": settingsContentBase_ScrollView, "type": "StatusBaseText", "unnamed": 1, "visible": True}
settingsContentBaseScrollView_accountsList_StatusListView = {"container": settingsContentBase_ScrollView, "id": "accountsList", "type": "StatusListView", "unnamed": 1, "visible": True}
settingsContentBaseScrollView_draggableDelegate_StatusDraggableListItem = {"checkable": False, "container": settingsContentBase_ScrollView, "id": "draggableDelegate", "type": "StatusDraggableListItem", "unnamed": 1, "visible": True}
settingsContentBaseScrollView_accountOrderView_AccountOrderView = {"container": settingsContentBase_ScrollView, "id": "accountOrderView", "type": "AccountOrderView", "unnamed": 1, "visible": True}
settingsContentBaseScrollView_StatusBaseText = {"container": settingsContentBase_ScrollView, "type": "StatusBaseText", "unnamed": 1, "visible": True}
mainWindow_StatusToolBar = {"container": statusDesktop_mainWindow, "objectName": "statusToolBar", "type": "StatusToolBar", "visible": True}
main_toolBar_back_button = {"container": mainWindow_StatusToolBar, "objectName": "toolBarBackButton", "type": "StatusFlatButton", "visible": True}
settingsContentBaseScrollView_WalletNetworkDelegate_template = {"container": settingsContentBase_ScrollView, "objectName": "walletNetworkDelegate_Mainnet_1", "type": "WalletNetworkDelegate", "visible": True}
networkSettingsNetworks_Mainnet = {"container": settingsContentBase_ScrollView, "objectName": "walletNetworkDelegate_Mainnet_1", "type": "WalletNetworkDelegate", "visible": True}
networkSettingsNetworks_Mainnet_Goerli = {"container": settingsContentBase_ScrollView, "objectName": "walletNetworkDelegate_Mainnet_5", "type": "WalletNetworkDelegate", "visible": True}
networkSettingsNetworks_Optimism = {"container": settingsContentBase_ScrollView, "objectName": "walletNetworkDelegate_Optimism_10", "type": "WalletNetworkDelegate", "visible": True}
networkSettingsNetworks_Optimism_Goerli = {"container": settingsContentBase_ScrollView, "objectName": "walletNetworkDelegate_Optimism_420", "type": "WalletNetworkDelegate", "visible": True}
networkSettingsNetworks_Arbitrum = {"container": settingsContentBase_ScrollView, "objectName": "walletNetworkDelegate_Arbitrum_42161", "type": "WalletNetworkDelegate", "visible": True}
networkSettingsNetworks_Arbitrum_Goerli = {"container": settingsContentBase_ScrollView, "objectName": "walletNetworkDelegate_Arbitrum_421613", "type": "WalletNetworkDelegate", "visible": True}
networkSettingsNetworks_Mainnet_Goerli_sensor = {"container": networkSettingsNetworks_Mainnet_Goerli, "objectName": "walletNetworkDelegate_Mainnet_5_sensor", "id": "sensor", "type": "MouseArea", "unnamed": 1, "visible": True}
networkSettingsNetowrks_Mainnet_Testlabel = {"container": networkSettingsNetworks_Mainnet_Goerli_sensor, "objectName": "testnetLabel_Mainnet", "type": "StatusBaseText", "visible": True}
settingsWalletAccountDelegate_Status_account = {"container": settingsContentBase_ScrollView, "objectName": "Status account", "type": "WalletAccountDelegate", "visible": True}
settingsWalletAccountDelegate = {"container": settingsContentBase_ScrollView, "objectName": RegularExpression("*"), "type": "WalletAccountDelegate", "visible": True}

# Wallet Account Details view
walletAccountViewEditAccountButton = {"container": statusDesktop_mainWindow, "objectName": "walletAccountViewEditAccountButton", "type": "StatusButton"}
walletAccountViewAccountName = {"container": statusDesktop_mainWindow, "objectName": "walletAccountViewAccountName", "type": "StatusBaseText"}
walletAccountViewAccountEmoji = {"container": statusDesktop_mainWindow, "objectName": "walletAccountViewAccountImage", "type": "StatusEmoji", "visible": True}
walletAccountViewDeleteAccountButton = {"container": statusDesktop_mainWindow, "objectName": "deleteAccountButton", "type": "StatusButton"}
walletAccountViewDetailsLabel = {"container": settingsContentBase_ScrollView, "objectName": "AccountDetails_TextLabel", "type": "StatusBaseText"}
walletAccountViewBalance = {"container": settingsContentBase_ScrollView, "objectName": "Balance_ListItem", "type": "WalletAccountDetailsListItem"}
walletAccountViewAddress = {"container": settingsContentBase_ScrollView, "objectName": "Address_ListItem", "type": "WalletAccountDetailsListItem"}
walletAccountViewKeypairItem = {"container": settingsContentBase_ScrollView, "objectName": "KeyPair_Item", "type": "WalletAccountDetailsKeypairItem"}
walletAccountViewOrigin = {"container": settingsContentBase_ScrollView, "objectName": "Origin_ListItem", "type": "WalletAccountDetailsListItem"}
walletAccountViewDerivationPath = {"container": settingsContentBase_ScrollView, "objectName": "DerivationPath_ListItem", "type": "WalletAccountDetailsListItem"}
walletAccountViewStored = {"container": settingsContentBase_ScrollView, "objectName": "Stored_ListItem", "type": "WalletAccountDetailsListItem"}
walletAccountViewPreferredNetworks = {"container": settingsContentBase_ScrollView, "objectName": "PreferredNetworks_ListItem", "type": "StatusListItem"}

# Wallet edit network view
settingsContentBaseScrollView_editPreviwTabBar_StatusTabBar = {"container": statusDesktop_mainWindow, "objectName": "editPreviwTabBar", "type": "StatusTabBar"}
editNetworkLiveButton = {"container": settingsContentBaseScrollView_editPreviwTabBar_StatusTabBar, "objectName": "editNetworkLiveButton", "type": "StatusTabButton"}
editNetworkTestButton = {"container": settingsContentBaseScrollView_editPreviwTabBar_StatusTabBar, "objectName": "editNetworkTestButton", "type": "StatusTabButton"}
editNetworkNameInput = {"container": statusDesktop_mainWindow, "objectName": "editNetworkNameInput", "type": "TextEdit"}
editNetworkShortNameInput = {"container": statusDesktop_mainWindow, "objectName": "editNetworkShortNameInput", "type": "TextEdit"}
editNetworkChainIdInput = {"container": statusDesktop_mainWindow, "objectName": "editNetworkChainIdInput", "type": "TextEdit"}
editNetworkSymbolInput = {"container": statusDesktop_mainWindow, "objectName": "editNetworkSymbolInput", "type": "TextEdit"}
editNetworkMainRpcInput = {"container": statusDesktop_mainWindow, "objectName": "editNetworkMainRpcInput", "type": "TextEdit", "visible": True}
editNetworkFailoverRpcUrlInput = {"container": statusDesktop_mainWindow, "objectName": "editNetworkFailoverRpcUrlInput", "type": "TextEdit", "visible": True}
editNetworkExplorerInput = {"container": statusDesktop_mainWindow, "objectName": "editNetworkExplorerInput", "type": "TextEdit"}
editNetworkAknowledgmentCheckbox = {"container": statusDesktop_mainWindow, "objectName": "editNetworkAknowledgmentCheckbox", "type": "StatusCheckBox", "visible": True}
editNetworkRevertButton = {"container": statusDesktop_mainWindow, "objectName": "editNetworkRevertButton", "type": "StatusButton"}
editNetworkSaveButton = {"container": statusDesktop_mainWindow, "objectName": "editNetworkSaveButton", "type": "StatusButton"}
mainRpcUrlInputObject = {"container": settingsContentBase_ScrollView, "objectName": "mainRpcInputObject", "type": "StatusInput", "visible": True}
failoverRpcUrlInputObject = {"container": settingsContentBase_ScrollView, "objectName": "failoverRpcUrlInputObject", "type": "StatusInput", "visible": True}

# Profile View
mainWindow_MyProfileView = {"container": statusDesktop_mainWindow, "type": "MyProfileView", "unnamed": 1, "visible": True}
displayName_StatusInput = {"container": statusDesktop_mainWindow, "objectName": "displayNameInput", "type": "StatusInput", "visible": True}
displayName_TextEdit = {"container": displayName_StatusInput, "type": "TextEdit", "unnamed": 1, "visible": True}
change_password_button = {"container": statusDesktop_mainWindow, "type": "StatusButton", "objectName": "profileSettingsChangePasswordButton", "visible": True}
bio_StatusInput = {"container": statusDesktop_mainWindow, "objectName": "bioInput", "type": "StatusInput", "visible": True}
bio_TextEdit = {"container": bio_StatusInput, "type": "TextEdit", "unnamed": 1, "visible": True}
addMoreSocialLinks = {"container": statusDesktop_mainWindow, "objectName": "addMoreSocialLinks", "type": "StatusLinkText", "visible": True}

# Syncing Settings View
mainWindow_SyncingView = {"container": statusDesktop_mainWindow, "type": "SyncingView", "unnamed": 1, "visible": True}
settings_Setup_Syncing_StatusButton = {"container": statusDesktop_mainWindow, "objectName": "setupSyncingStatusButton", "type": "StatusButton", "visible": True}
settings_Backup_Data_StatusButton = {"container": settingsContentBase_ScrollView, "objectName": "setupSyncBackupDataButton", "type": "StatusButton", "visible": True}
settings_Sync_New_Device_Header = {"container": settingsContentBase_ScrollView, "objectName": "syncNewDeviceTextLabel", "type": "StatusBaseText", "visible": True}
settings_Sync_New_Device_SubTitle = {"container": settingsContentBase_ScrollView, "objectName": "syncNewDeviceSubTitleTextLabel", "type": "StatusBaseText", "visible": True}
