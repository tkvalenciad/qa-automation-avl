from appium.webdriver.common.appiumby import AppiumBy


class MenuLocators:
    MENU = (AppiumBy.ACCESSIBILITY_ID, "open menu")
    CATALOG_MENU_ITEM = (AppiumBy.ACCESSIBILITY_ID, "menu item catalog")
    LOGIN_MENU_ITEM = (AppiumBy.ACCESSIBILITY_ID, "menu item log in")
    LOGOUT_MENU_ITEM = (AppiumBy.ACCESSIBILITY_ID, "menu item log out")
    LOGOUT_CONFIRM_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("LOG OUT")',
    )
    DIALOG_OK_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("OK")',
    )
    LOGIN_IN_VIEW = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true))'
        '.scrollIntoView(new UiSelector().description("menu item log in"))',
    )
