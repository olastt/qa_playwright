import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.checkbox_form.checkbox_page import CheckboxPage
from base.pages.checkbox_form.checkbox_methods import CheckboxMethods


class CheckboxStart:
    @staticmethod
    def checkbox_start(page: Page, checkbox_form: CheckboxPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.auth_checkbox_form(page)

            with allure.step("Выбор чекбоксов"):
                CheckboxMethods.click_on_home(checkbox_form)
                CheckboxMethods.click_on_desktop(checkbox_form)
                CheckboxMethods.click_on_documents(checkbox_form)
                CheckboxMethods.click_on_downloads(checkbox_form)
                CheckboxMethods.choose_desktop(checkbox_form)
                CheckboxMethods.choose_documents(checkbox_form)
                CheckboxMethods.choose_downloads(checkbox_form)
                CheckboxMethods.choose_close_all(checkbox_form)
                CheckboxMethods.choose_all(checkbox_form)

        except AssertionError as e:
            errors.append(str(e))
