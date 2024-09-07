import allure
import time

import page

from base.pages.download_and_upload_form.down_and_upload_page import DownAndUploadPage
from py_src.config.expectations import Wait


class DownloadAndUploadMethods:
    def __init__(self):
        self.browser = None

    def click_download_button(self: DownAndUploadPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Нажатие на кнопку скачивания"):
                self.download.on_click()

        except AssertionError as e:
            errors.append(str(e))

    def upload_img(self: DownAndUploadPage):
        errors = []
        Wait.set_page(self.page)

        try:
            image_path = 'py_src/img/test.JPG'

            with allure.step(f'Загрузка изображения "{image_path}" в элемент {self.upload}'):
                # Ищем наш элемент с помощью локатора
                file = self.page.locator(self.upload.locator)
                # Добавляем изображение для загрузки
                file.set_input_files(str(image_path))

        except AssertionError as e:
            errors.append(str(e))

    def check_title(self: DownAndUploadPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Проверка заголовка у таблицы полученных данных"):
                element_locator = self.page.locator('//*[@id="uploadedFilePath"]')

                # Получаем текст
                actual_text = element_locator.inner_text()
                expected_text = 'C:\fakepath\test.JPG'

                if actual_text != expected_text:
                    print(f"Ожидаемый заголовок: '{expected_text}', но получен: '{actual_text}'")

        except AssertionError as e:
            errors.append(str(e))


