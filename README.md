<p align="center">
  <a href="https://stellarburgers.education-services.ru/" target="_blank">
    <img width="120" height="auto" src="https://stellarburgers.education-services.ru/favicon.ico" title="Перейти на Stellar Burgers" alt="Stellar Burgers">
  </a>
</p>

## Проект автоматизации тестирования веб-приложения Stellar Burgers
#### Протестирована функциональность в Google Chrome и Mozilla Firefox.

**Стек**: Python, PyTest, Selenium, Allure-pytest, Allure-report.

### Проведённые тесты:
### - Проверка основной функциональности в модуле _test_constructor_:
**test_click_on_constructor_button_redirect_to_main_page_success** - проверка перехода на страницу '/' по клику на кнопку 'Конструктор'\
**test_click_on_order_feed_button_redirect_to_feed_page_success** - проверка перехода на страницу '/feed' по клику на кнопку 'Лента Заказов'\
**test_click_on_ingredient_show_modal_window_ingredient_details_success** - проверка появления всплывающего окна 'Детали ингредиента' по клику на ингредиент\
**test_click_on_close_button_closes_modal_window_ingredient_details_success** - проверка закрытия всплывающего окнка 'Детали ингредиента' по клику на крестик\
**test_ingredient_counter_increases_on_add_constructor_burgers_success** - проверка увелечения счётчика ингредиента при добавление в конструктор бургеров

### - Раздел "Лента заказов" в модуле _test_order_feed.py_:
**test_counter_all_time_increases_with_new_order_success** - проверка увеличения счётчика 'Выполнено за всё время' после создания нового заказа\
**test_counter_for_today_increases_with_new_order_success** - проверка увеличения счётчика "Счётчика 'Выполнено за сегодня' после создания нового заказа\
**test_number_appears_in_at_work_after_placing_order_success** - проверка появления номера заказа в разделе "В работе" после оформления заказа

## Установка зависимостей:
```
pip3 install -r requirements.txt
```
##### Для Python второй версии:
```
pip install -r requirements.txt
```
## Посмотреть отчёт в формате веб-страницы:
```
allure serve allure_results
```
