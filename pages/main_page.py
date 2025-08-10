import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators



class MainPage(BasePage):
    @allure.step('Ожидание загрузки главной страницы')
    def main_page_loading_wait(self):
        self.find_element_with_wait(MainPageLocators.BURGER_CONSTRUCTOR_SECTION)

    @allure.step('Нажать на кнопку "Конструктор"')
    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Открыть ленту заказов')
    def click_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Нажать на ингредиент R2-D3')
    def click_r2d3_bun(self):
        self.click_element(MainPageLocators.INGREDIENT_R2D3_BUN)

    @allure.step('Нажать кнопку "Собрать заказ"')
    def click_place_order(self):
        self.click_element(MainPageLocators.PLACE_AN_ORDER)

    @allure.step('Перетащить булку R2-D3 в конструктор')
    def put_r2d3_bun_into_constructor(self):
        self.find_element_with_wait(MainPageLocators.BURGER_CONSTRUCTOR_SECTION)
        self.drag_and_drop_element(
            MainPageLocators.INGREDIENT_R2D3_BUN,
            MainPageLocators.ORDER_TARGET_TOP
        )

    @allure.step('Перетащить булочку в корзину')
    def put_ingredient_into_basket(self):
        # Ожидаем загрузки главной страницы
        self.main_page_loading_wait()
        # Находим нужную булочку и область для её сброса
        ingredient = self.find_element_with_wait(MainPageLocators.INGREDIENT_R2D3_BUN)
        basket = self.find_element_with_wait(MainPageLocators.BUN_DROP_AREA_TOP)
        # Перетаскиваем ингредиент в корзину
        self.drag_and_drop_element(source=ingredient, target=basket)

    def get_order_success_message(self, timeout=10):
        return self.get_text(MainPageLocators.ORDER_SUCCESS_MESSAGE, timeout)

    @allure.step('Проверить видимость секции конструктора бургеров')
    def is_constructor_visible(self):
        return self.is_visible(MainPageLocators.BURGER_CONSTRUCTOR_SECTION)



