from mobile.pages.base_page import BasePage
from mobile.locators.checkout_locators import CheckoutLocators


class CheckoutPage(BasePage):

    def fill_shipping_address(self, full_name, address, city, zip_code, country):
        self._fill_field(CheckoutLocators.FULL_NAME, full_name)
        self._fill_field(CheckoutLocators.ADDRESS, address)
        self._fill_field(CheckoutLocators.CITY, city)
        self._fill_field(CheckoutLocators.ZIP_CODE, zip_code)
        self._fill_field(CheckoutLocators.COUNTRY, country)
        self.hide_keyboard()

    def _fill_field(self, locator, value):
        self.scroll_to(locator)
        self.write(locator, value)
        self.hide_keyboard()

    def go_to_payment(self):
        self.scroll_to(CheckoutLocators.TO_PAYMENT)
        self.click(CheckoutLocators.TO_PAYMENT)

    def is_payment_screen_visible(self):
        return self.is_visible(CheckoutLocators.PAYMENT_SCREEN)

    def is_address_screen_visible(self):
        return self.is_visible(CheckoutLocators.CHECKOUT_ADDRESS_SCREEN)
