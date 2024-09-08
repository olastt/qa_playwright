import allure
from playwright.sync_api import Page

from base.pages.login_form.login_page import LoginPage
from base.pages.login_form.login_methods import LoginMethods
from base.pages.authorization.authorization_method import AuthorizationMethod


class LoginStart:
    @staticmethod
    def login_start(page: Page, login_form: LoginPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.auth_login_form(page)

            with allure.step("Ввод данных пользователя"):
                LoginMethods.name(login_form)
                LoginMethods.password(login_form)
                LoginMethods.click_on_login(login_form)

        except AssertionError as e:
            errors.append(str(e))
