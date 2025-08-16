

from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Найти элемент с ожиданием отображения: {locator}')
    def find_element_with_wait(self, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="element_not_found",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Элемент {locator} не появился за {timeout} секунд")

    @allure.step('Клик по элементу: {locator}')
    def click_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            ActionChains(self.driver).move_to_element(element).click().perform()
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="click_failed",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Элемент {locator} не кликабелен за {timeout} секунд")

    @allure.step('Ввести текст "{text}" в элемент: {locator}')
    def enter_text(self, locator, text, timeout=10):
        element = self.find_element_with_wait(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step('Получить текст из элемента: {locator}')
    def get_text(self, locator, timeout=5):
        return self.find_element_with_wait(locator, timeout).text

    @allure.step('Проверить, что элемент видим: {locator}')
    def is_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step('Перейти по адресу: {url}')
    def navigate_to(self, url):
        self.driver.get(url)

    @allure.step('Перетащить элемент из {source} в {target}')
    def drag_and_drop_element(self, source, target):
        try:
            drag_and_drop(self.driver, source, target)
        except Exception as e:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="drag_and_drop_failed",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Не удалось перетащить элемент: {e}")

    @allure.step('Ожидать изменения текста у элемента: {locator}')
    def find_and_wait_until_text_changes(self, locator, initial_text, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda drv: self.find_element_with_wait(locator).text != initial_text
            )
            return self.find_element_with_wait(locator)
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="text_did_not_change",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Текст элемента {locator} не изменился за {timeout} секунд")

    @allure.step("Ожидание исчезновения всех модальных оверлеев")
    def wait_for_all_overlays_to_disappear(self, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"))
        )


    @allure.step('Ожидание выполнения условия (timeout={timeout}s)')
    def wait_until(self, condition_fn, timeout=30, poll_frequency=1, message: str | None = None):

        try:
            return WebDriverWait(self.driver, timeout, poll_frequency).until(
                lambda drv: condition_fn(drv)
            )
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="wait_until_timeout",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(message or f"Условие не выполнилось за {timeout} секунд")







