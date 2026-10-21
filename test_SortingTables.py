import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.smoke
def test_sort(browserInstance):
    driver = browserInstance
    browserSortedVeggies = []

    #service_obj = Service("C:\\Users\\scott\\Python\\chromedriver.exe")
    #driver = webdriver.Chrome(service=service_obj)
    #driver.implicitly_wait(5)
    driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/offers")
    driver.maximize_window()
    
    driver.find_element(By.XPATH, "//tr/th[1]").click()
    veglist = driver.find_elements(By.XPATH, "//tr/td[1]")
    for veg in veglist:
        print(veg.text)
        browserSortedVeggies.append(veg.text)
    originalSortedVeggies = browserSortedVeggies.copy()
    browserSortedVeggies.sort()
    print("Original Sorted Veggies: ", originalSortedVeggies)
    print("Browser Sorted Veggies: ", browserSortedVeggies)
    assert originalSortedVeggies == browserSortedVeggies   

    time.sleep(2)
    driver.quit()
