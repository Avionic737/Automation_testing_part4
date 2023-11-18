from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def get_book_info(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_name, product_price

    # def should_be_product_page_url(self, link):
        #     url = self.browser.current_url
    #     assert link == url, f"Expected {link}, but got '{url}'"

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_added_to_basket_message(self, product_name):
        added_to_basket_message = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE).text
        assert product_name == added_to_basket_message, f"Product name '{product_name}' " \
                                                        f"does not match added to basket message " \
                                                        f"'{added_to_basket_message}'"
        print(product_name)
        print(added_to_basket_message)

    def should_be_basket_total_price(self, product_price):
        basket_total_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        assert product_price == basket_total_message, f"Product price '{product_price}' " \
                                                      f"not found in basket total message '{basket_total_message}'"
        print(product_price)
        print(basket_total_message)
