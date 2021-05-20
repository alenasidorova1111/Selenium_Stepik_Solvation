from pages.base_page import BasePage
from pages.locators import CartPageLocators


class CartPage(BasePage):
    def should_be_cart_page(self):
        self.should_be_cart_url()
        self.should_be_cart_title()

    def should_be_cart_url(self):
        assert "basket" in self.url, "Current URL is not a cart page url"

    def should_be_cart_title(self):
        assert self.is_element_present(*CartPageLocators.CART_MAIN_TITLE), "Main cart title is not presented on page"

    def should_be_empty_cart(self):
        assert self.is_element_present(*CartPageLocators.CART_EMPTY_TITLE), "No message about empty cart on page"
