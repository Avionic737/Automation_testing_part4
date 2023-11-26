from .base_page import BasePage
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    # Метод для проверки, что корзина пуста
    def should_be_empty_basket(self):
        self.should_be_empty_basket_message()
        self.should_not_be_items_in_basket()

    # Метод для проверки, что есть текст о том, что корзина пуста
    def should_be_empty_basket_message(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#content_inner p"), "Empty basket message is not present"

    # Метод для проверки, что в корзине нет товаров
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(By.CSS_SELECTOR, ".basket-items"), \
            "Basket items are present, but should not be"
