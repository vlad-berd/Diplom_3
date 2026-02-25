import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    @allure.step("Подождать невидимости элемента")
    def wait_for_element_become_invisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Подождать изменения текста элемента")
    def wait_for_text_to_change(self, locator, expected_text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, expected_text))
    
    @allure.step("Перетащить элемент source к элементу target")
    def drag_and_drop(self, source_locator, target_locator, timeout=10):
        source_element = self.wait_for_element(locator=source_locator, timeout=timeout)
        target_element = self.wait_for_element(locator=target_locator, timeout=timeout)

        if self.driver.capabilities['browserName'] == 'chrome':
            actions = ActionChains(self.driver)
            actions.drag_and_drop(source_element, target_element).perform()
        elif self.driver.capabilities['browserName'] == 'firefox':
            self.driver.execute_script("""
                const source = arguments[0];
                const target = arguments[1];
                
                // Создаем события
                const dragStartEvent = new Event('dragstart', { bubbles: true });
                const dropEvent = new Event('drop', { bubbles: true });
                const dragEndEvent = new Event('dragend', { bubbles: true });
                
                source.dispatchEvent(dragStartEvent);
                target.dispatchEvent(dropEvent);
                source.dispatchEvent(dragEndEvent);
                """, source_element, target_element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        self.wait_for_element(locator, timeout).click()
        
    @allure.step("Кликнуть на элемент")
    def click_on_element_action_chains(self, locator, delay=0.5, timeout=10):
        element = self.wait_for_element(locator, timeout)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).pause(delay).click().perform()

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text
    
    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)
