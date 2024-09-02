from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Utilities.Logger import Logger


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger().get_logger()

    # Locators
    email = (By.ID, "Email")
    password = (By.ID, "Password")
    login_button = (By.XPATH, "//button[@type='submit']")

    # Actions
    def enter_email(self, email_text):
        self.logger.info(f'Entering email: {email_text}')
        self.enter_text_into_element(self.email, email_text)

    def enter_password(self, password_text):
        self.logger.info(f'Entering password')
        self.enter_text_into_element(self.password, password_text)

    def click_login_button(self):
        self.logger.info('Clicking login button')
        self.click_element(self.login_button)
