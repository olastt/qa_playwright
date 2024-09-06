import allure

from playwright.sync_api import Page
from base.pages.checkbox_form.checkbox_page import CheckboxPage
from base.pages.checkbox_form.checkbox_start import CheckboxStart
from conftest import checkbox_form


class TestCheckboxForm:
    @allure.epic("Тесты потока 1")
    @allure.feature("Checkbox")
    @allure.title("Выбор чекбоксов")
    def test_checkbox_form(self, page: Page, checkbox_form: CheckboxPage):
        CheckboxStart.checkbox_start(page, checkbox_form)
