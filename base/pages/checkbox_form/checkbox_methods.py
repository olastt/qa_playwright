import time
import allure

from base.pages.checkbox_form.checkbox_page import CheckboxPage
from py_src.config.expectations import Wait


class CheckboxMethods:
    def __init__(self):
        self.browser = None

    @staticmethod
    def click_on_home(self: CheckboxPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Раскрытие списка Home"):
                self.home.on_click()

        except AssertionError as e:
            errors.append(str(e))

    def click_on_desktop(self: CheckboxPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Раскрытие папки Desktop"):
                self.desktop.on_click()

        except AssertionError as e:
            errors.append(str(e))

    def click_on_documents(self: CheckboxPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Раскрытие папки Documents"):
                self.documents.on_click()

        except AssertionError as e:
            errors.append(str(e))

    def click_on_downloads(self: CheckboxPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Раскрытие папки Downloads"):
                self.downloads.on_click()

        except AssertionError as e:
            errors.append(str(e))

    def choose_desktop(self: CheckboxPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Выбор папки Desktop"):
                self.choose_desktop.on_click()

        except AssertionError as e:
            errors.append(str(e))

    def choose_documents(self: CheckboxPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Выбор папки Documents"):
                self.choose_documents.on_click()

        except AssertionError as e:
            errors.append(str(e))

    def choose_downloads(self: CheckboxPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Выбор папки Downloads"):
                self.choose_downloads.on_click()

        except AssertionError as e:
            errors.append(str(e))

    def choose_close_all(self: CheckboxPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Закрытие выпадающего списка посредством нажатия на кнопку минуса"):
                self.close_all.on_click()

        except AssertionError as e:
            errors.append(str(e))

    def choose_all(self: CheckboxPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Раскрытие выпадающего списка посредством нажатия на кнопку плюса"):
                self.choose_all.on_click()

        except AssertionError as e:
            errors.append(str(e))

