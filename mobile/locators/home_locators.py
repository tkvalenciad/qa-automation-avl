from appium.webdriver.common.appiumby import AppiumBy


class HomeLocators:
    CART = (AppiumBy.ACCESSIBILITY_ID, "cart badge")

    BACKPACK = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("store item text").text("Sauce Labs Backpack")',
    )

    PRODUCTS_SCREEN = (AppiumBy.ACCESSIBILITY_ID, "products screen")
