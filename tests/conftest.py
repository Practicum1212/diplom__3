
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
        """
        Простая фабрика для WebDriver.
        При необходимости добавь опции (headless, путь к бинарю и т.д.)
        """
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


# NOTE: fixtures main_page, order_feed_page, account_page were removed by request.
# Тесты должны сами создавать объекты страниц: MainPage(driver), OrderFeedPage(driver), AccountPage(driver)

@pytest.fixture
def logged_in_account(driver):
    """
    Если нужен залогиненный пользователь — фикстура делает логин.
    Она сама создаёт AccountPage, чтобы не зависеть от удалённых фикстур.
    """
    account_page = AccountPage(driver)
    account_page.open_login_page()
    account_page.login(EMAIL, PASSWORD)
    yield account_page
    # попытка безопасного логаута в teardown (если реализован)
    try:
        account_page.logout()
    except Exception:
        pass

