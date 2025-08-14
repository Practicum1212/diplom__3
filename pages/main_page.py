
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step('Клик по "Конструктор"')
    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик по "Лента заказов"')
    def click_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Проверить, видим ли конструктор')
    def is_constructor_visible(self):
        return self.is_visible(MainPageLocators.BURGER_CONSTRUCTOR_SECTION)

    @allure.step('Проверить, видна ли секция ленты заказов на странице')
    def is_order_feed_visible(self):
        return self.is_visible(MainPageLocators.COMPLETED_ORDERS)

    @allure.step('Клик по булке R2-D3')
    def click_r2d3_bun(self):
        self.click_element(MainPageLocators.INGREDIENT_R2D3_BUN)

    @allure.step('Ожидание загрузки главной страницы')
    def main_page_loading_wait(self, timeout=10):
        self.find_element_with_wait(MainPageLocators.BURGER_CONSTRUCTOR_SECTION, timeout=timeout)

    @allure.step('Перетащить ингредиент в корзину')
    def put_ingredient_into_basket(self):
        # используем FIRST_INGREDIENT → ORDER_TARGET_TOP (можно изменить на конкретный локатор)
        self.drag_and_drop_element(MainPageLocators.FIRST_INGREDIENT, MainPageLocators.ORDER_TARGET_TOP)

    @allure.step('Нажать кнопку оформления заказа')
    def click_place_order(self):
        self.click_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Получить сообщение об успешном создание заказа')
    def get_order_success_message(self, timeout=15):
        return self.get_text(MainPageLocators.ORDER_SUCCESS_MESSAGE, timeout=timeout)

    @allure.step('Получить значение счётчика ингредиента')
    def get_ingredient_counter(self):
        text = self.find_element_with_wait(MainPageLocators.INGREDIENT_COUNTER).text.strip()
        # защититься, если пустая строка
        return int(text) if text.isdigit() else 0

    @allure.step('Ожидать изменения счётчика ингредиента')
    def wait_for_ingredient_counter_change(self, initial_text, timeout=30):
        self.find_and_wait_until_text_changes(MainPageLocators.INGREDIENT_COUNTER, initial_text, timeout=timeout)

    @allure.step('Проверить видимость модалки ингредиента')
    def is_ingredient_modal_visible(self):
        return self.is_visible(MainPageLocators.INGREDIENT_DETAILS_TITLE)

    @allure.step('Закрыть модальное окно ингредиента (крестик)')
    def close_ingredient_modal(self):
        self.click_element(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    @allure.step('Ожидать закрытия модалки ингредиента')
    def wait_for_ingredient_modal_to_close(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_DETAILS_TITLE)
            )
        except TimeoutException:
            raise AssertionError(f"Модалка ингредиента не скрылась за {timeout} секунд")




