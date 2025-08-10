import pytest
import allure
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from data.data import BASE_URL, LOGIN_URL, EMAIL, PASSWORD
from pages.main_page import MainPage
from pages.account_page import AccountPage
from pages.order_feed_page import OrderFeedPage
from locators.order_feed_page_locators import OrderFeedPageLocators

@allure.feature('Лента заказов')
@allure.story('Создание нового заказа обновляет счётчики')
@allure.title('Проверка обновления счётчика «Выполнено за всё время»')
@pytest.mark.ui
def test_order_feed_updates_and_shows_new_order(driver):

    with allure.step('Шаг 1: Вход в аккаунт'):
        account_page = AccountPage(driver)
        account_page.login(EMAIL, PASSWORD)
        main_page = MainPage(driver)

        assert main_page.is_constructor_visible(), 'Не удалось войти в аккаунт или загрузить конструктор'


    with allure.step('Шаг 2: Сохранение начального значения счётчика «Выполнено за всё время»'):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_feed()
        initial_total = order_feed_page.get_total_orders()


    with allure.step('Шаг 3: Сборка и оформление заказа'):
        order_feed_page.click_constructor()
        main_page.put_ingredient_into_basket()
        main_page.click_place_order()

        try:
            success_msg = main_page.get_order_success_message()
            assert 'Ваш заказ начали готовить' in success_msg, 'Отсутствует сообщение о начале приготовления заказа'
        except TimeoutException:
            pytest.fail('Не появилось сообщение об успешном создании заказа')


    with allure.step('Шаг 4: Получение номера заказа и закрытие модального окна'):
        order_id = order_feed_page.get_order_id_from_modal()
        assert order_id.isdigit(), 'Номер заказа не получен или некорректен'
        order_feed_page.close_order_details()


    with allure.step('Шаг 5: Проверка увеличения счётчика «Выполнено за всё время»'):
        order_feed_page.click_feed()
        new_total = order_feed_page.get_total_orders()
        assert new_total == initial_total + 1, (
            f"Счётчик 'Выполнено за всё время' не увеличился: было {initial_total}, стало {new_total}"
        )



@allure.feature('Лента заказов')
@allure.story('Создание нового заказа обновляет счётчик "Выполнено за сегодня"')
@allure.title('Проверка увеличения счётчика «Выполнено за сегодня»')
@pytest.mark.ui
def test_today_completed_counter_increments_and_order_in_progress(driver):



    with allure.step('Шаг 1 — войти в аккаунт'):
        account_page = AccountPage(driver)
        account_page.login(EMAIL, PASSWORD)
        main_page = MainPage(driver)
        assert main_page.is_constructor_visible(), "Конструктор не виден — вход мог не выполниться"


    with allure.step('Шаг 2 — открыть ленту заказов и сохранить начальное значение "Выполнено за сегодня"'):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_feed()
        initial_today = order_feed_page.get_today_completed()


    with allure.step('Шаг 3 — собрать и оформить заказ'):
        order_feed_page.click_constructor()

        main_page.put_ingredient_into_basket()
        main_page.click_place_order()


        try:
            success_msg = main_page.get_order_success_message(timeout=15)
            assert 'Ваш заказ начали готовить' in success_msg, "Сообщение о начале приготовления отсутствует"
        except TimeoutException:
            pytest.fail('Не появилось сообщение об успешном создании заказа')


    with allure.step('Шаг 4 — получить ID заказа из модального окна'):
        try:
            order_id = order_feed_page.get_order_id_from_modal()
        except Exception as e:
            pytest.fail(f'Не удалось получить ID заказа: {e}')

        assert order_id and order_id.strip().isdigit(), f'Некорректный ID заказа: "{order_id}"'
        order_feed_page.close_order_details()


    with allure.step('Шаг 5 — проверить увеличение счётчика "Выполнено за сегодня"'):
        order_feed_page.open_feed()

        order_feed_page.find_and_wait_until_text_changes(OrderFeedPageLocators.TODAY_COMPLETED_COUNTER, str(initial_today), timeout=30)
        new_today = order_feed_page.get_today_completed()
        assert new_today == initial_today + 1, (
            f'Счётчик "Выполнено за сегодня" не увеличился: было {initial_today}, стало {new_today}'
        )


@allure.feature("Лента заказов")
@allure.story("После оформления заказа его номер появляется в разделе 'В работе'")
def test_order_appears_in_in_progress(main_page, order_feed_page, account_page, driver):


    with allure.step("1. Авторизация пользователя"):
        account_page.login(EMAIL, PASSWORD)
        driver.get(BASE_URL)
        main_page.main_page_loading_wait()

    with allure.step("2. Добавить булку в конструктор (drag & drop)"):
        main_page.put_ingredient_into_basket()

    with allure.step("3. Оформить заказ"):
        main_page.click_place_order()

    with allure.step("4. Получить номер заказа из модального окна"):
        order_id_text = order_feed_page.get_order_id_from_modal()
        # Извлекаем только цифры из строки (если есть)
        order_id_digits = ''.join(ch for ch in order_id_text if ch.isdigit())
        assert order_id_digits, f"Не удалось извлечь цифры из текста: '{order_id_text}'"
        order_id = order_id_digits
        allure.attach(order_id, name="order_id", attachment_type=allure.attachment_type.TEXT)

    with allure.step("5. Закрыть модальное окно и открыть ленту заказов"):
        order_feed_page.close_order_details()
        order_feed_page.open_feed()

    with allure.step("6. Проверить, что заказ появился в разделе 'В работе' ленты"):
        assert order_feed_page.is_order_in_feed(order_id), f"Заказ {order_id} не найден в ленте 'В работе' после оформления"






























