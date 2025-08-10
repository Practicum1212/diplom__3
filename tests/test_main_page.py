import pytest
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

pytestmark = pytest.mark.usefixtures("open_main_page")

@allure.title("Переход по клику на 'Конструктор'")
def test_click_constructor_navigates_to_constructor(driver):
    with allure.step('Кликаем по кнопке "Конструктор"'):
        main_page = MainPage(driver)
        main_page.click_constructor()
    with allure.step('Проверяем, что секция конструктора отображается'):
        assert main_page.is_constructor_visible(), "Секция конструктора не видна после клика"

@allure.title("Переход по клику на раздел 'Лента заказов'")
def test_click_feed_navigates_to_feed(driver):
    with allure.step('Кликаем по кнопке "Лента заказов"'):
        main_page = MainPage(driver)
        main_page.click_order_feed()
    with allure.step('Проверяем отображение ленты заказов'):
        assert main_page.is_visible(MainPageLocators.COMPLETED_ORDERS), \
            "Лента заказов не отображена после клика"

@allure.title("Открытие модального окна с деталями ингредиента")
def test_open_ingredient_modal(driver):
    main_page = MainPage(driver)
    with allure.step('Ожидание загрузки главной страницы'):
        main_page.main_page_loading_wait()
    with allure.step('Кликаем по ингредиенту R2-D3'):
        main_page.click_r2d3_bun()
    with allure.step('Проверяем открытие модального окна'):
        assert main_page.is_visible(MainPageLocators.INGREDIENT_DETAILS_TITLE), \
            "Модальное окно деталей ингредиента не открылось"

@allure.title("Закрытие модального окна с деталями ингредиента")
def test_close_ingredient_modal(driver):
    main_page = MainPage(driver)
    with allure.step('Ожидание загрузки главной страницы'):
        main_page.main_page_loading_wait()
    with allure.step('Открываем модальное окно с деталями ингредиента'):
        main_page.click_r2d3_bun()
    with allure.step('Закрываем модальное окно по крестику'):
        main_page.click_element(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)
    with allure.step('Ожидаем исчезновения модального окна'):
        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_DETAILS_TITLE)
        )
    with allure.step('Проверяем закрытие модального окна'):
        assert not main_page.is_visible(MainPageLocators.INGREDIENT_DETAILS_TITLE), \
            "Модальное окно деталей ингредиента не закрылось"

@allure.title("Увеличение счётчика ингредиента при добавлении")
def test_adding_ingredient_increments_counter(driver):
    main_page = MainPage(driver)
    with allure.step('Ожидание загрузки главной страницы'):
        main_page.main_page_loading_wait()
    with allure.step('Считываем текущее значение счётчика ингредиента'):
        initial_text = main_page.find_element_with_wait(MainPageLocators.INGREDIENT_COUNTER).text
        initial_count = int(initial_text)
    with allure.step('Перетаскиваем ингредиент в корзину'):
        main_page.put_ingredient_into_basket()
    with allure.step('Ожидаем изменения счётчика ингредиента'):
        main_page.find_and_wait_until_text_changes(MainPageLocators.INGREDIENT_COUNTER, initial_text, timeout=5)
    with allure.step('Считываем обновлённое значение счётчика'):
        updated_count = int(main_page.find_element_with_wait(MainPageLocators.INGREDIENT_COUNTER).text)
    with allure.step('Проверяем, что счётчик увеличился на 1'):
                assert updated_count > initial_count, \
            f"Ожидалось значение больше {initial_count}, но получили {updated_count}"



