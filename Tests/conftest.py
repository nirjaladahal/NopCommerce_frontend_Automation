import platform
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Utilities.cleanup_utility import cleanup_logs, cleanup_screenshots


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to use for tests")


@pytest.fixture()
def setup(request):
    # Clean up logs and screenshots before starting the test
    cleanup_logs()
    cleanup_screenshots()

    global driver
    current_os = str(platform.system())
    browser = request.config.getoption("--browser").lower()

    # Setup driver with options
    try:
        if browser == 'chrome':
            options = Options()
            options.add_experimental_option("detach", True)  # This keeps the browser window open after the test
            if current_os == 'Windows':
                driver = webdriver.Chrome(options=options)
            elif current_os == "Darwin":
                driver = webdriver.Chrome(options=options)

        elif browser == 'safari' and current_os == "Darwin":
            driver = webdriver.Safari()

        # Maximize window and navigate to the URL
        driver.maximize_window()
        driver.get("https://demo.nopcommerce.com")
        request.cls.driver = driver
        yield driver

    except Exception as e:
        print(str(e))
