import allure
from playwright.sync_api import Page
import time

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.practice_form.practice_form_methods import PracticeFormMethods
from base.pages.practice_form.practice_form_page import PracticeFormPage


class PracticeStart:
    @staticmethod
    def practice_form(page: Page, practice_form: PracticeFormPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.auth_practice_form(page)

            with allure.step("Ввод данных пользователя"):
                PracticeFormMethods.fill_name_input(practice_form)
                PracticeFormMethods.fill_email_input(practice_form)
                PracticeFormMethods.click_gender(practice_form)
                PracticeFormMethods.fill_number_input(practice_form)
                PracticeFormMethods.click_date_birth(practice_form)
                PracticeFormMethods.fill_subject_input(practice_form)
                PracticeFormMethods.choose_hobbies(practice_form)
                PracticeFormMethods.upload_image(practice_form)
                PracticeFormMethods.fill_address(practice_form)
                PracticeFormMethods.choose_state(practice_form)
                PracticeFormMethods.choose_city(practice_form)
                PracticeFormMethods.click_on_button(practice_form)
                PracticeFormMethods.check_title(practice_form)
                PracticeFormMethods.click_on_button_close(practice_form)

        except AssertionError as e:
            errors.append(str(e))