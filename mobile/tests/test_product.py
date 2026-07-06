from mobile.pages.home_page import HomePage
from mobile.pages.product_page import ProductPage


def test_product_detail_is_displayed(driver):
    home = HomePage(driver)
    product = ProductPage(driver)

    home.open_product()

    assert product.is_product_detail_visible()
    assert product.is_add_to_cart_visible()
