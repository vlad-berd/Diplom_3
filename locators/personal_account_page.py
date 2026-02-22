from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    BUTTON_LOGOUT = (By.XPATH, "//button[contains(@class, 'Account_button__') and text()='Выход']")  # Кнопка "Выход"
