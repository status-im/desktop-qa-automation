statusDesktop_mainWindow = {"name": "mainWindow", "type": "StatusWindow"}
mainWindow_StatusWindow = {"name": "mainWindow", "type": "StatusWindow", "visible": True}
statusDesktop_mainWindow_overlay = {"container": statusDesktop_mainWindow, "type": "Overlay", "unnamed": 1, "visible": True}
statusDesktop_mainWindow_overlay_popup2 = {"container": statusDesktop_mainWindow_overlay, "occurrence": 2, "type": "PopupItem", "unnamed": 1, "visible": True}
scrollView_StatusScrollView = {"container": statusDesktop_mainWindow_overlay, "id": "scrollView", "type": "StatusScrollView", "unnamed": 1, "visible": True}
splashScreen = {"container": statusDesktop_mainWindow, "objectName": "splashScreen", "type": "DidYouKnowSplashScreen"}
settingsSave_StatusButton = {"container": statusDesktop_mainWindow, "objectName": "settingsDirtyToastMessageSaveButton", "type": "StatusButton", "visible": True}

# Main right panel
mainWindow_RighPanel = {"container": statusDesktop_mainWindow, "type": "ColumnLayout", "objectName": "mainRightView", "visible": True}

# Navigation Panel
mainWindow_StatusAppNavBar = {"container": statusDesktop_mainWindow, "type": "StatusAppNavBar", "unnamed": 1, "visible": True}
messages_navbar_StatusNavBarTabButton = {"checkable": True, "container": mainWindow_StatusAppNavBar, "objectName": "Messages-navbar", "type": "StatusNavBarTabButton", "visible": True}
communities_Portal_navbar_StatusNavBarTabButton = {"checkable": True, "container": mainWindow_StatusAppNavBar, "objectName": "Communities Portal-navbar", "type": "StatusNavBarTabButton", "visible": True}
wallet_navbar_StatusNavBarTabButton = {"checkable": True, "container": mainWindow_StatusAppNavBar, "objectName": "Wallet-navbar", "type": "StatusNavBarTabButton", "visible": True}
settings_navbar_StatusNavBarTabButton = {"checkable": True, "container": mainWindow_StatusAppNavBar, "objectName": "Settings-navbar", "type": "StatusNavBarTabButton", "visible": True}
mainWindow_ProfileNavBarButton = {"container": statusDesktop_mainWindow, "objectName": "statusProfileNavBarTabButton", "type": "StatusNavBarTabButton", "visible": True}
mainWindow_statusCommunityMainNavBarListView_ListView = {"container": statusDesktop_mainWindow, "objectName": "statusCommunityMainNavBarListView", "type": "ListView", "visible": True}
statusCommunityMainNavBarListView_CommunityNavBarButton = {"checkable": True, "container": mainWindow_statusCommunityMainNavBarListView_ListView, "objectName": "CommunityNavBarButton", "type": "StatusNavBarTabButton", "visible": True}
invite_People_StatusMenuItem = {"container": statusDesktop_mainWindow_overlay, "enabled": True, "objectName": "invitePeople", "type": "StatusMenuItem", "visible": True}

# Banners
secureYourSeedPhraseBanner_ModuleWarning = {"container": statusDesktop_mainWindow, "objectName": "secureYourSeedPhraseBanner", "type": "ModuleWarning", "visible": True}

# Notifications
mainWindow_ephemeralNotificationList_StatusListView = {"container": mainWindow_StatusWindow, "objectName": "ephemeralNotificationList", "type": "StatusListView", "visible": True}
ephemeralNotificationList_statusToastMessage_StatusToastMessage = {"container": mainWindow_ephemeralNotificationList_StatusListView, "index": 0, "objectName": "statusToastMessage", "type": "StatusToastMessage", "visible": True}
statusToastMessage_Transaction_pending_StatusBaseText = {"container": ephemeralNotificationList_statusToastMessage_StatusToastMessage, "type": "StatusBaseText", "unnamed": 1, "visible": True}
