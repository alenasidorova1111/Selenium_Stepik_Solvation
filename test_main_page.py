import pytest
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser, page.browser.current_url)
        page.should_be_login_page()


def test_guest_can_see_empty_cart_opened_from_main_page(browser):
    link = MainPage.MAIN_PAGE
    page = MainPage(browser, link)
    page.open()
    page.open_cart()
    page = CartPage(browser, page.browser.current_url)
    page.should_be_empty_cart()
