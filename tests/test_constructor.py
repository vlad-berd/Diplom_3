import allure

from pages.main_page import MainPage
from curl import *


class TestConstructor:
    @allure.title("Проверка перехода на страницу '/' по клику на кнопку 'Конструктор'")
    @allure.description("Нажимаем на кнопку 'Конструктор' и проверяем переход на страницу '/'")
    def test_click_on_constructor_button_redirect_to_main_page_success(self, driver):
        main_page = MainPage(driver)

        main_page.click_on_constructor_button()

        assert main_page.get_current_url() == MAIN_URL

    @allure.title("Проверка перехода на страницу '/feed' по клику на кнопку 'Лента Заказов'")
    @allure.description("Нажимаем на кнопку 'Лента Заказов' и проверяем переход на страницу '/feed'")
    def test_click_on_order_feed_button_redirect_to_feed_page_success(self, driver):
        main_page = MainPage(driver)

        main_page.click_on_order_feed_button()

        assert main_page.get_current_url() == ORDER_FEED_URL

    @allure.title("Проверка появления всплывающего окна 'Детали ингредиента' по клику на ингредиент")
    @allure.description("Нажимаем на ингредиент и проверяем появление всплывающего окнка 'Детали ингредиента'")
    def test_click_on_ingredient_show_modal_window_ingredient_details_success(slef, driver):
        main_page = MainPage(driver)
        ingredient_name = 'Филе Люминесцентного тетраодонтимформа'
        main_page.click_on_ingredient(ingredient_name)

        text_title = main_page.get_text_modal_window_details_ingredient()

        assert text_title == 'Детали ингредиента'

    @allure.title("Проверка закрытия всплывающего окнка 'Детали ингредиента' по клику на крестик")
    @allure.description("Нажимаем на крестик и проверяем закрытие всплывающего окнка 'Детали ингредиента'")
    def test_click_on_close_button_closes_modal_window_ingredient_details_success(self, driver):
        main_page = MainPage(driver)
        ingredient_name = 'Филе Люминесцентного тетраодонтимформа'
        main_page.click_on_ingredient(ingredient_name)

        response = main_page.close_modal_window_ingredient_details()

        assert response, "Окно с ингридиентом не закрылось через крестик"
        assert main_page.get_current_url() == MAIN_URL

    @allure.title("Проверка увелечения счётчика ингредиента при добавление в конструктор бургеров")
    @allure.description("Переносим ингредиент в конструктор бургеров и проверяем число счётчика добавленного ингредиента")
    def test_ingredient_counter_increases_on_add_constructor_burgers_success(self, driver):
        main_page = MainPage(driver)
        ingredient_name = 'Филе Люминесцентного тетраодонтимформа'
        main_page.transfer_ingredient_burger_constructor(ingredient_name)
        main_page.transfer_ingredient_burger_constructor(ingredient_name)

        counter_number = main_page.get_ingredient_counter_number(ingredient_name)

        assert counter_number == 2
