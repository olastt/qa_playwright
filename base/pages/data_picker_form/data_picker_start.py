import allure
from playwright.sync_api import Page

from base.pages.data_picker_form.data_picker_methods import DataPickerMethods
from base.pages.data_picker_form.data_picker_page import DataPickerPage
from base.pages.authorization.authorization_method import AuthorizationMethod


class DataPickerStart:

    @staticmethod
    def data_picker_start(page: Page, data_picker_form: DataPickerPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.data_picker_form(page)

            with allure.step("Открытие первого дата пикера"):
                DataPickerMethods.click_on_calendar(data_picker_form)

            with allure.step("Открытие второго дата пикера"):
                DataPickerMethods.click_on_second_calendar(data_picker_form)

        except AssertionError as e:
            errors.append(str(e))
