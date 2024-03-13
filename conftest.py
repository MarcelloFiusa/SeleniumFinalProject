import pytest

from Pages.LoginPage import LoginPage


@pytest.fixture()
def open_login_page():
    select_browser = 'firefox'
    login_page = LoginPage(browser=select_browser)
    yield login_page
    login_page.close()
