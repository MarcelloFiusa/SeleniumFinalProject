from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class SearchCustomerPage(PageObject):
    # Localizadores da página de Login
    url_customers = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list'
    xpath_search_customer = '//*[@ng-model="searchCustomer"]'
    xpath_first_name = '//table/tbody/tr/td[1]'
    txt_search_customer = 'Search Customer'
    txt_first_name = 'Fernando'
    xpath_delete_customer = '//*[@ng-click="deleteCust(cust)"]'
    xpath_home_btn = '//button[@class="btn home"]'

    # Metodos do gerente do banco
    def __init__(self, driver):
        super(SearchCustomerPage, self).__init__(driver=driver)

    def is_url_customers(self):
        return self.is_url(url=self.url_customers)

    def is_customers_page(self):
        page_text = self.driver.find_element(By.XPATH, self.xpath_search_customer).text
        return self.is_url_customers and page_text == self.txt_search_customer

    def click_and_search(self):
        self.driver.find_element(By.XPATH, self.xpath_search_customer).send_keys(self.txt_first_name)

    def is_first_name_listed(self):
        first_name = self.driver.find_element(By.XPATH, self.xpath_first_name).text
        return first_name == self.txt_first_name

    def delete_customer(self):
        self.driver.find_element(By.XPATH, self.xpath_delete_customer).click()

    def goes_to_home(self):
        self.driver.find_element(By.CLASS_NAME, self.class_home).click()

    def go_to_home_page(self):
        self.driver.find_element(By.XPATH, self.xpath_home_btn).click()



