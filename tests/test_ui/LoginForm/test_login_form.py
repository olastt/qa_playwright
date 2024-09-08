import allure

from playwright.sync_api import Page
from base.pages.login_form.login_page import LoginPage
from base.pages.login_form.login_start import LoginStart
from conftest import login_form


class TestLoginForm:
    @allure.epic("Тесты потока 1")
    @allure.feature("Login")
    @allure.title("Авторизация пользователя")
    def test_login_form(self, page: Page, login_form: LoginPage):
        LoginStart.login_start(page, login_form)
