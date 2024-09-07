import time
import allure

from base.pages.select_menu_form.select_menu_page import SelectMenuPage
from py_src.config.expectations import Wait


class SelectMenuMethods:
    def __init__(self):
        self.browser = None

    @staticmethod
    def click_on_value(self: SelectMenuPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Раскрытие выпадающего списка Select Value"):
                self.open_value.on_click()
            with allure.step("Выбор Group 1, option 2"):
                self.page.locator('text=Group 1, option 2').click()
                time.sleep(1)

        except AssertionError as e:
            errors.append(str(e))

    def click_on_one(self: SelectMenuPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Раскрытие выпадающего списка Select One"):
                self.open_one.on_click()
            with allure.step("Выбор Prof."):
                self.page.locator('text=Prof.').click()
                time.sleep(1)

        except AssertionError as e:
            errors.append(str(e))

    def click_on_old(self: SelectMenuPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Раскрытие выпадающего списка Old Style Select Menu"):
                self.open_old.select_option(value='4')
                time.sleep(1)

        except AssertionError as e:
            errors.append(str(e))

    def click_on_multiselect(self: SelectMenuPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Раскрытие выпадающего Multiselect"):
                self.open_multiselect.click()
                time.sleep(1)

            with allure.step("Выбор цвета Black"):
                self.page.locator('#react-select-4-option-2').click()
                time.sleep(1)

        except AssertionError as e:
            errors.append(str(e))

    def click_on_car(self: SelectMenuPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Выбор значения Audi"):
                self.choose_car.click()
                time.sleep(1)

        except AssertionError as e:
            errors.append(str(e))