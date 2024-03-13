import time
from random import randint
from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject


class AccountPage(PageObject):
    # Localizadores da página de Login
    url_account_page = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    class_name_account = 'fontBig ng-binding'
    txt_name_account = 'Fernando Benbassat'

    xpath_change_to_second_account = '//select/option[2]'
    xpath_account_number = '//div[@class="center"][1]/strong[1]'
    xpath_transactions = '//*[@ng-click="transactions()"]'
    xpath_deposit = '//*[@ng-click="deposit()"]'
    xpath_withdrawl = '//*[@ng-click="withdrawl()"]'
    xpath_balance = '//div[@class="center"][1]/strong[2]'

    xpath_deposit_amount = '//*[@ng-model="amount"]'
    xpath_deposit_submit = '//button[@type="submit"]'
    xpath_deposit_success_msg = '//span[@class="error ng-binding"]'
    txt_success_deposit_msg = 'Deposit Successful'

    xpath_withdrawl_amount = '//*[@ng-model="amount"]'
    xpath_withdrawl_submit = '//button[@type="submit"]'
    xpath_withdraw_success_msg = '//span[@class="error ng-binding"]'
    xpath_unsuccess_withdraw_msg = '//span[@class="error ng-binding"]'
    txt_success_withdraw_msg = 'Transaction successful'
    txt_unsuccess_withdraw_msg = 'Transaction Failed. You can not withdraw amount more than the balance.'

    # ver dps
    txt_complete_name = "//table[@class='center']//strong"
    xpath_delete_customer = '//*[@ng-click="deleteCust(cust)"]'
    xpath_home_btn = '//button[@class="btn home"]'

    # Metodos do login usuário do banco
    def __init__(self, driver):
        super(AccountPage, self).__init__(driver=driver)

    def is_url_account_page(self):
        return self.is_url(url=self.url_account_page)

    def is_account_page(self):
        page_text = self.driver.find_element(By.XPATH, self.class_name_account).text
        return self.is_url_account_page and page_text == self.txt_name_account

    def change_account(self):
        self.driver.find_element(By.XPATH, self.xpath_change_to_second_account).click()

    def confirm_second_account_number(self):
        account = self.driver.find_element(By.XPATH, self.xpath_change_to_second_account).text
        new_account = self.driver.find_element(By.XPATH, self.xpath_account_number).text
        return account == new_account

    def deposit_randoms_values(self, times=1):
        self.driver.find_element(By.XPATH, self.xpath_deposit).click()
        time.sleep(2)
        # usar o random pra selecionar valores aleatorios
        for i in range(times):
            random_product_index = randint(1000, 1999)
            self.driver.find_element(By.XPATH, self.xpath_deposit_amount).send_keys(random_product_index)
            self.driver.find_element(By.XPATH, self.xpath_deposit_submit).click()
            time.sleep(1)

    def withdraw_randoms_values(self, times=1):
        self.driver.find_element(By.XPATH, self.xpath_withdrawl).click()
        time.sleep(2)
        # usar o random pra selecionar valores aleatorios
        for i in range(times):
            random_product_index = randint(100, 999)
            self.driver.find_element(By.XPATH, self.xpath_withdrawl_amount).send_keys(random_product_index)
            self.driver.find_element(By.XPATH, self.xpath_withdrawl_submit).click()
            time.sleep(1)

    def deposit_completed(self):
        success_msg = self.driver.find_element(By.XPATH, self.xpath_deposit_success_msg).text
        return success_msg == self.txt_success_deposit_msg

    def withdraw_uncompleted(self):
        unsuccess_msg = self.driver.find_element(By.XPATH, self.xpath_unsuccess_withdraw_msg).text
        return unsuccess_msg == self.txt_unsuccess_withdraw_msg

    def withdraw_completed(self):
        success_msg = self.driver.find_element(By.XPATH, self.xpath_withdraw_success_msg).text
        return success_msg == self.txt_success_withdraw_msg

    def go_to_transactions(self):
        self.driver.find_element(By.XPATH, self.xpath_transactions).click()

    def get_balance(self):
        balance = self.driver.find_element(By.XPATH, self.xpath_balance).text
        return balance

    def go_to_home_page(self):
        self.driver.find_element(By.XPATH, self.xpath_home_btn).click()
