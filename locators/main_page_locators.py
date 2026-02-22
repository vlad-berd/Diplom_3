from selenium.webdriver.common.by import By


class MainPageLocators:
    # РАЗДЕЛ "КОНСТРУКТОР"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__') and normalize-space()='Конструктор']")  # Кнопка "Конструктор"
    BUTTON_ORDER_FEED = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__') and normalize-space()='Лента Заказов']")  # Кнопка "Лента Заказов"
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__') and normalize-space()='Личный Кабинет']")  # кнопка "Личный кабинет"

    @staticmethod
    def get_ingredient(name):
        return By.XPATH, f"//p[contains(@class, 'BurgerIngredient_ingredient__text__') and normalize-space()='{name}']/ancestor::a[contains(@class, 'BurgerIngredient_ingredient__')]"
    
    # Конструктор бургеров
    BURGER_CONSTRUCTOR_BASKET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__')]//ul[contains(@class, 'BurgerConstructor_basket__list__')]")  # Конструктор бургеров
    # Оформленный заказ полсе авторизации
    NUMBER_ORDER_ID = (By.XPATH, "//p[text()='идентификатор заказа']/preceding-sibling::h2[1]")  # Идентификатор заказа
    BUTTON_CLOSE_MODAL_WINDOW_ORDER_ID = (By.XPATH, "//div[contains(@class, 'contentBox')]/following-sibling::button[1]")  # Кнопка закрытия окна оформленного заказа

    @staticmethod
    def get_ingredient_counter(name):
        return By.XPATH, f"//p[contains(@class, 'BurgerIngredient_ingredient__text__') and normalize-space()='{name}']/ancestor::a[contains(@class, 'BurgerIngredient_ingredient__')]//p[contains(@class, 'counter_counter__num__')]"

    # Всплывающее окно с деталями ингредиента
    TITLE_MODAL_WINDOW_INGREDIENT = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__')]//h2[contains(@class, 'Modal_modal__title_modified__') and normalize-space()='Детали ингредиента']")  # Заголовок "Детали ингредиента"
    BUTTON_CLOSE_MODAL_WINDOW_INGREDIENT = (By.XPATH, "//h2[text()='Детали ингредиента']/ancestor::div[@class='Modal_modal__container__Wo2l_']//button[contains(@class, 'Modal_modal__close__TnseK')]")  # Кнопка закрытия окна "Детали ингредиента"

    # Кнопка после авторизации
    BUTTON_PLACE_ORDER = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__')]//button[contains(@class, 'button_button__') and normalize-space()='Оформить заказ']")  # Кнопка "Оформить заказ"
