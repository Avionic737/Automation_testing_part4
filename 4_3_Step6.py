from Automation_testing_part4.pages.locators import ProductPageLocators
from Automation_testing_part4.pages.product_page import ProductPage

link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), \
        "Success message is present, but it should not be"


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), \
        "Success message is present, but it should not be"


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    assert page.is_disappeared(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), \
        "Success message did not disappear, but it should have"
    # pytest -s 4_3_Step6.py
