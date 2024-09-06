import allure
from playwright.sync_api import Page

from base.pages.button_form.button_page import ButtonPage
from base.pages.button_form.button_start import ButtonStart

from conftest import button_form


class TestButton:
    @allure.epic("Тесты потока 1")
    @allure.feature("Button")
    @allure.title("Выбор кнопок")
    def test_radio_form(self, page: Page, button_form: ButtonPage):
        ButtonStart.button_start(page, button_form)
