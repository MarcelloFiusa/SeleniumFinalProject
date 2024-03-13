import time

from selenium.common import NoSuchElementException

from Pages.AccountPage import AccountPage
from Pages.AddCustomerPage import AddCustomerPage
from Pages.BankManagerPage import BankManagerPage
from Pages.CustomerLoginPage import CustomerLoginPage
from Pages.SearchCustomersPage import SearchCustomerPage
from Pages.LoginPage import LoginPage
from Pages.OpenAccountPage import OpenAccount


class Test9:

    def test_delete_user_account(self, open_login_page):

        # Abre o navegador na página de seleção dos logins de cliente e gerente do banco
        login_page = open_login_page
        assert login_page.is_url_login(), "Aplicação não está na pagina de logins!"
        login_page.click_bank_manager_login_btn()

        # Seleciona a opção de adicionar cliente, na página do gerente do banco
        bank_manager_page = BankManagerPage(driver=login_page.driver)
        assert bank_manager_page.is_url_manager(), "Não está na página do gerente"
        bank_manager_page.click_add_customer_btn()

        # Adiciona o cliente ao banco de dados do banco XYZ
        add_customer_page = AddCustomerPage(driver=bank_manager_page.driver)
        assert add_customer_page.is_url_add_customer(), "Não está na página de adicionar clientes"
        add_customer_page.information_to_add_customer()
        add_customer_page.get_confirmation_pop_up()
        add_customer_page.accept_pop_up()
        assert add_customer_page.is_url_add_customer(), "Não está na página de adicionar clientes"
        add_customer_page.click_open_account_btn()

        # Cria nova conta e associa ao cliente registrado anteriormente
        open_account_page = OpenAccount(driver=add_customer_page.driver)
        assert open_account_page.is_url_open_account(), "Não está na página de abrir conta"
        open_account_page.information_to_add_account()
        open_account_page.get_confirmation_pop_up()
        open_account_page.accept_pop_up()
        assert open_account_page.is_url_open_account(), "Não está na página de abrir conta"
        open_account_page.click_customers_btn()

        # Na home page, segue para o login de clientes do banco
        login_page = LoginPage(driver=open_account_page.driver)
        assert login_page.is_url_login(), "Aplicação não está na pagina de logins"
        login_page.click_customer_login_btn()

        # Seleciona e entra na conta do cliente registrado anteriormente
        customer_login_page = CustomerLoginPage(driver=login_page.driver)
        assert customer_login_page.is_url_customer_login(), "Não está na página de login do usuário"
        customer_login_page.search_and_click_customer()

        # Clica na aba de depósito e deposita três valores aleatórios
        account_page = AccountPage(driver=customer_login_page.driver)
        assert account_page.is_url_account_page(), "Não está na página da conta do usuário"
        account_page.deposit_randoms_values(times=3)
        assert account_page.deposit_completed(), "Depósito não realizado!"
        # Clica na aba de débito e debita três valores aleatórios
        account_page.withdraw_randoms_values(times=3)
        assert account_page.withdraw_completed(), "Débito não realizado!"
        account_page.go_to_home_page()

        # Retorna para a página do gerente do banco
        login_page = LoginPage(driver=account_page.driver)
        assert login_page.is_url_login(), "Aplicação não está na pagina de logins"
        login_page.click_bank_manager_login_btn()

        # Segue para a aba de pesquisa dos clientes registrados
        bank_manager_page = BankManagerPage(driver=login_page.driver)
        assert bank_manager_page.is_url_manager(), "Não está na página do gerente do banco"
        bank_manager_page.click_customers_btn()

        # Pesquisa pelo cliente criado anteriormente e o exclui do sistema
        search_customer_page = SearchCustomerPage(driver=bank_manager_page.driver)
        assert search_customer_page.is_url_customers(), "Não está na página de pesquisa de clientes"
        search_customer_page.click_and_search()
        assert search_customer_page.is_first_name_listed(), "Nome não registrado no banco de dados de clientes"
        search_customer_page.delete_customer()
        search_customer_page.go_to_home_page()

        # Retorna para a home page
        login_page = LoginPage(driver=search_customer_page.driver)
        assert login_page.is_url_login(), "Aplicação não está na pagina de logins"
        login_page.click_customer_login_btn()

        # Tenta logar na conta do usuário excluído
        customer_login_page = CustomerLoginPage(driver=login_page.driver)
        assert customer_login_page.is_url_customer_login(), "Não está na página de login do usuário"
        try:
            customer_login_page.search_and_click_customer()
            not_found = False
        except NoSuchElementException:
            not_found = True
        assert not_found, "Conta pertence ao banco de dados do banco"
