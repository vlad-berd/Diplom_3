from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    COUNTER_COMPLETED_ALL_TIME = (By.CSS_SELECTOR, ".undefined .OrderFeed_number__2MbrQ")  # Счётчик "Выполнено за всё время"
    COUNTER_COMPLETED_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]")  # Счётчик "Выполнено за сегодня"
    
    # Блок "В работе"
    LAST_ORDER_NUMBER = (By.CSS_SELECTOR, ".OrderFeed_orderListReady__1YFem .text")  # Номер последнего заказа
