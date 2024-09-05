import allure

from playwright.sync_api import Page
from base.pages.elements_form.elements_page import ElementsPage
from base.pages.elements_form.elements_start import ElementsStart
from conftest import elements_form


class TestElementsForm:
    @allure.epic("Тесты потока 1")
    @allure.feature("Elements")
    @allure.title("Заполнение формы элементов")
    def test_elements_form(self, page: Page, elements_form: ElementsPage):
        ElementsStart.elements_start(page, elements_form)
