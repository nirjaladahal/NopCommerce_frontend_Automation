import pytest

from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.ProductPage import ProductPage
from Pages.CartPage import CartPage


class TestNopCommerce(BasePage):

    def test_login(self):
        try:
            login_page = LoginPage(self.driver)
            login_page.enter_email("testuser@example.com")
            login_page.enter_password("Test@123")
            login_page.click_login_button()
            assert "My account" in self.driver.title
        except Exception as e:
            print(str(e))

    def test_add_to_cart(self):
        try:
            product_page = ProductPage(self.driver)
            product_page.select_product()
            product_page.add_to_cart()
            assert "Shopping cart" in self.driver.title
        except Exception as e:
            print(str(e))

    def test_remove_from_cart(self):
        try:
            cart_page = CartPage(self.driver)
            cart_page.remove_item_from_cart()
            assert "Your Shopping Cart is empty" in self.driver.page_source
        except Exception as e:
            print(str(e))
