from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class PageObject:
    class_title = 'title'

    def __init__(self, driver=None, browser=None):
        if driver:
            self.driver = driver
        else:
            if browser == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser == 'chrome':
                self.driver = webdriver.Chrome()
            else:
                raise Exception('Browser não suportado!')
            self.driver.implicitly_wait(10)

    def is_url(self, url):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_to_be(url))
        return self.driver.current_url == url

    def close(self):
        self.driver.quit()
