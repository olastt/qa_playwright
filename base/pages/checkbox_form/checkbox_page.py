from playwright.sync_api import Page

from base.page_factory.button import Button
from base.page_factory.input import Input


class CheckboxPage:
    def __init__(self, page: Page) -> None:
        self.locator = None
        self.page = page

        """Локаторы страницы: Раскрытие списка Home"""
        self.home = Button(page, locator='//*[@aria-label="Toggle"]', name='Home')

        """Локаторы страницы: Раскрытие папки Desktop"""
        self.desktop = Button(page, locator='(//*[@aria-label="Toggle"])[2]', name='Desktop')

        """Локаторы страницы: Раскрытие папки Documents"""
        self.documents = Button(page, locator='(//*[@aria-label="Toggle"])[3]', name='Documents')

        """Локаторы страницы: Раскрытие папки Downloads"""
        self.downloads = Button(page, locator='(//*[@aria-label="Toggle"])[4]', name='Downloads')

        """Локаторы страницы: Выбор папки Desktop"""
        self.choose_desktop = Button(page, locator='//*[@for="tree-node-desktop"]', name='Desktop')

        """Локаторы страницы: Выбор папки Documents"""
        self.choose_documents = Button(page, locator='//*[@for="tree-node-documents"]', name='Documents')

        """Локаторы страницы: Выбор папки Downloads"""
        self.choose_downloads = Button(page, locator='//*[@for="tree-node-downloads"]', name='Downloads')

        """Локаторы страницы: Закрытие выпадающего списка посредством нажатия на кнопку минуса"""
        self.close_all = Button(page, locator='//*[@aria-label="Collapse all"]', name='Minus')

        """Локаторы страницы: Раскрытие выпадающего списка посредством нажатия на кнопку плюса"""
        self.choose_all = Button(page, locator='//*[@aria-label="Expand all"]', name='Home')

