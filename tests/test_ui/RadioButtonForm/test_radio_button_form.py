import allure
from playwright.sync_api import Page

from base.pages.radio_button_form.radio_button_page import RadioButtonPage
from base.pages.radio_button_form.radio_button_start import RadioButtonStart
from conftest import radio_button_form


class TestRadioButton:

    @allure.epic("Тесты потока 1")
    @allure.feature("Radio Button")
    @allure.title("Выбор радио кнопок")
    def test_radio_form(self, page: Page, radio_button_form: RadioButtonPage):
        RadioButtonStart.radio_button_start(page, radio_button_form)
