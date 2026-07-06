from appium.webdriver.common.appiumby import AppiumBy


class ProductLocators:
    ADD_TO_CART = (AppiumBy.ACCESSIBILITY_ID, "Add To Cart button")
    PRODUCT_SCREEN = (AppiumBy.ACCESSIBILITY_ID, "product screen")

    PRODUCT_TITLE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Sauce Labs Backpack")',
    )
