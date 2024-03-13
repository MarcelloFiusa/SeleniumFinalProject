import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.PageObject import PageObject


class OpenAccount(PageObject):
    # Localizadores da página de Login
    url_open_account = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount'
    xpath_process = '//*[@type="submit"]'
    id_customer_name = 'userSelect'
    id_currency = 'currency'
    class_customer = 'form-group'
    txt_process = 'Process'
    txt_name = 'Fernando Benbassat'
    txt_currency = 'Dollar'
    css_customers = '[ng-click="showCust()"]'

    # Metodos do gerente do banco
    def __init__(self, driver):
        super(OpenAccount, self).__init__(driver=driver)

    def is_url_open_account(self):
        return self.is_url(url=self.url_open_account)

    def is_open_account_page(self):
        page_text = self.driver.find_element(By.XPATH, self.xpath_process).text
        return self.is_url_open_account and page_text == self.txt_process

    def add_multiple_account(self, times=2):
        for i in range(times):
            dropdown_customers = Select(self.driver.find_element(By.ID, self.id_customer_name))
            dropdown_customers.select_by_visible_text(self.txt_name)
            dropdown_currency = Select(self.driver.find_element(By.ID, self.id_currency))
            dropdown_currency.select_by_visible_text(self.txt_currency)
            self.driver.find_element(By.XPATH, self.xpath_process).click()
            pop_up = Alert(self.driver)
            pop_up.accept()
            time.sleep(1)

    def information_to_add_account(self, currency=txt_currency):
        dropdown_customers = Select(self.driver.find_element(By.ID, self.id_customer_name))
        dropdown_customers.select_by_visible_text(self.txt_name)
        dropdown_currency = Select(self.driver.find_element(By.ID, self.id_currency))
        dropdown_currency.select_by_visible_text(currency)
        self.driver.find_element(By.XPATH, self.xpath_process).click()

    def get_confirmation_pop_up(self):
        pop_up = Alert(self.driver).text
        return pop_up

    def accept_pop_up(self):
        pop_up = Alert(self.driver)
        pop_up.accept()

    def click_customers_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_customers).click()
