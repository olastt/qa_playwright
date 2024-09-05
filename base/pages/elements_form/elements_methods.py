import time
from pstats import Stats
import base.base

import allure

from base.pages.elements_form.elements_page import ElementsPage
from py_src.config.expectations import Wait


class ElementsMethods:

    def __init__(self):
        self.browser = None

    @staticmethod
    def fill_name_input(self: ElementsPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Ввод имени"):
                self.full_name.fill("Олеся")

        except AssertionError as e:
            errors.append(str(e))

    def fill_email(self: ElementsPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Ввод почты"):
                self.email.fill("olaaa@gmail.com")

        except AssertionError as e:
            errors.append(str(e))

    def fill_current_adress(self: ElementsPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Ввод текущего адреса"):
                self.current_adress.fill("Краснодар, ул. Северная, 100")

        except AssertionError as e:
            errors.append(str(e))

    def fill_permanent_adress(self: ElementsPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Ввод постоянного адреса"):
                self.permanent_adress.fill("Краснодар, ул. Калинина, 205")

        except AssertionError as e:
            errors.append(str(e))

    def submit_button(self: ElementsPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Нажатие на кнопку отправки"):
                self.submit_button.click()

        except AssertionError as e:
            errors.append(str(e))
