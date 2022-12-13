import pytest
from pages.main_page import MainPage


class TestMainPage:

    @pytest.fixture(autouse=True)
    def class_setup(self, driver):
        self.main_page = MainPage(driver, 'http://prestashop-automation.qatestlab.com.ua/ru/')
        self.main_page.open()

    def test_items_currency(self, driver):
        """Makes sure that all items currencies are equal"""
        items_currencies = []
        items_currency = self.main_page.find_items_currency()
        for item in items_currency: items_currencies.append(item.text[-1])
        assert [items_currencies[0]] * len(items_currencies) == items_currencies, 'Items currencies are not equal!'

    def test_currency(self, driver):
        """Makes sure that choosen and actual currencies are equal"""
        current_currency = self.main_page.find_current_currency().text[-1]
        item_currency = self.main_page.find_item_currency().text[-1]
        assert current_currency == item_currency, 'Pages currency isn`t equal to items!'

    def test_currency_usd(self, driver):
        """Makes sure that choosen currency is USD"""
        self.main_page.change_currency_to_usd()
        current_currency = self.main_page.find_current_currency().text[-1]
        assert current_currency == '$', 'Pages currency isn`t equal to USD!'








