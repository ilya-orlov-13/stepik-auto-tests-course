import pytest

from pages.product_page import ProductPage


@pytest.mark.parametrize("link", [
    pytest.param(
        f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}",
        marks=pytest.mark.xfail(
            reason="offer7 adds 'book' to the product name in the success message",
            raises=AssertionError,
            strict=True,
        ),
    ) if offer == 7 else
    f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
    for offer in range(10)
])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_added_to_basket(product_name)
    page.should_be_basket_total_equal_product_price(product_price)
