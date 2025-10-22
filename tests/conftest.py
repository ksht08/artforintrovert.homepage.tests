import allure
import pytest
from selene import browser
from selenium import webdriver
from selene.support.shared import config

@pytest.fixture(scope="function", autouse=True)
def browser_management():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1600,1024")
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    config.driver = webdriver.Chrome(options=options)
    config.base_url = "https://online.artforintrovert.ru"
    config.timeout = 5.0

    browser.open("/")
    yield

    log_text = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(
                  log_text,
                  name = 'Web Browser logs',
                  attachment_type=allure.attachment_type.TEXT,
                  extension='.log',
                  )
    
    browser.quit()
