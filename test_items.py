from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_add_to_cart_button_is_present(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

    add_to_cart_btn = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket"))
     )

    assert add_to_cart_btn is not None, "The button is missing"
    