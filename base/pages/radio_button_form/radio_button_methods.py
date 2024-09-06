import time

import allure
from playwright.sync_api import expect

from base.pages.radio_button.radio_button_page import RadioButtonPage
from py_src.config.expectations import Wait


class RadioButtonMethods:
    def __init__(self):
        self.browser = None

    @staticmethod
    def click_on_yes(self: RadioButtonPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Выбор радио кнопки Yes"):
                self.click_on_yes.on_click()

            with allure.step("Проверка что радио кнопка выбрана"):
                if self.is_yes_radio_selected():
                    print("Радиокнопка 'Yes' выбрана")
                else:
                    print("Ошибка: Радиокнопка 'Yes' не выбрана")
        except AssertionError as e:
            errors.append(str(e))

    def click_on_impressive(self: RadioButtonPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Выбор радио кнопки Impressive"):
                self.click_on_impressive.on_click()

            with allure.step("Проверка что радио кнопка выбрана"):
                if self.is_impressive_radio_selected():
                    print("Радиокнопка 'Impressive' выбрана")
                else:
                    print("Ошибка: Радиокнопка 'Impressive' не выбрана")
        except AssertionError as e:
            errors.append(str(e))
