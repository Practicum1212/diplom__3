from selenium.webdriver.common.by import By

class OrderFeedPageLocators:

    PLACE_AN_ORDER = (
        By.XPATH,
        "//button[contains(@class,'button_button_type_primary') and contains(text(),'Оформить заказ')]"
    )

    ORDER_FEED_BUTTON = (
        By.XPATH,
        "//p[contains(text(),'Лента Заказов')]"
    )

    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//p[contains(text(),'Конструктор')]"
    )

    ORDER_HISTORY_BUTTON = (
        By.XPATH,
        "//a[contains(@class,'Account_link') and contains(text(),'История заказов')]"
    )

    ACCOUNT_BUTTON = (
        By.XPATH,
        "//p[contains(text(),'Личный Кабинет')]"
    )

    # Последний заказ в ленте — без жёсткого индекса, берём первый в найденном списке через код
    LAST_ORDER = (
        By.XPATH,
        "//ul[contains(@class,'OrderFeed_list')]//li[contains(@class,'OrderFeed_listItem')]"
    )

    ORDER_DETAILS_CONTENT = (
        By.XPATH,
        "//p[contains(@class,'text_type_main-medium') and contains(@class,'mb-8')]"
    )

    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "//h4[contains(text(), 'Выполнено за всё время')]/following-sibling::p[contains(@class,'text_type_digits')]"
    )

    TODAY_COMPLETED_COUNTER = (
        By.XPATH,
        "//h4[contains(text(), 'Выполнено за сегодня')]/following-sibling::p[contains(@class,'text_type_digits')]"
    )

    CLOSE_ORDER_DETAILS_BUTTON = (
        By.XPATH,
        "//button[@type='button']//*[name()='svg']"
    )

    ORDER_ID = (
        By.XPATH,
        "//h2[contains(@class, 'Modal_modal__title')]"
    )

    ORDER_ID_IN_FEED = (
        By.XPATH,
        "//*[contains(text(), '{0}')]"
    )

    ORDER_IN_PROGRESS_LOCATOR = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderListReady')]//p[contains(@class,'text_type_digits-default')]"
    )

    FEED_TITLE = (
        By.XPATH,
        "//h1[contains(@class, 'text_type_main-large')]"
    )

    LOGIN_AFTER_LOGOUT_BURGER = (
        By.XPATH,
        "//h1[contains(@class,'text_type_main-large') and contains(text(),'Соберите бургер')]"
    )

    ORDER_PREPARING_MESSAGE = (
        By.XPATH,
        "//p[contains(@class,'text_type_main-small') and contains(text(),'готовится')]"
    )

    ORDER_MODAL = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]"
    )

    ORDER_ID_TEXT = (
        By.XPATH,
        "//p[contains(@class, 'text_type_digits-large')]"
    )

    ORDER_NUMBER_IN_FEED = (
        By.XPATH,
        "//ul[contains(@class,'OrderFeed_list')]//li//p[contains(@class,'text_type_digits-default')]"
    )

    MODAL_OVERLAY = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal__overlay')]"
    )



