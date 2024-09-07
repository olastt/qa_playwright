import allure
import time
from base.pages.button_form.button_page import ButtonPage
from py_src.config.expectations import Wait


class ButtonMethods:
    def __init__(self):
        self.browser = None

    def double_click(self: ButtonPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Двойное нажатие на кнопку"):
                self.click.double_click()
        except AssertionError as e:
            errors.append(str(e))
            print(f"Ошибка при двойном клике: {e}")

    def right_click(self: ButtonPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Нажатие правой кнопкой на мышке"):
                self.right.right_click(button='right')
        except AssertionError as e:
            errors.append(str(e))

    def simple_click(self: ButtonPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Нажатие кнопкой на мышке"):
                self.simple.on_click()
        except AssertionError as e:
            errors.append(str(e))
            print(f"Ошибка при выполнении простого клика: {e}")
