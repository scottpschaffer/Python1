from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.browserUtils import BrowserUtils

class Checkout_Confirmation(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.success_alert = (By.CLASS_NAME, "alert-success")
        self.checkout_button = (By.CSS_SELECTOR, "button[class*='btn-success']")
        self.country_input = (By.ID, "country")
        self.india_link = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submit_button = (By.CSS_SELECTOR, "[type='submit']")

    def get_success_text(self):
        return self.driver.find_element(*self.success_alert).text

    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def enter_delivery_address(self, countryName):
        
        self.driver.find_element(*self.country_input).send_keys(countryName)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.india_link))
        self.driver.find_element(*self.india_link).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click()

    def validate_order(self):
        successText = self.driver.find_element(*self.success_alert).text
        assert successText.__contains__("Success")
        assert "Success! Thank you!" in successText


#self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()