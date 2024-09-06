from playwright.sync_api import Page

from base.page_factory.button import Button
from base.page_factory.input import Input


class RadioButtonPage:
    def __init__(self, page: Page) -> None:
        self.locator = None
        self.page = page

        """Локаторы страницы: Клик по радио кнопке Yes"""
        self.click_on_yes = Button(page, locator='//*[@for="yesRadio"]', name='Yes')

        """Локаторы страницы: Клик по радио кнопке Impressive"""
        self.click_on_impressive = Button(page, locator='//*[@for="impressiveRadio"]', name='Impressive')

    # нагуглила, здесь получаем локатор элемента для проверки
    def get_yes_radio_locator(self):
        return self.page.locator('//*[@for="yesRadio"]')

    # здесь берем полученный локатор и методом is checked проверяем что элемент действительно выбран
    def is_yes_radio_selected(self):
        radio_button = self.get_yes_radio_locator()
        return radio_button.is_checked()

    # здесь получаем локатор элемента для проверки
    def get_impressive_radio_locator(self):
        return self.page.locator('//*[@for="impressiveRadio"]')

    # здесь берем полученный локатор и методом is checked проверяем что элемент действительно выбран
    def is_impressive_radio_selected(self):
        radio_button = self.get_impressive_radio_locator()
        return radio_button.is_checked()

