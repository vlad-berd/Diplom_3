## Проект автоматизации тестирования веб-приложения Stellar Burgers

### Протестирована функциональность в Google Chrome и Mozilla Firefox.
1. Основа для написания автотестов — фреймворк pytest, selenium.
2. Библитека для генерации отчёта Allure

### Проведённые тесты:
- Проверка основной функциональности test_constructor
    - test_click_on_constructor_button_redirect_to_main_page_success - переход по клику на "Конструктор"
    - test_click_on_order_feed_button_redirect_to_feed_page_success - переход по клику на раздел "Лента заказов"
    - test_click_on_ingredient_show_modal_window_ingredient_details_success - если кликнуть на ингредиент, появится всплывающее окно с деталями
    - test_click_on_close_button_closes_modal_window_ingredient_details_success - всплывающее окно закрывается кликом по крестик
    - test_ingredient_counter_increases_on_add_constructor_burgers_success - при добавлении ингредиента в заказ, счётчик этого ингредиента увеличивается
- Раздел "Лента заказов"
    - test_counter_all_time_increases_with_new_order_success - при создании нового заказа счётчик "Выполнено за всё время" увеличивается
    - test_counter_for_today_increases_with_new_order_success - при создании нового заказа счётчик "Выполнено за сегодня" увеличивается
    - test_number_appears_in_at_work_after_placing_order_success - после оформления заказа его номер появляется в разделе "В работе"

### Установить зависимости:
— pip3 install -r requirements.txt

Сформировать отчёт в формате веб-страницы:
- allure serve allure_results