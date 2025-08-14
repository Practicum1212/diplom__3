

import allure
from .base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from data.urls import FEED_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import re


class OrderFeedPage(BasePage):
    @allure.step('Открыть страницу ленты заказов')
    def open_feed(self):
        # use FEED_URL from data.urls
        self.navigate_to(FEED_URL)
        self.find_element_with_wait(OrderFeedPageLocators.FEED_TITLE)

    @allure.step('Нажать на последний заказ')
    def click_last_order(self):
        self.click_element(OrderFeedPageLocators.LAST_ORDER)

    @allure.step('Получить содержимое деталей заказа')
    def get_order_details(self):
        return self.get_text(OrderFeedPageLocators.ORDER_DETAILS_CONTENT)

    @allure.step('Получить общее количество заказов')
    def get_total_orders(self):
        raw = self.get_text(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER)
        digits = re.sub(r'\D', '', raw)
        return int(digits) if digits else 0

    @allure.step('Получить количество выполненных сегодня заказов')
    def get_today_completed(self):
        raw = self.find_element_with_wait(OrderFeedPageLocators.TODAY_COMPLETED_COUNTER, timeout=10).text.strip()
        digits = re.sub(r'\D', '', raw)
        return int(digits) if digits else 0

    @allure.step('Подождать, пока счётчик "Выполнено за сегодня" изменится')
    def wait_until_today_completed_changes(self, old_text, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(*OrderFeedPageLocators.TODAY_COMPLETED_COUNTER).text != old_text
        )

    @allure.step('Получить ID заказа из модального окна')
    def get_order_id_from_modal(self):

        if self.is_visible(OrderFeedPageLocators.ORDER_ID_TEXT, timeout=20):
            text = self.get_text(OrderFeedPageLocators.ORDER_ID_TEXT, timeout=20)
            assert text and text.strip(), "ORDER_ID_TEXT найден, но текст пустой"
            return text


        if self.is_visible(OrderFeedPageLocators.ORDER_ID, timeout=20):
            text = self.get_text(OrderFeedPageLocators.ORDER_ID, timeout=20)
            assert text and text.strip(), "ORDER_ID найден, но текст пустой"
            return text


        assert False, "Не удалось получить ID заказа из модального окна (locators: ORDER_ID_TEXT/ORDER_ID)"

    @allure.step('Закрыть окно деталей заказа')
    def close_order_details(self):
        self.click_element(OrderFeedPageLocators.CLOSE_ORDER_DETAILS_BUTTON)

    @allure.step('Проверить, что заказ отображается в ленте')
    def is_order_in_feed(self, order_id: str) -> bool:

        template = OrderFeedPageLocators.ORDER_ID_IN_FEED[1]  # строка xpath с '{0}'
        xpath = template.format(order_id)
        locator = (By.XPATH, xpath)
        return self.is_visible(locator, timeout=10)



