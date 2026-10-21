import json

import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.login import LoginPage
from pageObjects.shopPage import ShopPage

test_data_path = 'data/testData.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list =test_data["data"]


@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    
    driver = browserInstance
    driver.get("https://www.rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    loginPage = LoginPage(driver)
    print("*****" + loginPage.getTitle() + "*****")
    
    shopPage = loginPage.login(test_list_item["userEmail"], test_list_item["userPassword"])
    shopPage.add_product_to_cart(test_list_item["productName"])
    print("*****" + shopPage.getTitle() + "*****")
    checkoutPage = shopPage.go_to_cart()
    checkoutPage.checkout()
    print("*****" + checkoutPage.getTitle() + "*****")
    checkoutPage.enter_delivery_address("Ind")
    checkoutPage.validate_order()
    
    
    time.sleep(10)

    #driver.find_element(By.XPATH, "//a[contains(@href, 'shop')]").click()