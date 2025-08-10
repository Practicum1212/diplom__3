from selenium.webdriver.common.by import By

class MainPageLocators:


    BUN_DROP_AREA_TOP = (
        By.XPATH,
        "//div[contains(@class,'constructor-element_pos_top')]"
    )

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")


    BURGER_CONSTRUCTOR_SECTION = (By.XPATH, "//section[@class='BurgerIngredients_ingredients__1N8v2']")




    COMPLETED_ORDERS = (By.XPATH, "//p[contains(text(),'Готовы:')]")


    COMPLETED_ORDERS_COUNTER = (By.XPATH, "//p[normalize-space()='153072']")


    INGREDIENT_R2D3_BUN = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")


    INGREDIENT_DETAILS_TITLE = (By.XPATH,
                                "//h2[@class='Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10']")


    CLOSE_INGREDIENT_DETAILS_BUTTON = (By.XPATH,
                                       "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@type='button']//*[name()='svg']//*[name()='path' and contains(@fill-rule,'evenodd')]")

    ORDER_TARGET_TOP = (By.XPATH, "//img[@alt='Перетяните булочку сюда (верх)']")


    INGREDIENT_COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")

    PLACE_AN_ORDER = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")

    ORDER_SUCCESS_MESSAGE = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal__')]//p[contains(text(), 'Ваш заказ начали готовить')]"
    )

    ORDER_IN_PROGRESS_LOCATOR = (
        By.XPATH,
        "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']//li[1]//*[contains(text(), '{}')]"
    )

    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    FIRST_INGREDIENT = (By.XPATH, "(//div[@class='BurgerIngredient_ingredient__image__EgMaL'])[1]")
    BASKET = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket__container')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal__overlay')]")