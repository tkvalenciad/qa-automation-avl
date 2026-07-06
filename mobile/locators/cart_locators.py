from appium.webdriver.common.appiumby import AppiumBy


class CartLocators:
    CART_BADGE_COUNT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("cart badge")'
        '.childSelector(new UiSelector().className("android.widget.TextView"))',
    )

    PRODUCT_NAME = (AppiumBy.ACCESSIBILITY_ID, "product label")
    PROCEED_TO_CHECKOUT = (AppiumBy.ACCESSIBILITY_ID, "Proceed To Checkout button")
    CART_SCREEN = (AppiumBy.ACCESSIBILITY_ID, "cart screen")
