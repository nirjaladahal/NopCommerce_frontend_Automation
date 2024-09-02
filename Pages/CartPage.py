from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Utilities.Logger import Logger

class CartPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger().get_logger()

    # Locators
    cart_items = (By.CLASS_NAME, "cart-item-row")
    remove_button = (By.XPATH, "//button[@class='remove-btn']")

    # Actions
    def remove_item_from_cart(self):
        self.logger.info('Removing item from cart')
        self.click_element(self.remove_button)
