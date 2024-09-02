from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Utilities.Logger import Logger


class ProductPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger().get_logger()

    # Locators
    product_name = (By.XPATH, "//a[contains(text(),'Some Product')]")
    add_to_cart_button = (By.ID, "add-to-cart-button")

    # Actions
    def select_product(self):
        self.logger.info('Selecting product')
        self.click_element(self.product_name)

    def add_to_cart(self):
        self.logger.info('Adding product to cart')
        self.click_element(self.add_to_cart_button)
