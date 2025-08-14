
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from data.urls import BASE_URL
from data.data import EMAIL, PASSWORD

from pages.account_page import AccountPage


class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser_name: str):

        if browser_name == "firefox":
            return webdriver.Firefox(service=FirefoxService())
        elif browser_name == "chrome":
            return webdriver.Chrome(service=ChromeService())
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выбор браузера: 'chrome' или 'firefox'"
    )


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = WebdriverFactory.get_webdriver(browser_name)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL




@pytest.fixture
def logged_in_account(driver):

    account_page = AccountPage(driver)
    account_page.open_login_page()
    account_page.login(EMAIL, PASSWORD)
    yield account_page

    try:
        account_page.logout()
    except Exception:
        pass

