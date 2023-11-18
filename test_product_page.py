import pytest
from Automation_testing_part4.pages.product_page import ProductPage


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
# pytest -s test_product_page.py
