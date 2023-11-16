from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_added_to_basket_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_to_basket_message = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE).text
        assert product_name == added_to_basket_message, f"Product name '{product_name}' does not match added to basket message '{added_to_basket_message}'"

    def should_be_basket_total_price(self):
        basket_total_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        assert basket_total_message, "Basket total price message is not present"
