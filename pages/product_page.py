from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_product_description()
        self.should_be_product_reviews()
        self.should_be_add_to_cart_button()

    def should_be_product_url(self):
        assert "/catalogue/" in self.url, "Current URL is not a product page url"

    def should_be_product_description(self):
        assert self.is_element_present(*ProductPageLocators.PROD_DESCRIPTION),\
            "Description of product is not presented"

    def should_be_product_reviews(self):
        assert self.is_element_present(*ProductPageLocators.PROD_REVIEWS),\
            "Reviews on product are not presented"

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON),\
            "Add to basket button is not presented"

    def add_product_to_cart(self):
        self.choose_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def should_appear_valid_add_message(self):
        product_name = self.choose_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.choose_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert product_name == message, "No product name in the message"

    def should_appear_valid_price_in_cart(self):
        cart_total = self.choose_element(*ProductPageLocators.MESSAGE_CART_TOTAL).text
        product_price = self.choose_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert cart_total == product_price, "Cart total price or product price error"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDING),\
            "Success message is presented, but should be disappeared"
