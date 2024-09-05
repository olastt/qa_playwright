from playwright.sync_api import Page

from base.page_factory.button import Button
from base.page_factory.input import Input


class ElementsPage:
    def __init__(self, page: Page) -> None:
        self.locator = None
        self.page = page

        """Локаторы страницы: Имя"""
        self.full_name = Input(page, locator='//*[@id="userName"]', name='Олеся')

        """Локаторы страницы: Почта"""
        self.email = Input(page, locator='//*[@id="userEmail"]', name='Почта')

        """Локаторы страницы: Текущий адрес"""
        self.current_adress = Input(page, locator='//*[@id="currentAddress"]', name='Текущий адрес')

        """Локаторы страницы: Постоянный адрес"""
        self.permanent_adress = Input(page, locator='//*[@id="permanentAddress"]', name='Постоянный адрес')

        """Локаторы страницы: Кнопка сабмита"""
        self.submit_button = Button(page, locator='//*[@id="submit"]', name='Кнопка')

