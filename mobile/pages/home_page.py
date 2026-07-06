from selenium.webdriver.support import expected_conditions as EC

from mobile.locators.home_locators import HomeLocators
from mobile.locators.product_locators import ProductLocators
from mobile.pages.base_page import BasePage


class HomePage(BasePage):

    def open_cart(self):
        self.click(HomeLocators.CART)

    def open_product(self):
        self.click(HomeLocators.BACKPACK)
        self.wait.until(
            EC.presence_of_element_located(ProductLocators.PRODUCT_SCREEN)
        )

    def is_products_visible(self):
        return self.is_present(HomeLocators.PRODUCTS_SCREEN)
