import allure
from playwright.sync_api import Page

from base.pages.modal_form.modal_page import ModalPage
from base.pages.modal_form.modal_methods import ModalMethods
from base.pages.authorization.authorization_method import AuthorizationMethod


class ModalStart:
    @staticmethod
    def elements_start(page: Page, modal_form: ModalPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.modals_form(page)

            with allure.step("Открытие и закрытие маленького модального окна"):
                ModalMethods.click_on_small_modal(modal_form)
                ModalMethods.close_on_small_modal(modal_form)
                ModalMethods.check_text_small(modal_form)

            with allure.step("Открытие и закрытие большого модального окна"):
                ModalMethods.click_on_lagre_modal(modal_form)
                ModalMethods.close_on_lagre_modal(modal_form)
                ModalMethods.check_text_large(modal_form)

        except AssertionError as e:
            errors.append(str(e))
