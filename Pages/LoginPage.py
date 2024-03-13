from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class LoginPage(PageObject):
    # Localizadores da página de Login
    url_login = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    css_customer_login = '[ng-click="customer()"]'
    css_bank_manager_login = '[ng-click="manager()"]'
    txt_customer_login = 'Customer Login'

    # Metodos de login
    def __init__(self, browser='firefox', driver=None):
        super(LoginPage, self).__init__(browser=browser, driver=driver)
        self.driver.get(self.url_login)


    def is_url_login(self):
        return self.is_url(url=self.url_login)

    def is_login_page(self):
        page_text = self.driver.find_element(By.CSS_SELECTOR, self.css_customer_login).text
        return self.is_url_login and page_text == self.txt_customer_login

    def click_customer_login_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_customer_login).click()

    def click_bank_manager_login_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_bank_manager_login).click()
