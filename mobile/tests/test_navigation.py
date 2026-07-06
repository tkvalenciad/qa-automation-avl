from mobile.pages.home_page import HomePage
from mobile.pages.product_page import ProductPage
from mobile.pages.cart_page import CartPage


def test_navigate_home_product_and_cart(driver):
    home = HomePage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    assert home.is_products_visible()

    home.open_product()
    assert product.is_product_detail_visible()
    assert product.is_add_to_cart_visible()

    product.add_to_cart()
    assert cart.get_cart_badge() == "1"

    home.open_cart()
    assert cart.is_cart_screen_visible()
    assert cart.get_product_name() == "Sauce Labs Backpack"
