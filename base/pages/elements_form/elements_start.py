import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.elements_form.elements_page import ElementsPage
from base.pages.elements_form.elements_methods import ElementsMethods


class ElementsStart:
    @staticmethod
    def elements_start(page: Page, elements_form: ElementsPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.auth_elements_form(page)

            with allure.step("Ввод данных пользователя"):
                ElementsMethods.fill_name_input(elements_form)
                ElementsMethods.fill_email(elements_form)
                ElementsMethods.fill_current_adress(elements_form)
                ElementsMethods.fill_permanent_adress(elements_form)
                ElementsMethods.fill_email(elements_form)
                ElementsMethods.submit_button(elements_form)

        except AssertionError as e:
            errors.append(str(e))
