import allure

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    @allure.step("Заполнить поле 'Email' значением {value}")
    def fill_email_field(self, value):
        self.send_keys_to_input(LoginPageLocators.EMAIL, value)

    @allure.step("Заполнить поле 'Password' значением {value}")
    def fill_password_field(self, value):
        self.send_keys_to_input(LoginPageLocators.PASSWORD, value)
    
    @allure.step("Кликнуть на кнопку 'Войти'")
    def click_on_login_button(self):
        self.click_on_element_action_chains(LoginPageLocators.BUTTON_LOGIN, delay=0.1)
