import time

import allure
from playwright.sync_api import expect

from base.pages.modal_form.modal_page import ModalPage
from py_src.config.expectations import Wait


class ModalMethods:
    def __init__(self):
        self.browser = None

    @staticmethod
    def click_on_small_modal(self: ModalPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Открытие модального окна"):
                self.open_small_modal.on_click()

        except AssertionError as e:
            errors.append(str(e))

    def close_on_small_modal(self: ModalPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Нажатие на кнопку закрытия модального окна"):
                self.close_small_modal.on_click()

        except AssertionError as e:
            errors.append(str(e))

    def check_text_small(self: ModalPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Проверка текста в модальном окне"):
                element_locator = self.page.locator('//*[@class="modal-body"]')

                # Получаем текст
                actual_text = element_locator.inner_text()
                expected_text = 'This is a small modal. It has very less content'

                if actual_text != expected_text:
                    print(f"Ожидаемый заголовок: '{expected_text}', но получен: '{actual_text}'")

        except AssertionError as e:
            errors.append(str(e))

    def click_on_lagre_modal(self: ModalPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Открытие модального окна"):
                self.open_lagre_modal.on_click()

        except AssertionError as e:
            errors.append(str(e))

    def close_on_lagre_modal(self: ModalPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Нажатие на кнопку закрытия модального окна"):
                self.close_lagre_modal.on_click()

        except AssertionError as e:
            errors.append(str(e))

    def check_text_large(self: ModalPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Проверка текста в модальном окне"):
                element_locator = self.page.locator('//*[@class="modal-body"]')

                # Получаем текст
                actual_text = element_locator.inner_text()
                expected_text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry!!!'

                assert actual_text == expected_text, (f"Ожидаемый текст: '{expected_text}', "
                                                      f"но получен: '{actual_text}'")

        except AssertionError as e:
            errors.append(str(e))

