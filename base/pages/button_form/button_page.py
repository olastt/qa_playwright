from playwright.sync_api import Page
from base.page_factory.button import Button


class ButtonPage:
    def __init__(self, page: Page) -> None:
        self.page = page  # Используем переданный объект page

        """Локаторы страницы: Двойной клик"""
        self.click = Button(page, locator='//*[@id="doubleClickBtn"]', name='Double Click')

        """Локаторы страницы: Клик правой кнопкой мыши"""
        self.right = Button(page, locator='//*[@id="rightClickBtn"]', name='Right Click')

        """Локаторы страницы: Простой клик"""
        self.simple = Button(page, locator='(//*[@class="btn btn-primary"])[3]', name='Click')
