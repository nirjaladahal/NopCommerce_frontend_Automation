import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class CaptchaHandler:
    def __init__(self, driver):
        self.driver = driver
        self.cookie_file = "cookies.pkl"

    def save_cookies(self):
        """ Save cookies to a file """
        pickle.dump(self.driver.get_cookies(), open(self.cookie_file, "wb"))

    def load_cookies(self):
        """ Load cookies from a file """
        self.driver.get("https://demo.nopcommerce.com/")  # Open the site first
        cookies = pickle.load(open(self.cookie_file, "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def handle_captcha(self):
        """ Handle CAPTCHA manually and save cookies """
        self.driver.get("https://demo.nopcommerce.com/")
        input("Complete CAPTCHA manually and press Enter...")
        self.save_cookies()
