import allure
from playwright.sync_api import Page

from base.pages.select_menu_form.select_menu_page import SelectMenuPage
from base.pages.select_menu_form.select_menu_start import SelectMenuStart
from conftest import select_menu_form


class TestSelectMenuForm:
    @allure.epic("Тесты потока 1")
    @allure.feature("Select Menu")
    @allure.title("Выбор из выпадающих списков")
    def test_radio_form(self, page: Page, select_menu_form: SelectMenuPage):
        SelectMenuStart.select_menu_start(page, select_menu_form)
