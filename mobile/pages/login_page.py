import time

from config.settings import VALID_USERNAME
from mobile.locators.home_locators import HomeLocators
from mobile.locators.login_locators import LoginLocators
from mobile.pages.base_page import BasePage
from mobile.utils.app_helpers import dismiss_system_prompts, wait_for_catalog


class LoginPage(BasePage):

    def login(self, username, password):
        self.wait_for_visible(LoginLocators.LOGIN_SCREEN)

        if username == VALID_USERNAME:
            self.driver.find_element(*LoginLocators.SAMPLE_USER_SCROLL).click()
        else:
            self.write(LoginLocators.USERNAME, username)
            self.hide_keyboard()
            self.write(LoginLocators.PASSWORD, password)
            self.hide_keyboard()

        self.click(LoginLocators.LOGIN_BUTTON)

    def login_and_return_home(self, username, password):
        self.login(username, password)
        self._wait_for_catalog_after_login()

    def _wait_for_catalog_after_login(self):
        deadline = time.monotonic() + 20
        while time.monotonic() < deadline:
            dismiss_system_prompts(self.driver)
            if self.is_present(HomeLocators.PRODUCTS_SCREEN):
                return
            time.sleep(0.5)

        wait_for_catalog(self.driver)

    def get_error_message(self):
        return self.get_text(LoginLocators.ERROR_MESSAGE)

    def is_error_visible(self):
        return self.is_visible(LoginLocators.ERROR_MESSAGE)

    def is_login_screen_visible(self):
        return self.is_present(LoginLocators.LOGIN_SCREEN)
