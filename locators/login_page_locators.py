from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле "Email"
    PASSWORD = (By.XPATH, "//input[@name='Пароль']")  # Поле "Пароль"
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти" на странице авторизации
