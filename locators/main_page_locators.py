from selenium.webdriver.common.by import By

class MainPageLocators:

    BUN_DROP_AREA_TOP = (
        By.XPATH,
        "//div[contains(@class,'constructor-element_pos_top')]"
    )

    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//p[contains(text(),'Конструктор')]"
    )

    BURGER_CONSTRUCTOR_SECTION = (
        By.XPATH,
        "//section[contains(@class, 'BurgerIngredients_ingredients')]"
    )

    COMPLETED_ORDERS = (
        By.XPATH,
        "//p[contains(text(),'Готовы:')]"
    )

    COMPLETED_ORDERS_COUNTER = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderListReady')]//p[contains(@class, 'text_type_digits')]"
    )

    INGREDIENT_R2D3_BUN = (
        By.XPATH,
        "//img[@alt='Флюоресцентная булка R2-D3']"
    )

    INGREDIENT_DETAILS_TITLE = (
        By.XPATH,
        "//h2[contains(@class,'Modal_modal__title') and contains(@class,'text_type_main-large')]"
    )

    CLOSE_INGREDIENT_DETAILS_BUTTON = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal_opened')]//button[@type='button']//*[name()='svg']//*[name()='path' and contains(@fill-rule,'evenodd')]"
    )

    ORDER_TARGET_TOP = (
        By.XPATH,
        "//img[@alt='Перетяните булочку сюда (верх)']"
    )

    INGREDIENT_COUNTER = (
        By.XPATH,
        "//p[contains(@class,'counter_counter__num')]"
    )

    PLACE_AN_ORDER = (
        By.XPATH,
        "//button[contains(@class, 'button_button_type_primary') and contains(text(), 'Оформить заказ')]"
    )

    ORDER_SUCCESS_MESSAGE = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal__')]//p[contains(text(), 'Ваш заказ начали готовить')]"
    )

    ORDER_IN_PROGRESS_LOCATOR = (
        By.XPATH,
        "//ul[contains(@class,'OrderFeed_orderListReady')]//p[contains(text(), '{}')]"
    )

    ORDER_FEED_BUTTON = (
        By.XPATH,
        "//p[contains(text(),'Лента Заказов')]"
    )

    FIRST_INGREDIENT = (
        By.XPATH,
        "(//div[contains(@class,'BurgerIngredient_ingredient__image')])[1]"
    )

    BASKET = (
        By.XPATH,
        "//div[contains(@class, 'BurgerConstructor_basket__container')]"
    )

    PLACE_ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Оформить заказ')]"
    )

    MODAL_OVERLAY = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal__overlay')]"
    )
