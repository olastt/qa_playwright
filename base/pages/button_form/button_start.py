import allure
from playwright.sync_api import Page

from base.pages.button_form.button_page import ButtonPage
from base.pages.button_form.button_methods import ButtonMethods
from base.pages.authorization.authorization_method import AuthorizationMethod


class ButtonStart:
    @staticmethod
    def button_start(page: Page, button_form: ButtonPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.auth_button_form(page)

            with allure.step("Нажатие на кнопку"):
                ButtonMethods.double_click(button_form)
                ButtonMethods.right_click(button_form)
                ButtonMethods.simple_click(button_form)

        except AssertionError as e:
            errors.append(str(e))

