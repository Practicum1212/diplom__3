import pytest
from selenium import webdriver
from data.data import BASE_URL
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.account_page import AccountPage


class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser_name):
        if browser_name == "firefox":
            return webdriver.Firefox()
        elif browser_name == "chrome":
            return webdriver.Chrome()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")


# Добавление CLI-параметра --browser
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выбор браузера: 'chrome' или 'firefox'"
    )


# Фикстура браузера
@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = WebdriverFactory.get_webdriver(browser_name)
    driver.maximize_window()
    yield driver
    driver.quit()


# Автоматическое открытие главной страницы
@pytest.fixture(autouse=True)
def open_main_page(driver):
    driver.get(BASE_URL)


# Автоматическое открытие ленты заказов
@pytest.fixture(autouse=True)
def open_feed_page(driver):
    driver.get(f"{BASE_URL}/feed")


# Инициализация MainPage
@pytest.fixture
def main_page(driver):
    return MainPage(driver)


# Инициализация OrderFeedPage
@pytest.fixture
def order_feed_page(driver):
    return OrderFeedPage(driver)


# Инициализация AccountPage
@pytest.fixture
def account_page(driver):
    return AccountPage(driver)