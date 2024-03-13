from Pages.AddCustomerPage import AddCustomerPage
from Pages.BankManagerPage import BankManagerPage
from Pages.CustomerLoginPage import CustomerLoginPage
from Pages.LoginPage import LoginPage


class Test4:

    def test_client_without_account(self, open_login_page):
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
        add_customer_page.click_to_home()

        # Retorna à home page e segue para o login de clientes
        login_page = LoginPage(driver=add_customer_page.driver)
        assert login_page.is_url_login(), "Aplicação não está na pagina de logins!"
        login_page.click_customer_login_btn()

        # Tenta entrar na página de usuário sem conta aberta no seu nome
        customer_login_page = CustomerLoginPage(driver=login_page.driver)
        assert customer_login_page.is_url_customer_login(), "Não está na página de login do usuário"
        customer_login_page.search_and_click_customer()
        assert customer_login_page.create_account_message()
