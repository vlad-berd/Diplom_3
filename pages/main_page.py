import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Клик по кнопке 'Конструктор'")
    def click_on_constructor_button(self):
        self.click_on_element_action_chains(MainPageLocators.BUTTON_CONSTRUCTOR, delay=0.5)
    
    @allure.step("Клик по кнопке 'Лента Заказов'")
    def click_on_order_feed_button(self):
        self.click_on_element_action_chains(MainPageLocators.BUTTON_ORDER_FEED, delay=0.5)
    
    @allure.step("Клик по кнопке 'Личный Кабинет'")
    def click_on_personal_account_button(self):
        self.click_on_element(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_on_place_order_button(self):
        self.click_on_element(MainPageLocators.BUTTON_PLACE_ORDER)

    @allure.step("Клик по игредиенту")
    def click_on_ingredient(self, name_ingredient):
        self.click_on_element(MainPageLocators.get_ingredient(name=name_ingredient))
    
    @allure.step("Получить заголовок всплывающего окна 'Детали ингредиента'")
    def get_text_modal_window_details_ingredient(self):
        return self.get_text_on_element(MainPageLocators.TITLE_MODAL_WINDOW_INGREDIENT)

    @allure.step("Закрыть всплывающее окно 'Детали ингредиента'")
    def close_modal_window_ingredient_details(self):
        self.click_on_element(MainPageLocators.BUTTON_CLOSE_MODAL_WINDOW_INGREDIENT)
        return self.wait_for_element_become_invisible(MainPageLocators.TITLE_MODAL_WINDOW_INGREDIENT)
    
    @allure.step("Перенести ингредиент {name_ingredient} в конструктор бургеров")
    def transfer_ingredient_burger_constructor(self, name_ingredient):
        self.drag_and_drop(MainPageLocators.get_ingredient(name_ingredient), MainPageLocators.BURGER_CONSTRUCTOR_BASKET)

    @allure.step("Получить число счётчика ингредиента")
    def get_ingredient_counter_number(self, name_ingredient):
        return int(self.get_text_on_element(MainPageLocators.get_ingredient_counter(name_ingredient)))
    
    @allure.step("Получить номер оформленного заказа")
    def get_number_order_id(self):
        default_value = '9999'
        return self.wait_for_text_to_change(MainPageLocators.NUMBER_ORDER_ID, default_value)
    
    @allure.step("Закрыть всплывающее окно оформленного заказа")
    def close_modal_window_order_id(self):
        self.click_on_element_action_chains(MainPageLocators.BUTTON_CLOSE_MODAL_WINDOW_ORDER_ID, delay=0.5)
        return self.wait_for_element_become_invisible(MainPageLocators.NUMBER_ORDER_ID)
