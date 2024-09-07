import time
from pstats import Stats
import base.base

import allure

from base.pages.practice_form.practice_form_page import PracticeFormPage
from py_src.config.expectations import Wait


class PracticeFormMethods:

    def __init__(self):
        self.browser = None

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
                self.page.locator('text=Female').click()

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

        except AssertionError as e:
            errors.append(str(e))

    def fill_subject_input(self: PracticeFormPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Заполнение предметов"):
                self.subject.fill("E")
            with allure.step("Выбор англ языка"):
                # Выбираем второй элемент по индексу, ибо он видит два элемента и не знает куда кликать
                self.page.locator('text=English').nth(1).click()

            with allure.step("Заполнение второго предмета"):
                self.subject.fill("C")
            with allure.step("Выбор химии"):
                self.page.locator('text=Chemistry').click()

            with allure.step("Заполнение третьего предмета"):
                self.subject.fill("B")
            with allure.step("Выбор биологии"):
                self.page.locator('text=Biology').nth(1).click()

            with allure.step("Заполнение четвертого предмета"):
                self.subject.fill("H")
            with allure.step("Выбор хинди"):
                self.page.locator('text=Hindi').nth(1).click()

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

        try:

            image_path = 'py_src/img/image-1_A8qEAeU.jpg'

            with allure.step(f'Загрузка изображения "{image_path}" в элемент {self.upload}'):
                # Ищем наш элемент с помощью локатора
                file = self.page.locator(self.upload.locator)
                # Добавляем изображение для загрузки
                file.set_input_files(str(image_path))

        except AssertionError as e:
            errors.append(str(e))

    def fill_address(self: PracticeFormPage):
        errors = []
        Wait.set_page(self.page)

        try:

            with allure.step("Заполнение адреса"):
                self.address.fill("г. Краснодар, ул. Северная")

        except AssertionError as e:
            errors.append(str(e))

    def choose_state(self: PracticeFormPage):
        errors = []
        Wait.set_page(self.page)

        try:

            with allure.step("Раскрытие выпадающего списка штатов"):
                self.state_drop.click()
            with allure.step("Выбор штата Haryana"):
                self.page.locator('text=Haryana').click()

        except AssertionError as e:
            errors.append(str(e))

    def choose_city(self: PracticeFormPage):
        errors = []
        Wait.set_page(self.page)

        try:

            with allure.step("Раскрытие выпадающего списка городов"):
                self.city_drop.click()
            with allure.step("Выбор города"):
                self.page.locator('text=Panipat').click()

        except AssertionError as e:
            errors.append(str(e))

    def click_on_button(self: PracticeFormPage):
        errors = []
        Wait.set_page(self.page)

        try:

            with allure.step("Клик по кнопке"):
                self.button.click()

        except AssertionError as e:
            errors.append(str(e))

    def check_title(self: PracticeFormPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Проверка заголовка у таблицы полученных данных"):
                # Ожидаем когда появится заголовок попапа
                header_locator = self.page.locator('//*[@class="modal-header"]')

                # Получаем текст заголовка
                actual_text = header_locator.inner_text()
                expected_text = 'Thanks for submitting the form'

                if actual_text != expected_text:
                    print(f"Ожидаемый заголовок: '{expected_text}', но получен: '{actual_text}'")

        except AssertionError as e:
            errors.append(str(e))

    def click_on_button_close(self: PracticeFormPage):
        errors = []
        Wait.set_page(self.page)

        try:

            with allure.step("Клик по кнопке закрытия попапа"):
                self.button_close.click()

        except AssertionError as e:
            errors.append(str(e))

