import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):
    @allure.step("Получить число счётчика 'Выполнено за всё время'")
    def get_number_counter_all_orders(self):
        return self.get_text_on_element(OrderFeedPageLocators.COUNTER_COMPLETED_ALL_TIME)
    
    @allure.step("Получить число счётчика 'Выполнено за сегодня'")
    def get_number_counter_for_today_orders(self):
        return self.get_text_on_element(OrderFeedPageLocators.COUNTER_COMPLETED_TODAY)
    
    @allure.step("Получить число из раздела 'В работе'")
    def get_number_from_section_at_work(self, order_number):
        order_number = '0' + order_number
        order_number_in_progress_locator = OrderFeedPageLocators.get_order_number_in_progress(order_number)
        text_status_completed_orders = 'Все текущие заказы готовы!'

        return self.wait_for_text_to_change(order_number_in_progress_locator, text_status_completed_orders)
    
    @allure.step("Клик по кнопке 'Конструктор'")
    def click_on_constructor_button(self):
        self.click_on_element_action_chains(MainPageLocators.BUTTON_CONSTRUCTOR, delay=0.5)
