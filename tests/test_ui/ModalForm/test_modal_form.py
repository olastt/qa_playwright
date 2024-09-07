import allure

from playwright.sync_api import Page
from base.pages.modal_form.modal_page import ModalPage
from base.pages.modal_form.modal_start import ModalStart
from conftest import modal_form


class TestModalForm:
    @allure.epic("Тесты потока 1")
    @allure.feature("Modals")
    @allure.title("Открытие и закрытие модальных окон")
    def test_modal_form(self, page: Page, modal_form: ModalPage):
        ModalStart.elements_start(page, modal_form)
