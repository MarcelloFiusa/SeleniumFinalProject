from Pages.AddCustomerPage import AddCustomerPage
from Pages.BankManagerPage import BankManagerPage
from Pages.OpenAccountPage import OpenAccount


class Test2:

    def test_click_add_account(self, open_login_page):

        # Abre o navegador na página de seleção dos logins de cliente e gerente do banco
        login_page = open_login_page
        assert login_page.is_url_login(), "Aplicação não está na pagina de login!"
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
