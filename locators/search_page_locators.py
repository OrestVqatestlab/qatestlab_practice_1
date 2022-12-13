from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_FIELD = (By.XPATH, '/html/body/main/header/div/div/div[1]/div[2]/div/div[2]/form/input[2]')
    SEARCH_BUTTON = (By.XPATH, '/html/body/main/header/div/div/div[1]/div[2]/div/div[2]/form/button')
    GOODS_QUANTITY = (By.XPATH, '/html/body/main/section/div/div/section/section/div[1]/div/div[1]/p')
    ITEMS = (By.CSS_SELECTOR, 'article')
    CURRENCY_BUTTON = (By.XPATH, '/html/body/main/header/nav/div/div/div[1]/div[2]/div[2]/div/a')
    USD_CURRENCY = (By.XPATH, '/html/body/main/header/nav/div/div/div[1]/div[2]/div[2]/div/ul/li[3]/a')
    CURRENT_CURRENCY = (By.XPATH, '/html/body/main/header/nav/div/div/div[1]/div[2]/div[2]/div/span[2]')
    SORT_BUTTON = (By.XPATH, '/html/body/main/section/div/div/section/section/div[1]/div/div[2]/div/div/a')
    SORT_HL = (By.XPATH, '/html/body/main/section/div/div/section/section/div[1]/div/div[2]/div/div/div/a[5]')