import pytest
from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time


@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6",
                                         pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    product_name, product_price = page.get_book_info()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_added_to_basket_message(product_name)
    page.should_be_basket_total_price(product_price)


link2 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()
    basket_page.should_not_be_items_in_basket()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.add_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), \
        "Success message is present, but it should not be"


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link2)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), \
        "Success message is present, but it should not be"


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.add_to_basket()
    assert page.is_disappeared(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), \
        "Success message did not disappear, but it should have"


@pytest.mark.test_user
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = MainPage(browser, link2)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = "testpassword123"
        login_page.register_new_user(email, password)
        print("User should be authorized:", page.is_authorized_user())
        login_page.should_be_authorized_user()
        self.email = email
        self.password = password

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link2)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), \
            "Success message is present, but it should not be"

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link2)
        page.open()
        product_name, product_price = page.get_book_info()
        page.add_to_basket()
        page.should_be_added_to_basket_message(product_name)
        page.should_be_basket_total_price(product_price)

# pytest -s -m test_user test_product_page.py
