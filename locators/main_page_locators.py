from selenium.webdriver.common.by import By


class MainPageLocators:
    CURRENT_CURRENCY = (By.CSS_SELECTOR, 'div.currency-selector span')
    ITEMS_CURRENCY = (By.CLASS_NAME, 'price')
    CURRENCY_BUTTON = (By.CSS_SELECTOR, 'div.currency-selector a')
    USD_CURRENCY = (By.CSS_SELECTOR, "a[title='Доллар США']")


