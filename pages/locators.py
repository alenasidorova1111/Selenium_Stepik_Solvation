from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    INVALID_LOGIN_LINK = (By.CSS_SELECTOR, "#login_link_inc")
    OPEN_CART_BUTTON = (By.CSS_SELECTOR, "a[class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_REPEAT_PASS = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_FORM_REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    PROD_DESCRIPTION = (By.CSS_SELECTOR, "#product_description")
    PROD_REVIEWS = (By.CSS_SELECTOR, "#reviews")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner > strong")
    MESSAGE_CART_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class CartPageLocators:
    CART_MAIN_TITLE = (By.TAG_NAME, "h1")
    CART_EMPTY_TITLE = (By.CSS_SELECTOR, "div[id='content_inner'] p")
