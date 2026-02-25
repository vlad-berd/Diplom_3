import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage
from curl import *
from data import Credentials


@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):
    browser = request.param
    if browser == 'Chrome':
        options = OptionsChrome()
        options.add_argument("--windows-size=1600,900")
        browser = webdriver.Chrome(options=options)
    elif browser == 'Firefox':
        options = Options()
        options.add_argument("--windows-size=1600,900")
        browser = webdriver.Firefox(options=options)

    browser.get(MAIN_URL)
    
    yield browser

    browser.quit()

@pytest.fixture()
def authenticated_driver(driver):
    driver.get(LOGIN_URL)
    login_page = LoginPage(driver)
    order_feed_page = OrderFeedPage(driver)
    main_page = MainPage(driver)

    login_page.fill_email_field(Credentials.email)
    login_page.fill_password_field(Credentials.password)
    login_page.click_on_login_button()

    yield driver

    order_feed_page.click_on_constructor_button()
    main_page.click_on_personal_account_button()
    
    personal_account_page = PersonalAccountPage(driver)
    personal_account_page.click_on_logout_button()
