from playwright.sync_api import Page

from base.base import BasePage
from py_src.config.url import Url


class AuthorizationMethod:

    @staticmethod
    def auth_practice_form(page: Page):
        BasePage.open_page(page, Url.AUTOMATION_PRACTICE_FORM)

    def auth_elements_form(page: Page):
        BasePage.open_page(page, Url.TEXT_BOX)

    def auth_checkbox_form(page: Page):
        BasePage.open_page(page, Url.CHECKBOX)

    def auth_radio_button_form(page: Page):
        BasePage.open_page(page, Url.RADIO_BUTTON)

    def auth_button_form(page: Page):
        BasePage.open_page(page, Url.BUTTONS)

    def auth_download_and_upload_form(page: Page):
        BasePage.open_page(page, Url.UPLOAD_DOWNLOAD)

    def auth_modals_form(page: Page):
        BasePage.open_page(page, Url.MODALS)

    def auth_data_picker_form(page: Page):
        BasePage.open_page(page, Url.DATA_PICKER)

    def auth_select_menu_form(page: Page):
        BasePage.open_page(page, Url.SELECT_MENU)

    def auth_login_form(page: Page):
        BasePage.open_page(page, Url.LOGIN)