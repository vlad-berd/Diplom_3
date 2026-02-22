import allure

from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage
from curl import *


class TestOrderFeed:
    @allure.title("Счётчик 'Выполнено за всё время' увеличивается после создания нового заказа")
    @allure.description("Автроризуем пользователя. Собираем бургер из ингредиентов. Проверяем, что общий счётчик заказов увеличился")
    def test_counter_all_time_increases_with_new_order_success(self, authenticated_driver):
        main_page = MainPage(authenticated_driver)
        order_feed_page = OrderFeedPage(authenticated_driver)
        ingredient_name_1 = 'Краторная булка N-200i'
        ingredient_name_2 = 'Мясо бессмертных моллюсков Protostomia'
        ingredient_name_3 = 'Соус с шипами Антарианского плоскоходца'
        ingredient_name_4 = 'Филе Люминесцентного тетраодонтимформа'
        main_page.click_on_order_feed_button()
        before_number_all_orders = int(order_feed_page.get_number_counter_all_orders())
        order_feed_page.click_on_constructor_button()
        main_page.transfer_ingredient_burger_constructor(ingredient_name_1)
        main_page.transfer_ingredient_burger_constructor(ingredient_name_2)
        main_page.transfer_ingredient_burger_constructor(ingredient_name_3)
        main_page.transfer_ingredient_burger_constructor(ingredient_name_2)
        main_page.transfer_ingredient_burger_constructor(ingredient_name_4)
        main_page.click_on_place_order_button()
        main_page.get_number_order_id()
        main_page.close_modal_window_order_id()
        main_page.click_on_order_feed_button()

        ather_number_all_orders = int(order_feed_page.get_number_counter_all_orders())

        assert before_number_all_orders < ather_number_all_orders

    @allure.title("Счётчика 'Выполнено за сегодня' увеличивается после создания нового заказа")
    @allure.description("Автроризуем пользователя. Собираем бургер из ингредиентов. Проверяем, что счётчик 'Выполнено за сегодня' заказов увеличился")
    def test_counter_for_today_increases_with_new_order_success(self, authenticated_driver):
        main_page = MainPage(authenticated_driver)
        order_feed_page = OrderFeedPage(authenticated_driver)
        ingredient_name_1 = 'Краторная булка N-200i'
        ingredient_name_2 = 'Мясо бессмертных моллюсков Protostomia'
        ingredient_name_3 = 'Соус с шипами Антарианского плоскоходца'
        ingredient_name_4 = 'Филе Люминесцентного тетраодонтимформа'
        main_page.click_on_order_feed_button()
        before_number_for_today_orders = int(order_feed_page.get_number_counter_for_today_orders())
        order_feed_page.click_on_constructor_button()
        main_page.transfer_ingredient_burger_constructor(ingredient_name_1)
        main_page.transfer_ingredient_burger_constructor(ingredient_name_2)
        main_page.transfer_ingredient_burger_constructor(ingredient_name_3)
        main_page.transfer_ingredient_burger_constructor(ingredient_name_2)
        main_page.transfer_ingredient_burger_constructor(ingredient_name_4)
        main_page.click_on_place_order_button()
        main_page.get_number_order_id()
        main_page.close_modal_window_order_id()
        main_page.click_on_order_feed_button()

        ather_number_for_today_orders = int(order_feed_page.get_number_counter_for_today_orders())

        assert before_number_for_today_orders < ather_number_for_today_orders
    
    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    @allure.description("Автроризуем пользователя. Собираем бургер из ингредиентов. Проверяем, что номер нового заказа появился в разделе 'В работе'")
    def test_number_appears_in_at_work_after_placing_order_success(self, authenticated_driver):
        main_page = MainPage(authenticated_driver)
        order_feed_page = OrderFeedPage(authenticated_driver)
        ingredient_name_1 = 'Краторная булка N-200i'
        ingredient_name_2 = 'Мясо бессмертных моллюсков Protostomia'
        ingredient_name_3 = 'Соус с шипами Антарианского плоскоходца'
        ingredient_name_4 = 'Филе Люминесцентного тетраодонтимформа'
        main_page.click_on_order_feed_button()
        order_feed_page.click_on_constructor_button()
        main_page.transfer_ingredient_burger_constructor(ingredient_name_1)
        main_page.transfer_ingredient_burger_constructor(ingredient_name_2)
        main_page.transfer_ingredient_burger_constructor(ingredient_name_3)
        main_page.transfer_ingredient_burger_constructor(ingredient_name_2)
        main_page.transfer_ingredient_burger_constructor(ingredient_name_4)
        main_page.click_on_place_order_button()
        order_number = main_page.get_number_order_id()
        main_page.close_modal_window_order_id()
        main_page.click_on_order_feed_button()

        order_number_from_section_at_work = int(order_feed_page.get_number_from_section_at_work(order_number=order_number))

        assert int(order_number) == int(order_number_from_section_at_work)
