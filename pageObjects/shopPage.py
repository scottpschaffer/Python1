from selenium.webdriver.common.by import By
from pageObjects.checkout_confirm import Checkout_Confirmation
from utils.browserUtils import BrowserUtils

class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        self.product_name_locator = "div/h4/a"
        self.add_to_cart_button_locator = "div/button"
        self.cart_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def add_product_to_cart(self, product_name):
        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.product_cards)
        
        for product in products:
            current_product_name = product.find_element(By.XPATH, self.product_name_locator).text
            if current_product_name == product_name:
                product.find_element(By.XPATH, self.add_to_cart_button_locator).click()
                break

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
        checkoutPage = Checkout_Confirmation(self.driver)
        return checkoutPage