import allure
from base.pages.api_pages.registration.registration_base import RegistrationBase


class RegistrationMethods:
    @staticmethod
    @allure.step("Регистрация пользователя через POST /Account/v1/User")
    def post_v1_account_registration():
        auth_base = RegistrationBase(username="Олеся123321", password="Someon123321!")

        with allure.step("Формирование данных и отправка запроса"):
            data, url = auth_base.form_request_data(auth_base.get_registration_endpoint())
            response = auth_base.send_post_request(data, url)

        with allure.step("Валидация ответа"):
            auth_base.validate_response(response, auth_base.validate_success_response)
