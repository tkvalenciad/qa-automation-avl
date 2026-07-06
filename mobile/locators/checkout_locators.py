from appium.webdriver.common.appiumby import AppiumBy


class CheckoutLocators:
    FULL_NAME = (AppiumBy.ACCESSIBILITY_ID, "Full Name* input field")
    ADDRESS = (AppiumBy.ACCESSIBILITY_ID, "Address Line 1* input field")
    CITY = (AppiumBy.ACCESSIBILITY_ID, "City* input field")
    ZIP_CODE = (AppiumBy.ACCESSIBILITY_ID, "Zip Code* input field")
    COUNTRY = (AppiumBy.ACCESSIBILITY_ID, "Country* input field")
    TO_PAYMENT = (AppiumBy.ACCESSIBILITY_ID, "To Payment button")
    CHECKOUT_ADDRESS_SCREEN = (AppiumBy.ACCESSIBILITY_ID, "checkout address screen")
    PAYMENT_SCREEN = (AppiumBy.ACCESSIBILITY_ID, "checkout payment screen")
