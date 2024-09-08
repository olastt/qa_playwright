import time
import allure

from base.pages.login_form.login_page import LoginPage
from py_src.config.expectations import Wait


class LoginMethods:
    def __init__(self):
        self.browser = None

    @staticmethod
    def name(self: LoginPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Ввод имени"):
                self.name.fill('Олеся')

        except AssertionError as e:
            errors.append(str(e))

    def password(self: LoginPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Ввод пароля"):
                self.password.fill('Someone1234!')

        except AssertionError as e:
            errors.append(str(e))

    def click_on_login(self: LoginPage):
        errors = []
        Wait.set_page(self.page)

        try:
            with allure.step("Ввод имени"):
                self.login.click()
                element_locator = self.page.locator('//*[@id="userName-value"]')

                # Получаем текст
                actual_text = element_locator.inner_text()
                expected_text = 'Олеся'

                if actual_text != expected_text:
                    print(f"Ожидаемый текст: '{expected_text}', но получен: '{actual_text}'")

        except AssertionError as e:
            errors.append(str(e))

