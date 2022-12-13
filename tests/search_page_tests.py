import re
import time
import pytest
from selenium.webdriver.common.by import By
from pages.search_page import SearchPage


class TestSearchPage:

    @pytest.fixture(autouse=True)
    def class_setup(self, driver):
        self.search_page = SearchPage(driver, 'http://prestashop-automation.qatestlab.com.ua/ru/')
        self.search_page.open()
        self.search_page.search()

    def test_searchpages_counter(self, driver):
        """Makes sure that counter works properly"""
        expected_number = int(re.findall(r'[0-9]+', self.search_page.get_expected_quantity().text)[0])
        actual_number = len(self.search_page.get_items())
        assert expected_number == actual_number, 'Counter isnt equal to items quantity!'

    def test_searchpages_currency(self,driver):
        """Makes sure that currency is equal to USD"""
        self.search_page.change_currency_to_usd()
        current_currency = self.search_page.find_current_currency().text[-1]
        assert current_currency == '$', 'Pages currency isn`t equal to USD!'

    def test_sortresults_hl(self,driver):
        """Makes sure that results sorts by descending"""
        self.search_page.change_sorting_hl()
        time.sleep(5)
        items = self.search_page.get_items()
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

    def test_check_discount(self, driver):
        """Makes sure that discounts are calculated properly"""
        items = self.search_page.get_items()
        for item in items:
            try:
                item.find_element(By.CLASS_NAME, 'regular-price').text
                discount_exist = True
            except:
                discount_exist = False
            finally:
                if discount_exist:
                    regular_price = float(re.findall(
                        r'[0-9]+.[0-9]+', item.find_element(By.CLASS_NAME, 'regular-price').text.replace(',','.'))[0])
                    discount_percentage = float(
                        re.findall(r'[0-9]+', item.find_element(By.CLASS_NAME, 'discount-percentage').text)[0])
                    discounted_price = float(re.findall(
                        r'[0-9]+.[0-9]+', item.find_element(By.CLASS_NAME, 'price').text.replace(',', '.'))[0])
                    discount = round((regular_price * discount_percentage / 100), 2)
                    assert discounted_price == round((regular_price - discount), 2), 'Wrong discounted price'
