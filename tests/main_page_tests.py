import re
import time

import pytest
from selenium.webdriver.common.by import By
from pages.main_page import MainPage


class TestMainPage:

    @pytest.fixture(autouse=True)
    def class_setup(self, driver):
        self.main_page = MainPage(driver, 'http://prestashop-automation.qatestlab.com.ua/ru/')
        self.main_page.open()

    def test_items_currency(self, driver):
        """Makes sure that choosen and actual currencies are equal """
        items_currencies = []
        items_currency = self.main_page.find_items_currency()
        for item in items_currency: items_currencies.append(item.text[-1])
        assert [items_currencies[0]] * len(items_currencies) == items_currencies, 'Items currencies are not equal!'

    def test_currency(self, driver):
        current_currency = self.main_page.find_current_currency().text[-1]
        item_currency = self.main_page.find_item_currency().text[-1]
        assert current_currency == item_currency, 'Pages currency isn`t equal to items!'

    def test_currency_usd(self, driver):
        self.main_page.change_currency_to_usd()
        current_currency = self.main_page.find_current_currency().text[-1]
        assert current_currency == '$', 'Pages currency isn`t equal to USD!'

    def test_find_dress(self, driver):
        self.main_page.search()
        expected_number = int(re.findall(r'[0-9]+', self.main_page.get_expected_quantity().text)[0])
        actual_number = len(self.main_page.get_items())
        assert expected_number == actual_number, 'Counter isnt equal to items quantity!'
        self.main_page.change_currency_to_usd()
        current_currency = self.main_page.find_current_currency().text[-1]
        assert current_currency == '$', 'Pages currency isn`t equal to USD!'
        self.main_page.change_sorting_hl()
        time.sleep(5)
        items = self.main_page.get_items()
        prices = []
        for item in items:
            try:
                full_price = item.find_element(By.CLASS_NAME, 'regular-price').text
            except:
                full_price = item.find_element(By.CLASS_NAME, 'price').text
            finally:
                price = float(re.findall(r'[0-9]+.[0-9]+', full_price)[0].replace(',', '.'))
                prices.append(price)
        desc_list = sorted(prices, key=float, reverse=True)
        assert prices == desc_list, 'HL sorting doesnt work properly'

        for item in items:
            try:
                item.find_element(By.CLASS_NAME, 'regular-price').text
                discount_exist = True
            except:
                discount_exist = False
            finally:
                if discount_exist:
                    print("True")
                    regular_price = float(re.findall(r'[0-9]+.[0-9]+',
                                                     item.find_element(By.CLASS_NAME, 'regular-price').text.replace(',',
                                                                                                                    '.'))[
                                              0])
                    discount_percentage = float(
                        re.findall(r'[0-9]+', item.find_element(By.CLASS_NAME, 'discount-percentage').text)[0])
                    discounted_price = float(
                        re.findall(r'[0-9]+.[0-9]+', item.find_element(By.CLASS_NAME, 'price').text.replace(',', '.'))[
                            0])
                    discount = round((regular_price * discount_percentage / 100), 2)
                    assert discounted_price == round((regular_price - discount), 2), 'Wrong discounted price'








