from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn-default")
    BASKET_LINK_INVALID = (By.CSS_SELECTOR, "div.basket-mini a.btn-default_inv")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form.well")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form.well")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email.form-control")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1.form-control")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2.form-control")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"][value="Register"]')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")
