import allure

from playwright.sync_api import Page
from base.pages.data_picker_form.data_picker_page import DataPickerPage
from base.pages.data_picker_form.data_picker_start import DataPickerStart

from conftest import data_picker_form


class TestDownloadAndUploadForm:
    @allure.epic("Тесты потока 1")
    @allure.feature("Date Picker")
    @allure.title("Выбор даты, месяца, года, времени")
    def test_download_and_upload_form(self, page: Page, data_picker_form: DataPickerPage):
        DataPickerStart.data_picker_start(page, data_picker_form)
