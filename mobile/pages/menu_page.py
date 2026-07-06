from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from mobile.locators.home_locators import HomeLocators
from mobile.locators.login_locators import LoginLocators
from mobile.locators.menu_locators import MenuLocators
from mobile.pages.base_page import BasePage
from mobile.utils.app_helpers import wait_for_catalog


class MenuPage(BasePage):

    def open_menu(self):
        if self.is_present(MenuLocators.CATALOG_MENU_ITEM):
            return

        self.click(MenuLocators.MENU)
        self.wait.until(
            EC.presence_of_element_located(MenuLocators.CATALOG_MENU_ITEM)
        )

    def close_menu_to_catalog(self):
        self.click(MenuLocators.CATALOG_MENU_ITEM)
        wait_for_catalog(self.driver)

    def _dismiss_dialog_if_present(self):
        try:
            ok_button = self.wait.until(
                EC.element_to_be_clickable(MenuLocators.DIALOG_OK_BUTTON)
            )
            ok_button.click()
        except TimeoutException:
            pass

    def _perform_logout(self):
        self.click(MenuLocators.LOGOUT_MENU_ITEM)
        self.click(MenuLocators.LOGOUT_CONFIRM_BUTTON)
        self._dismiss_dialog_if_present()
        self.wait.until(
            EC.any_of(
                EC.presence_of_element_located(LoginLocators.LOGIN_SCREEN),
                EC.presence_of_element_located(HomeLocators.PRODUCTS_SCREEN),
            )
        )

    def go_to_login(self):
        if self.is_present(LoginLocators.LOGIN_SCREEN):
            return

        self.open_menu()

        if self.is_present(MenuLocators.LOGOUT_MENU_ITEM):
            self._perform_logout()
            if self.is_present(LoginLocators.LOGIN_SCREEN):
                return
            self.open_menu()

        self.driver.find_element(*MenuLocators.LOGIN_IN_VIEW).click()
        self.wait_for_visible(LoginLocators.LOGIN_SCREEN)
