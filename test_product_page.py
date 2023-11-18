import time

import pytest

from Automation_testing_part4.pages.product_page import ProductPage


# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

# @pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6",
# pytest.param("7", marks=pytest.mark.xfail), "8", "9"])

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# @pytest.mark.parametrize('promo_offer', ["7"])
def test_guest_can_add_product_to_basket(browser, link):
    # link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    product_name, product_price = page.get_book_info()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    # page.should_be_product_page_url(link)
    page.should_be_added_to_basket_message(product_name)
    # time.sleep(100)
    page.should_be_basket_total_price(product_price)



# pytest -s test_product_page.py
