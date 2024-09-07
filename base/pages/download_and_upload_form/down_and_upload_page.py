from playwright.sync_api import Page

from base.page_factory.button import Button
from base.page_factory.input import Input


class DownAndUploadPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.locator = None

        """Локаторы страницы: Кнопка скачивания"""
        self.download = Button(page, locator='//*[@id="downloadButton"]', name='Download')

        """Локаторы страницы: Загрузка файла"""
        self.upload = Button(page, locator='//*[@id="uploadFile"]', name='Файл')


