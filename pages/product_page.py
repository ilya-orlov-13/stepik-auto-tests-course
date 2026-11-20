from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_product_added_to_basket(self, expected_name):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME), "Product added message is not presented"
        actual_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert actual_name == expected_name, (
            f"Added product name differs: expected {expected_name!r}, got {actual_name!r}"
        )

    def should_be_basket_total_equal_product_price(self, expected_price):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), "Basket total message is not presented"
        actual_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert actual_total == expected_price, (
            f"Basket total differs from product price: expected {expected_price!r}, got {actual_total!r}"
        )

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), (
            "Success message is presented, but should not be"
        )

    def should_disappear_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), (
            "Success message did not appear before checking its disappearance"
        )
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), (
            "Success message did not disappear"
        )
