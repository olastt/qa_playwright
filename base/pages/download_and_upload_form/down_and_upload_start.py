import allure
from playwright.sync_api import Page

from base.pages.download_and_upload_form.down_and_upload_methods import DownloadAndUploadMethods
from base.pages.download_and_upload_form.down_and_upload_page import DownAndUploadPage
from base.pages.authorization.authorization_method import AuthorizationMethod


class DownloadAndUploadStart:

    @staticmethod
    def download_and_upload_start(page: Page, download_and_upload_form: DownAndUploadPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.auth_download_and_upload_form(page)

            with allure.step("Скачивание и загрузка файлов"):
                DownloadAndUploadMethods.click_download_button(download_and_upload_form)

            with allure.step("Проверка что файл загружен"):
                DownloadAndUploadMethods.upload_img(download_and_upload_form)

        except AssertionError as e:
            errors.append(str(e))
