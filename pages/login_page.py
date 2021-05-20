from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "Current URL is not a login_url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password, page):
        email_field = page.choose_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        password_field = page.choose_element(*LoginPageLocators.REGISTER_FORM_PASS)
        password2_field = page.choose_element(*LoginPageLocators.REGISTER_FORM_REPEAT_PASS)

        email_field.send_keys(email)
        password_field.send_keys(password)
        password2_field.send_keys(password)

        register_button = page.choose_element(*LoginPageLocators.REGISTER_FORM_REGISTER_BUTTON)
        register_button.click()
