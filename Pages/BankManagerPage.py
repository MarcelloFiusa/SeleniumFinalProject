from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class BankManagerPage(PageObject):
    # Localizadores da página de Login
    url_bank_manager = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
    css_add_customer = '[ng-click="addCust()"]'
    css_open_account = '[ng-click="openAccount()"]'
    css_customers = '[ng-click="showCust()"]'
    txt_add_customer = 'Add Customer'

    # Metodos do gerente do banco
    def __init__(self, driver):
        super(BankManagerPage, self).__init__(driver=driver)

    def is_url_manager(self):
        return self.is_url(url=self.url_bank_manager)

    def is_manager_page(self):
        page_text = self.driver.find_element(By.CSS_SELECTOR, self.css_add_customer).text
        return self.is_url_manager and page_text == self.txt_add_customer

    def click_add_customer_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_add_customer).click()

    def click_open_account_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_open_account).click()

    def click_customers_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_customers).click()
