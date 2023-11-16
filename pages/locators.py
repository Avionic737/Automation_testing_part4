from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form.well")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form.well")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")
