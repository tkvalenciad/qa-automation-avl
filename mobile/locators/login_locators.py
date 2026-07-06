from appium.webdriver.common.appiumby import AppiumBy


class LoginLocators:
    USERNAME = (AppiumBy.ACCESSIBILITY_ID, "Username input field")
    PASSWORD = (AppiumBy.ACCESSIBILITY_ID, "Password input field")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Login button")
    ERROR_MESSAGE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("credentials")',
    )
    LOGIN_SCREEN = (AppiumBy.ACCESSIBILITY_ID, "login screen")
    SAMPLE_USER = (AppiumBy.ACCESSIBILITY_ID, "bob@example.com-autofill")
    SAMPLE_USER_SCROLL = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true))'
        '.scrollIntoView(new UiSelector().description("bob@example.com-autofill"))',
    )
