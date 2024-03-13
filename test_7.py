from Pages.AccountPage import AccountPage
from Pages.AddCustomerPage import AddCustomerPage
from Pages.BankManagerPage import BankManagerPage
from Pages.CustomerLoginPage import CustomerLoginPage
from Pages.LoginPage import LoginPage
from Pages.OpenAccountPage import OpenAccount
from Pages.TransactionPAge import TransactionPage


class Test7:

    def test_transactions_equals_balance(self, open_login_page):

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
        open_account_page.click_customers_btn()

        # Retorna à home page e segue para o login de clientes
        login_page = LoginPage(driver=open_account_page.driver)
        assert login_page.is_url_login(), "Aplicação não está na pagina de login!"
        login_page.click_customer_login_btn()

        # Seleciona cliente e entra na conta
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
        account_page.go_to_transactions()

        # Na aba de histórico de transações verifica todos os créditos e débitos realizados
        transactions_page = TransactionPage(driver=account_page.driver)
        assert transactions_page.is_transaction_page(), "Não está na página do extrato de transações"
        new_balance = transactions_page.get_info_from_table()
        transactions_page.go_back_btn()

        # Retorna para a aba inicial da conta e confirma se o extrato está batendo com o balanço atual da conta
        account_page = AccountPage(driver=transactions_page.driver)
        assert account_page.is_url_account_page(), "Não está na página da conta do usuário"
        assert str(new_balance) in account_page.get_balance(),\
            "Valor do extrato é diferente do apresentado como balanço"
