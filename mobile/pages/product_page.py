from selenium.webdriver.support import expected_conditions as EC

from mobile.locators.product_locators import ProductLocators
from mobile.pages.base_page import BasePage


class ProductPage(BasePage):

    def add_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(ProductLocators.ADD_TO_CART)
        )
        self.click(ProductLocators.ADD_TO_CART)

    def is_add_to_cart_visible(self):
        return self.is_visible(ProductLocators.ADD_TO_CART)

    def is_product_detail_visible(self):
        return self.is_visible(ProductLocators.PRODUCT_SCREEN)
