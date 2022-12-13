from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Locators


class MainPage(BasePage):

    def find_current_currency(self):
        current_currency = self.element_is_visible(Locators.CURRENT_CURRENCY)
        return current_currency

    def find_item_currency(self):
        item_currency = self.element_is_visible(Locators.ITEMS_CURRENCY)
        return item_currency

    def find_items_currency(self):
        items_currency = self.elements_are_visible(Locators.ITEMS_CURRENCY)
        return items_currency

    def change_currency_to_usd(self):
        self.element_is_visible(Locators.CURRENCY_BUTTON).click()
        self.element_is_visible(Locators.USD_CURRENCY).click()
