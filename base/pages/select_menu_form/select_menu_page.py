from playwright.sync_api import Page

from base.page_factory.button import Button
from base.page_factory.input import Input


class SelectMenuPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.locator = None

        """Локаторы страницы: Открытие выпадающего списка Select Value"""
        self.open_value = Button(page, locator='//*[@id="withOptGroup"]', name='Value')

        """Локаторы страницы: Открытие выпадающего списка Select One"""
        self.open_one = Button(page, locator='//*[@id="selectOne"]', name='One')

        """Локаторы страницы: Открытие выпадающего списка Old Style Select Menu"""
        self.open_old = Button(page, locator='//*[@id="oldSelectMenu"]', name='Old')

        """Локаторы страницы: Открытие выпадающего списка Multiselect drop down"""
        self.open_multiselect = Button(page, locator='(//*[@class=" css-1hwfws3"])[3]', name='Multiselect')

        """Локаторы страницы: Выбор значения Audi"""
        self.choose_car = Button(page, locator='//*[@value="audi"]', name='Car')

