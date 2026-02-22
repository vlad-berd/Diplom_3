import allure

from pages.base_page import BasePage
from locators.personal_account_page import PersonalAccountPageLocators


class PersonalAccountPage(BasePage):
    @allure.step("Кликнуть по кнопке 'Выход'")
    def click_on_logout_button(self):
        self.click_on_element_action_chains(PersonalAccountPageLocators.BUTTON_LOGOUT, delay=0.5)
