import time
from pstats import Stats

import allure

from base.pages.practice_form.practice_form_page import PracticeFormPage
from py_src.config.expectations import Wait


class PracticeFormMethods:

    @staticmethod
    def fill_name_input(practice_form: PracticeFormPage):
        errors = []
        Wait.set_page(practice_form.page)

        try:
            with allure.step("Ввод имени и фамилии"):
                practice_form.first_name.fill("Олеся")
                practice_form.last_name.fill("Астраханцева")

        except AssertionError as e:
            errors.append(str(e))

    def fill_email_input(self: PracticeFormPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Ввод почты пользователя"):
                self.email.fill("test@mail.ru")

        except AssertionError as e:
            errors.append(str(e))

    def click_gender(self: PracticeFormPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Выбор радио кнопки пола"):
                self.gender.click()

        except AssertionError as e:
            errors.append(str(e))

    def fill_number_input(self: PracticeFormPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Ввод номера телефона"):
                self.number.fill("9181111111")

        except AssertionError as e:
            errors.append(str(e))

    def click_date_birth(self: PracticeFormPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Клик по полю выбора даты"):
                self.drop_calendar.on_click()
            with allure.step("Выбор месяца Июль"):
                self.choose_month.select_option(value='6')
            with allure.step("Выбор года 1997"):
                self.choose_year.select_option(value='1997')
            with allure.step("Выбор дня - 2 число"):
                self.choose_day.on_click()
                time.sleep(1)

        except AssertionError as e:
            errors.append(str(e))

    def fill_subject_input(self: PracticeFormPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Заполнение предметов"):
                self.subject.fill(
                    "История, Математика, Английский язык, Информатика, Литература, Русский язык")
                time.sleep(1)

        except AssertionError as e:
            errors.append(str(e))

    def choose_hobbies(self: PracticeFormPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Выбор хобби"):
                self.hobbies.on_click()

        except AssertionError as e:
            errors.append(str(e))

    def upload_image(self: PracticeFormPage):
        errors = []
        Wait.set_page(self.page)

        image_path = 'py_src/img/image-1_A8qEAeU.jpg'

        with allure.step(f'Загрузка изображения "{image_path}" в элемент {self.upload}'):
            # Ищем наш элемент с помощью локатора
            file = self.page.locator(self.upload.locator)
            # Добавляем изображение для загрузки
            file.set_input_files(str(image_path))

    def fill_address(self: PracticeFormPage):
        errors = []
        Wait.set_page(self.page)

        with allure.step("Заполнение адреса"):
            self.address.fill("г. Краснодар, ул. Северная")

    def fill_city(self: PracticeFormPage):
        errors = []
        Wait.set_page(self.page)

        with allure.step("Выбор города"):
            self.city.on_click()

