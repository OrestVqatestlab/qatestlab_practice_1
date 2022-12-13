from selenium.webdriver.common.by import By


class MainPageLocators:
    CURRENT_CURRENCY = (By.XPATH, '/html/body/main/header/nav/div/div/div[1]/div[2]/div[2]/div/span[2]')
    ITEMS_CURRENCY = (By.CLASS_NAME, 'price')
    CURRENCY_BUTTON = (By.XPATH, '/html/body/main/header/nav/div/div/div[1]/div[2]/div[2]/div/a')
    USD_CURRENCY = (By.XPATH, '/html/body/main/header/nav/div/div/div[1]/div[2]/div[2]/div/ul/li[3]/a')


