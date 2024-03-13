from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Pages.PageObject import PageObject


class CustomerLoginPage(PageObject):
    # Localizadores da página de Login
    url_customer_login = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'
    xpath_select_customer = '//select'
    xpath_login_btn = '//button[@class="btn btn-default"]'
    txt_complete_name = 'Fernando Benbassat'
    xpath_open_account_msg = '//*[@ng-show="noAccount"]'
    class_customer_without_account = 'fontBig ng-binding'
    txt_customer_without_account = 'Please open an account with us.'
    xpath_finding_customer = '//select/option[@class="ng-binding ng-scope"]'
    txt_select_customer = '---Your Name---'


    class_home = 'btn home'

    # Metodos do login usuário do banco
    def __init__(self, driver):
        super(CustomerLoginPage, self).__init__(driver=driver)

    def is_url_customer_login(self):
        return self.is_url(url=self.url_customer_login)

    def is_customer_login_page(self):
        page_text = self.driver.find_element(By.XPATH, self.xpath_select_customer).text
        return self.is_url_customer_login and page_text == self.txt_select_customer

    def search_and_click_customer(self):
        select = Select(self.driver.find_element(By.XPATH, self.xpath_select_customer))
        select.select_by_visible_text('Fernando Benbassat')
        self.driver.find_element(By.XPATH, self.xpath_login_btn).click()

    def create_account_message(self):
        message = self.driver.find_element(By.XPATH, self.xpath_open_account_msg).text
        return message == self.txt_customer_without_account

    def is_customer_in_list(self):
        for i in range(len(self.xpath_finding_customer)):
            searching = self.xpath_finding_customer + f'[{i}]'
            customer = self.driver.find_element(By.XPATH, searching).text
            if customer == self.txt_complete_name:
                return True
        return False