import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.headless = True
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service, chrome_options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
