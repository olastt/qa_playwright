import allure

from playwright.sync_api import Page
from base.pages.download_and_upload_form.down_and_upload_page import DownAndUploadPage
from base.pages.download_and_upload_form.down_and_upload_start import DownloadAndUploadStart

from conftest import download_and_upload_form


class TestDownloadAndUploadForm:
    @allure.epic("Тесты потока 1")
    @allure.feature("Upload and Download")
    @allure.title("Скачивание и загрузка файлов")
    def test_download_and_upload_form(self, page: Page, download_and_upload_form: DownAndUploadPage):
        DownloadAndUploadStart.download_and_upload_start(page, download_and_upload_form)
