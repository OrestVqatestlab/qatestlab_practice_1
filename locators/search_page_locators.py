from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, "#search_widget input[name='s']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, '#search_widget button')
    GOODS_QUANTITY = (By.CSS_SELECTOR, 'div.total-products p')
    ITEMS = (By.CSS_SELECTOR, 'article')
    CURRENCY_BUTTON = (By.CSS_SELECTOR, 'div.currency-selector > a')
    USD_CURRENCY = (By.CSS_SELECTOR, "a[title='Доллар США']")
    CURRENT_CURRENCY = (By.CSS_SELECTOR, 'div.currency-selector span')
    SORT_BUTTON = (By.CSS_SELECTOR, 'a.select-title i')
    SORT_HL = (By.CSS_SELECTOR, 'div.dropdown-menu a')

