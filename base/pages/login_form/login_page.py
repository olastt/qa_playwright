from playwright.sync_api import Page

from base.page_factory.button import Button
from base.page_factory.input import Input


class LoginPage:

    def __init__(self, page: Page) -> None:
        self.locator = None
        self.page = page

        """Локаторы страницы: Ввод имени"""
        self.name = Input(page, locator='//*[@id="userName"]', name='Имя')

        """Локаторы страницы: Ввод пароля"""
        self.password = Input(page, locator='//*[@id="password"]', name='Пароль')

        """Локаторы страницы: Нажатие на кнопку логина"""
        self.login = Button(page, locator='//*[@id="login"]', name='Пароль')
