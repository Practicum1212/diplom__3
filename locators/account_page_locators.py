from selenium.webdriver.common.by import By

class AccountPageLocators:

    # Кнопка входа в личный кабинет в шапке
    ACCOUNT_BUTTON = (
        By.XPATH,
        "//p[contains(text(),'Личный Кабинет')]"
    )

    # Поле ввода e-mail (проверить, что name='name' действительно email)
    EMAIL_INPUT = (
        By.XPATH,
        "//input[@name='name']"
    )

    # Поле ввода пароля
    PASSWORD_INPUT = (
        By.XPATH,
        "//input[@name='Пароль']"
    )

    # Кнопка входа
    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        ".button_button__33qZ0"
    )

    # Кнопка выхода из аккаунта
    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Выход')]"
    )

    # Кнопка "История заказов"
    ORDER_HISTORY_BUTTON = (
        By.XPATH,
        "//a[contains(@class,'Account_link') and contains(text(), 'История заказов')]"
    )

    # Завершённый заказ в истории
    ORDER_COMPLETED = (
        By.XPATH,
        "//p[contains(@class,'OrderHistory_visible') and contains(@class,'text_type_main-small')]"
    )

    # Заголовок страницы входа после выхода
    LOGIN_AFTER_LOGOUT = (
        By.XPATH,
        "//h2[contains(text(),'Вход')]"
    )

    # Заголовок главной страницы после выхода
    LOGIN_AFTER_LOGOUT_BURGER = (
        By.XPATH,
        "//h1[contains(@class,'text_type_main-large') and contains(text(), 'Соберите бургер')]"
    )
