import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_e2e(browserInstance):
    
    driver = browserInstance
    driver.get("https://www.rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    #driver.find_element(By.XPATH, "//a[contains(@href, 'shop')]").click()
    driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
    products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    for product in products:
        product_name = product.find_element(By.XPATH, "div/h4/a").text
        if product_name == "Blackberry":
            product.find_element(By.XPATH, "div/button").click()
            break
    driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
    driver.find_element(By.ID, "country").send_keys("Ind")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
    driver.find_element(By.LINK_TEXT, "India").click()
    #driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    successText = driver.find_element(By.CLASS_NAME, "alert-success").text
    assert successText.__contains__("Success")
    assert "Success! Thank you!" in successText
    time.sleep(5)