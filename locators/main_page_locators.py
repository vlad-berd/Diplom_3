from selenium.webdriver.common.by import By


class MainPageLocators:
    # РАЗДЕЛ "КОНСТРУКТОР"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__') and normalize-space()='Конструктор']")  # Кнопка "Конструктор"
    BUTTON_ORDER_FEED = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__') and normalize-space()='Лента Заказов']")  # Кнопка "Лента Заказов"
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__') and normalize-space()='Личный Кабинет']")  # кнопка "Личный кабинет"

    @staticmethod
    def get_ingredient(name):
        return By.XPATH, f"//p[contains(@class, 'BurgerIngredient_ingredient__text__') and normalize-space()='{name}']"
    
    # Конструктор бургеров
    BURGER_CONSTRUCTOR_BASKET = (By.CLASS_NAME, "BurgerConstructor_basket__list__l9dp_")  # Конструктор бургеров
    # Оформленный заказ полсе авторизации
    NUMBER_ORDER_ID = (By.CLASS_NAME, "text_type_digits-large")  # Идентификатор заказа
    BUTTON_CLOSE_MODAL_WINDOW_ORDER_ID = (By.CSS_SELECTOR, ".Modal_modal_opened__3ISw4 .Modal_modal__close__TnseK")  # Кнопка закрытия окна оформленного заказа

    @staticmethod
    def get_ingredient_counter(name):
        return By.XPATH, f"//a[contains(., '{name}')]//p[@class='counter_counter__num__3nue1']"

    # Всплывающее окно с деталями ингредиента
    TITLE_MODAL_WINDOW_INGREDIENT = (By.CLASS_NAME, "Modal_modal__title_modified__3Hjkd")  # Заголовок "Детали ингредиента"
    BUTTON_CLOSE_MODAL_WINDOW_INGREDIENT = (By.CSS_SELECTOR, ".Modal_modal_opened__3ISw4 .Modal_modal__close__TnseK")  # Кнопка закрытия окна "Детали ингредиента"

    # Кнопка после авторизации
    BUTTON_PLACE_ORDER = (By.CLASS_NAME, "button_button__33qZ0")  # Кнопка "Оформить заказ"
