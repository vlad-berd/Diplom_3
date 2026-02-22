from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    COUNTER_COMPLETED_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'text_type_digits-large') and contains(@class, 'text')]")  # Счётчик "Выполнено за всё время"
    COUNTER_COMPLETED_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'text_type_digits-large') and contains(@class, 'text')]")  # Счётчик "Выполнено за сегодня"
    
    # Блок "В работе"
    (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__')]//li[last()]")  # Номер последнего заказа

    @staticmethod
    def get_order_number_in_progress(order_number):
        return By.XPATH, f"//ul[contains(@class, 'OrderFeed_orderList__cBvyi')]/li[contains(@class, 'text') and contains(@class, 'text_type_digits-default') and contains(@class, 'mb-2') and normalize-space()='{order_number}']"
