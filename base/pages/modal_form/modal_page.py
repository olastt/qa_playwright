from playwright.sync_api import Page

from base.page_factory.button import Button
from base.page_factory.input import Input


class ModalPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.locator = None

        """Локаторы страницы: Открытие Small Modal"""
        self.open_small_modal = Button(page, locator='//*[@id="showSmallModal"]', name='Open')

        """Локаторы страницы: Закрытие Small Modal"""
        self.close_small_modal = Button(page, locator='//*[@id="closeSmallModal"]', name='Close')

        """Локаторы страницы: Открытие Large Modal"""
        self.open_lagre_modal = Button(page, locator='//*[@id="showLargeModal"]', name='Open')

        """Локаторы страницы: Закрытие Large Modal"""
        self.close_lagre_modal = Button(page, locator='//*[@id="closeLargeModal"]', name='Close')
