from selenium.webdriver.common.by import By

class AccountPageLocators:

    ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.button_button__33qZ0')
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")
    ORDER_COMPLETED = (By.XPATH, "//p[@class='OrderHistory_visible__19YMB text text_type_main-small mb-7']")
    LOGIN_AFTER_LOGOUT = (By.XPATH, "//h2[contains(text(),'Вход')]")
    LOGIN_AFTER_LOGOUT_BURGER = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")