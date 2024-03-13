import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

import Pages
from Pages.PageObject import PageObject


class TransactionPage(PageObject):
    # Localizadores da página de Login
    url_transaction = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx'
    xpath_back_btn = '//button[@ng-click="back()"]'
    xpath_reset_btn = '//*[@ng-click="reset()"]'
    xpath_start_date_btn = '//*[@ng-model="startDate"]'
    xpath_end_date_btn = '//*[@ng-model="end"]'
    txt_reset_btn = 'Reset'
    xpath_table = '//table/tbody'

    # Metodos do login usuário do banco
    def __init__(self, driver):
        super(TransactionPage, self).__init__(driver=driver)

    def is_url_transaction_page(self):
        return self.is_url(url=self.url_transaction)

    def is_transaction_page(self):
        page_text = self.driver.find_element(By.XPATH, self.xpath_reset_btn).text
        return self.url_transaction and page_text == self.txt_reset_btn

    def get_info_from_table(self):
        list_credit = []
        list_debit = []
        sum_cred = 0
        sum_debit = 0
        i = 1
        while i != 0:
            xpath_table_inside = self.xpath_table + f'/tr[{i}]' + '/td[2]'
            xpath_table_inside_type = self.xpath_table + f'/tr[{i}]' + '/td[3]'
            try:
                is_credit_or_debit = self.driver.find_element(By.XPATH, xpath_table_inside_type).text
                get_value = self.driver.find_element(By.XPATH, xpath_table_inside).text
                if is_credit_or_debit == 'Credit':
                    list_credit.append(int(get_value))
                if is_credit_or_debit == 'Debit':
                    list_debit.append(int(get_value))
                i += 1
            except NoSuchElementException:
                break
        for n in list_credit:
            sum_cred += n
        for x in list_debit:
            sum_debit += x
        total = sum_cred - sum_debit
        return str(total)

    def go_back_btn(self):
        self.driver.find_element(By.XPATH, self.xpath_back_btn).click()
