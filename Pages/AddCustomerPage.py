import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class AddCustomerPage(PageObject):
    # Localizadores da página de Login
    url_add_customer = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust'
    xpath_add_customer = '//*[@type="submit"]'
    css_open_account = '[ng-click="openAccount()"]'
    css_first_name = '[ng-model="fName"]'
    css_last_name = '[ng-model="lName"]'
    css_postal_code = '[ng-model="postCd"]'
    txt_add_customer = 'Add Customer'
    class_home_btn = '//button[@class="btn home"]'

    # Metodos do gerente do banco
    def __init__(self, driver):
        super(AddCustomerPage, self).__init__(driver=driver)

    def is_url_add_customer(self):
        return self.is_url(url=self.url_add_customer)

    def is_manager_page(self):
        page_text = self.driver.find_element(By.XPATH, self.xpath_add_customer).text
        return self.is_url_add_customer and page_text == self.txt_add_customer

    def information_to_add_customer(self, first_name='Fernando', last_name='Benbassat', postal_code='51021-350'):
        self.driver.find_element(By.CSS_SELECTOR, self.css_first_name).send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, self.css_last_name).send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, self.css_postal_code).send_keys(postal_code)
        self.driver.find_element(By.XPATH, self.xpath_add_customer).click()

    def get_confirmation_pop_up(self):  # Ver como pegar a mensagem do pop up
        pop_up = Alert(self.driver).text
        return pop_up

    def accept_pop_up(self):
        pop_up = Alert(self.driver)
        pop_up.accept()

    def click_open_account_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_open_account).click()

    def click_to_home(self):
        self.driver.find_element(By.XPATH, self.class_home_btn).click()

