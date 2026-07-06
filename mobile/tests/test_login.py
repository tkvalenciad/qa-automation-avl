from config.settings import (
    INVALID_PASSWORD,
    INVALID_USERNAME,
    VALID_PASSWORD,
    VALID_USERNAME,
)
from mobile.pages.home_page import HomePage
from mobile.pages.login_page import LoginPage
from mobile.pages.menu_page import MenuPage


def test_login_with_valid_credentials(driver):
    menu = MenuPage(driver)
    login = LoginPage(driver)
    home = HomePage(driver)

    menu.go_to_login()
    login.login_and_return_home(VALID_USERNAME, VALID_PASSWORD)

    assert home.is_products_visible()


def test_login_with_invalid_credentials(driver):
    menu = MenuPage(driver)
    login = LoginPage(driver)

    menu.go_to_login()
    login.login(INVALID_USERNAME, INVALID_PASSWORD)

    assert login.is_error_visible()
    assert "credentials" in login.get_error_message().lower()
