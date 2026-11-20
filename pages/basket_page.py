from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), (
            "Empty basket message is not presented"
        )
        message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "Your basket is empty." in message, (
            f"Expected empty basket message, got {message!r}"
        )

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), (
            "Basket contains products, but should be empty"
        )
