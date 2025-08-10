import allure

from data.data import FEED_URL
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators

class OrderFeedPage(BasePage):
    @allure.step('Открыть страницу ленты заказов')
    def open_feed(self):
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
        return int(self.get_text(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER))

    @allure.step('Получить количество выполненных сегодня заказов')
    def get_today_completed(self):
        return int(self.find_element_with_wait(OrderFeedPageLocators.TODAY_COMPLETED_COUNTER, timeout=10).text.strip())

    @allure.step('Переключиться в конструктор')
    def click_constructor(self):
        self.click_element(OrderFeedPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Переключиться на ленту заказов')
    def click_feed(self):
        self.click_element(OrderFeedPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Нажать кнопку "Личный кабинет"')
    def click_account(self):
        self.click_element(OrderFeedPageLocators.ACCOUNT_BUTTON)

    @allure.step('Нажать кнопку закрытия деталей заказа')
    def close_order_details(self):
        self.click_element(OrderFeedPageLocators.CLOSE_ORDER_DETAILS_BUTTON)

    @allure.step('Получить ID заказа из модального окна')
    def get_order_id_from_modal(self):
        self.find_and_wait_until_text_changes(OrderFeedPageLocators.ORDER_ID, '9999')
        return self.get_text(OrderFeedPageLocators.ORDER_ID)

    @allure.step('Проверить, что заказ отображается в ленте')
    def is_order_in_feed(self, order_id):
        formatted = f'{int(order_id):07d}'
        locator = (OrderFeedPageLocators.ORDER_ID_IN_FEED[0], OrderFeedPageLocators.ORDER_ID_IN_FEED[1].format(formatted))
        return self.is_visible(locator)

    @allure.step('Проверить, что заказ в обработке')
    def is_order_in_progress(self, order_id):
        formatted = f'{int(order_id):07d}'
        self.find_and_wait_until_text_changes(OrderFeedPageLocators.ORDER_IN_PROGRESS_LOCATOR, formatted)
        return True

