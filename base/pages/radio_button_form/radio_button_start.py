import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.radio_button.radio_button_page import RadioButtonPage
from base.pages.radio_button.radio_button_methods import RadioButtonMethods


class Radio_Button_Start:
    @staticmethod
    def radio_button_start(page: Page, radio_button_form: RadioButtonPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.auth_radio_button_form(page)

            with allure.step("Выбор радио кнопок"):
                RadioButtonMethods.click_on_yes(radio_button_form)
                RadioButtonMethods.click_on_impressive(radio_button_form)

        except AssertionError as e:
            errors.append(str(e))
