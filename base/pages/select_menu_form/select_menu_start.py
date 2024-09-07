import allure
from playwright.sync_api import Page

from base.pages.select_menu_form.select_menu_page import SelectMenuPage
from base.pages.select_menu_form.select_menu_methods import SelectMenuMethods
from base.pages.authorization.authorization_method import AuthorizationMethod


class SelectMenuStart:
    def select_menu_start(page: Page, select_menu_form: SelectMenuPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.select_menu_form(page)

            with allure.step("Открытие выпадающих списков"):
                SelectMenuMethods.click_on_value(select_menu_form)
                SelectMenuMethods.click_on_one(select_menu_form)
                SelectMenuMethods.click_on_old(select_menu_form)
                SelectMenuMethods.click_on_multiselect(select_menu_form)
                SelectMenuMethods.click_on_car(select_menu_form)


        except AssertionError as e:
            errors.append(str(e))
