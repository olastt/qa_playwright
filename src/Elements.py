# base_test.py

from selenium import webdriver


class BaseTest:
    def __init__(self):
        self.url = None
        self.driver = None

    def setup_method(self):
        self.url = 'https://demoqa.com/'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def open_site(self, url):
        self.driver.get(url)
