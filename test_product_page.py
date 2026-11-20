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


@pytest.mark.xfail(
    reason="Adding a product displays a success message",
    raises=AssertionError,
    strict=True,
)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(
    reason="Success message does not disappear within 4 seconds",
    raises=AssertionError,
    strict=True,
)
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_disappear_success_message()
