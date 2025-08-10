import allure
from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from data.data import LOGIN_URL

class AccountPage(BasePage):
    @allure.step('Открыть страницу логина')
    def open_login_page(self):
        self.navigate_to(LOGIN_URL)

    @allure.step('Ввести логин и пароль и нажать "Войти"')
    def login(self, email, password):
        self.open_login_page()
        self.enter_text(AccountPageLocators.EMAIL_INPUT, email)
        self.enter_text(AccountPageLocators.PASSWORD_INPUT, password)
        self.click_element(AccountPageLocators.LOGIN_BUTTON)

    @allure.step('Нажать кнопку "Личный кабинет"')
    def click_account_button(self):
        self.click_element(AccountPageLocators.ACCOUNT_BUTTON)

    @allure.step('Нажать кнопку "История заказов"')
    def click_order_history(self):
        self.click_element(AccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Нажать кнопку "Выход"')
    def logout(self):
        self.click_element(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step('Проверить успешность входа (кнопка "Выход" видна)')
    def is_logout_visible(self):
        return self.is_visible(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step('Проверить, что отображается кнопка "Вход" после выхода')
    def is_login_visible_after_logout(self):
        return self.get_text(AccountPageLocators.LOGIN_AFTER_LOGOUT) == 'Вход'





