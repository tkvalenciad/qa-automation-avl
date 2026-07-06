from mobile.pages.home_page import HomePage
from mobile.pages.product_page import ProductPage
from mobile.pages.cart_page import CartPage


def test_add_product_to_cart(driver):
    home = HomePage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    home.open_product()
    product.add_to_cart()

    assert cart.get_cart_badge() == "1"

    home.open_cart()
    assert cart.get_product_name() == "Sauce Labs Backpack"
