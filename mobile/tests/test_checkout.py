from mobile.pages.cart_page import CartPage
from mobile.pages.checkout_page import CheckoutPage
from mobile.pages.home_page import HomePage
from mobile.pages.login_page import LoginPage
from mobile.pages.menu_page import MenuPage
from mobile.pages.product_page import ProductPage
from mobile.payloads.checkout_payload import SHIPPING_ADDRESS_PAYLOAD
from config.settings import VALID_PASSWORD, VALID_USERNAME


def test_checkout_reaches_payment_screen(driver):
    menu = MenuPage(driver)
    login = LoginPage(driver)
    home = HomePage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    menu.go_to_login()
    login.login_and_return_home(VALID_USERNAME, VALID_PASSWORD)

    home.open_product()
    product.add_to_cart()
    assert cart.get_cart_badge() == "1"

    home.open_cart()
    assert cart.get_product_name() == "Sauce Labs Backpack"

    cart.proceed_to_checkout()
    assert checkout.is_address_screen_visible()

    checkout.fill_shipping_address(**SHIPPING_ADDRESS_PAYLOAD)
    checkout.go_to_payment()

    assert checkout.is_payment_screen_visible()
