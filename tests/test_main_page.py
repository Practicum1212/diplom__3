import pytest
import allure
from selenium.common.exceptions import TimeoutException

from data.urls import BASE_URL
from pages.main_page import MainPage


class TestMainPage:
    @allure.title("Переход по клику на 'Конструктор'")
    @pytest.mark.ui
    def test_click_constructor_navigates_to_constructor(self, driver):
        main_page = MainPage(driver)
        driver.get(BASE_URL)

        with allure.step('Кликаем по "Конструктор"'):
            main_page.click_constructor()
        with allure.step('Проверяем, что секция конструктора отображается'):
            assert main_page.is_constructor_visible(), "Секция конструктора не видна после клика"


    @allure.title("Переход по клику на раздел 'Лента заказов'")
    @pytest.mark.ui
    def test_click_feed_navigates_to_feed(self, driver):
        main_page = MainPage(driver)
        driver.get(BASE_URL)

        with allure.step('Кликаем по "Лента заказов"'):
            main_page.click_order_feed()
        with allure.step('Проверяем отображение ленты заказов'):
            assert main_page.is_order_feed_visible(), "Лента заказов не отображена после клика"


    @allure.title("Открытие модального окна с деталями ингредиента")
    @pytest.mark.ui
    def test_open_ingredient_modal(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            driver.get(BASE_URL)

        with allure.step("Ожидаем загрузки главной страницы (конструктор)"):
            main_page.main_page_loading_wait()

        with allure.step("Кликаем по ингредиенту R2-D3"):
            main_page.click_r2d3_bun()

        with allure.step("Проверяем, что модальное окно деталей ингредиента открылось"):
            assert main_page.is_ingredient_modal_visible(), "Модальное окно деталей ингредиента не открылось"


    @allure.title("Закрытие модального окна с деталями ингредиента")
    @pytest.mark.ui
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            driver.get(BASE_URL)

        with allure.step("Ожидаем загрузки главной страницы (конструктор)"):
            main_page.main_page_loading_wait()

        with allure.step("Открываем модальное окно ингредиента (необходимая предпосылка для проверки закрытия)"):
            main_page.click_r2d3_bun()
            assert main_page.is_ingredient_modal_visible(), "Модальное окно не открылось — невозможно проверить закрытие"

        with allure.step("Закрываем модальное окно (клик по кресту)"):
            main_page.close_ingredient_modal()

        with allure.step("Ожидаем скрытия модального окна и проверяем, что оно закрыто"):
            main_page.wait_for_ingredient_modal_to_close(timeout=5)
            assert not main_page.is_ingredient_modal_visible(), "Модальное окно деталей ингредиента не закрылось"


    @allure.title("Увеличение счётчика ингредиента при добавлении")
    @pytest.mark.ui
    def test_adding_ingredient_increments_counter(self, driver):
        main_page = MainPage(driver)
        driver.get(BASE_URL)

        with allure.step('Ждём загрузки и читаем начальный счётчик'):
            main_page.main_page_loading_wait()
            initial_count = main_page.get_ingredient_counter()

        with allure.step('Перетаскиваем ингредиент в корзину'):
            main_page.put_ingredient_into_basket()

        with allure.step('Ожидаем изменения счётчика'):
            main_page.wait_for_ingredient_counter_change(str(initial_count), timeout=10)

        with allure.step('Считываем обновлённый счётчик и проверяем увеличение'):
            updated_count = main_page.get_ingredient_counter()
            assert updated_count > initial_count, f"Ожидалось значение больше {initial_count}, но получили {updated_count}"






