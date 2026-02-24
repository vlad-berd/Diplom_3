from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL = (By.NAME, "name")  # Поле "Email"
    PASSWORD = (By.NAME, "Пароль")  # Поле "Пароль"
    BUTTON_LOGIN = (By.CLASS_NAME, "button_button__33qZ0")  # Кнопка "Войти" на странице авторизации
