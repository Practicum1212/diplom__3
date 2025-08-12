
import time
import pytest
import allure

from data.urls import BASE_URL
from data.data import EMAIL, PASSWORD
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature('Лента заказов')
@allure.story('Создание нового заказа обновляет счётчики')
@allure.title('Проверка обновления счётчика «Выполнено за всё время»')
@pytest.mark.ui
def test_order_feed_updates_and_shows_new_order(driver):
    account_page = AccountPage(driver)
    main_page = MainPage(driver)
    order_feed_page = OrderFeedPage(driver)

    with allure.step("1) Авторизация пользователя"):
        account_page.open_login_page()
        account_page.login(EMAIL, PASSWORD)

    with allure.step("2) Открываем главную страницу и проверяем видимость конструктора"):
        driver.get(BASE_URL)
        assert main_page.is_constructor_visible(), 'Не удалось войти в аккаунт или загрузить конструктор'

    with allure.step("3) Открываем ленту и сохраняем начальное значение полного счётчика"):
        order_feed_page.open_feed()
        initial_total = order_feed_page.get_total_orders()

    with allure.step("4) Собираем и оформляем заказ"):
        main_page.click_constructor()
        main_page.put_ingredient_into_basket()
        main_page.click_place_order()

        success_msg = main_page.get_order_success_message(timeout=15)
        assert 'Ваш заказ начали готовить' in success_msg, 'Отсутствует сообщение о начале приготовления заказа'

    with allure.step("5) Получаем ID заказа из модалки и закрываем её"):
        order_id_text = order_feed_page.get_order_id_from_modal()
        order_id_digits = ''.join(ch for ch in order_id_text if ch.isdigit())
        assert order_id_digits, f"Невозможно извлечь цифры заказа из: '{order_id_text}'"
        order_feed_page.close_order_details()
        allure.attach(order_id_digits, name="order_id", attachment_type=allure.attachment_type.TEXT)

    with allure.step("6) Проверяем, что общий счётчик увеличился на 1"):
        order_feed_page.open_feed()
        new_total = order_feed_page.get_total_orders()
        assert new_total == initial_total + 1, (
            f"Счётчик 'Выполнено за всё время' не увеличился: было {initial_total}, стало {new_total}"
        )


@allure.feature('Лента заказов')
@allure.story('Создание нового заказа обновляет счётчик "Выполнено за сегодня"')
@allure.title('Проверка увеличения счётчика «Выполнено за сегодня»')
@pytest.mark.ui
def test_today_completed_counter_increments_and_order_in_progress(driver):
    account_page = AccountPage(driver)
    main_page = MainPage(driver)
    order_feed_page = OrderFeedPage(driver)

    with allure.step("1) Авторизация пользователя"):
        account_page.open_login_page()
        account_page.login(EMAIL, PASSWORD)

    with allure.step("2) Переход на главную страницу и проверка конструктора"):
        driver.get(BASE_URL)
        assert main_page.is_constructor_visible(), "Конструктор не виден — вход мог не выполниться"

    with allure.step("3) Открываем ленту и сохраняем текущее значение 'Выполнено за сегодня'"):
        order_feed_page.open_feed()
        initial_today = order_feed_page.get_today_completed()

    with allure.step("4) Собираем и оформляем заказ"):
        main_page.click_constructor()
        main_page.put_ingredient_into_basket()
        main_page.click_place_order()

        success_msg = main_page.get_order_success_message(timeout=15)
        assert 'Ваш заказ начали готовить' in success_msg, "Сообщение о начале приготовления отсутствует"

    with allure.step("5) Получаем ID и закрываем модалку"):
        order_id_text = order_feed_page.get_order_id_from_modal()
        order_id_digits = ''.join(ch for ch in order_id_text if ch.isdigit())
        assert order_id_digits, f'Некорректный ID заказа: "{order_id_text}"'
        order_feed_page.close_order_details()
        allure.attach(order_id_digits, name="order_id", attachment_type=allure.attachment_type.TEXT)

    with allure.step("6) Ожидаем обновления счётчика 'Выполнено за сегодня' и проверяем увеличение"):
        timeout_seconds = 30
        poll_interval = 1
        deadline = time.time() + timeout_seconds
        current = None
        while time.time() < deadline:
            order_feed_page.open_feed()
            current = order_feed_page.get_today_completed()
            if current == initial_today + 1:
                break
            time.sleep(poll_interval)

        assert current == initial_today + 1, (
            f'Счётчик "Выполнено за сегодня" не увеличился за {timeout_seconds} секунд (было {initial_today}, стало {current})'
        )


@allure.feature("Лента заказов")
@allure.story("После оформления заказа его номер появляется в разделе 'В работе'")
@allure.title("Проверка появления номера заказа в разделе 'В работе'")
@pytest.mark.ui
def test_order_appears_in_in_progress(driver):
    account_page = AccountPage(driver)
    main_page = MainPage(driver)
    order_feed_page = OrderFeedPage(driver)

    with allure.step("1) Авторизация и переход на главную"):
        account_page.open_login_page()
        account_page.login(EMAIL, PASSWORD)
        driver.get(BASE_URL)
        main_page.main_page_loading_wait()

    with allure.step("2) Добавляем ингредиенты и оформляем заказ"):
        main_page.put_ingredient_into_basket()
        main_page.click_place_order()

    with allure.step("3) Получаем ID из модалки и прикрепляем к отчету"):
        order_id_text = order_feed_page.get_order_id_from_modal()
        order_id_digits = ''.join(ch for ch in order_id_text if ch.isdigit())
        assert order_id_digits, f"Не удалось извлечь цифры из текста: '{order_id_text}'"
        order_id = order_id_digits
        allure.attach(order_id, name="order_id", attachment_type=allure.attachment_type.TEXT)

    with allure.step("4) Закрываем модалку и открываем ленту"):
        order_feed_page.close_order_details()
        order_feed_page.open_feed()

    with allure.step("5) Проверяем, что заказ появился в разделе 'В работе'"):
        assert order_feed_page.is_order_in_feed(order_id), f"Заказ {order_id} не найден в ленте 'В работе' после оформления"





































