from mobile.pages.base_page import BasePage
from mobile.locators.cart_locators import CartLocators


class CartPage(BasePage):

    def get_cart_badge(self):
        return self.get_text(CartLocators.CART_BADGE_COUNT)

    def get_product_name(self):
        return self.get_text(CartLocators.PRODUCT_NAME)

    def is_cart_screen_visible(self):
        return self.is_visible(CartLocators.CART_SCREEN)

    def proceed_to_checkout(self):
        self.click(CartLocators.PROCEED_TO_CHECKOUT)
