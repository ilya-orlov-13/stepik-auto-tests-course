import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    
    add_to_basket_btn = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(add_to_basket_btn) > 0, "Add to basket button is not found on the page"