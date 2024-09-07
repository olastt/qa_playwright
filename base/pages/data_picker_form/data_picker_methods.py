import time
import allure

from base.pages.data_picker_form.data_picker_page import DataPickerPage
from py_src.config.expectations import Wait


class DataPickerMethods:
    def __init__(self):
        self.browser = None

    @staticmethod
    def click_on_calendar(self: DataPickerPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Открытие дата пикера"):
                self.select_calendar.on_click()
            with allure.step("Выбор месяца - июль"):
                self.choose_month.select_option(value='6')
            with allure.step("Выбор года - 1997"):
                self.choose_year.select_option(value='1997')
                time.sleep(1)
            with allure.step("Выбор дня - 2 число"):
                self.choose_day.on_click()

        except AssertionError as e:
            errors.append(str(e))

    def click_on_second_calendar(self: DataPickerPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Открытие дата пикера"):
                self.select_second_calendar.click()

            with allure.step("Выбор месяца - февраль"):
                self.choose_second_month.on_click()
                self.page.locator('text=February').click()
                time.sleep(1)

            with allure.step("Выбор года - 1998"):
                self.choose_second_year.on_click()

                # здесь пришлось сделать два цикла, ибо первый локатор сбивается, доходя до 2015 года
                for i in range(6):
                    self.click_to_year.click()
                for i in range(15):
                    self.page.locator('(//*[@class="react-datepicker__year-option"])[13]').click()

                self.page.locator('text=1998').click()
                time.sleep(1)

            with allure.step("Выбор дня - 15"):
                self.choose_second_day.on_click()
                time.sleep(1)

            with allure.step("Выбор времени - 09:30"):
                # выбираем элемент нужного времени
                time_element = self.page.locator('(//*[@class="react-datepicker__time-list-item "])[40]')

                # скролл к элементу
                time_element.scroll_into_view_if_needed()
                time_element.click()
                time.sleep(1)

        except AssertionError as e:
            errors.append(str(e))
