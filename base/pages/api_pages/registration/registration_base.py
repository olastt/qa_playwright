import allure
import requests
from pydantic import ValidationError

from base.models_api_pydantic.registration.model_registration import RegistrationResponseSuccess, RegistrationResponseError
from settings import Settings


class RegistrationBase:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        self.base_url = Settings().base_url

    def get_registration_endpoint(self):
        return f"{self.base_url}/Account/v1/User"

    @allure.step("Формирование данных для запроса")
    def form_request_data(self, endpoint):
        data = {
            "userName": self.username,
            "password": self.password
        }
        url = endpoint
        allure.attach(
            f"curl -X 'POST' '{url}' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{data}'",
            name="Curl for Postman", attachment_type=allure.attachment_type.TEXT)
        return data, url

    @allure.step("Отправка POST-запроса")
    def send_post_request(self, data, url):
        response = requests.post(url, headers=self.headers, json=data)
        allure.attach(response.text, name="Ответ сервера", attachment_type=allure.attachment_type.JSON)
        allure.attach(response.request.body.decode(), name="Сырой запрос", attachment_type=allure.attachment_type.JSON)
        allure.attach(url, name="URL запроса", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Status Code: {response.status_code}", name="Код статуса",
                      attachment_type=allure.attachment_type.TEXT)
        return response

    @allure.step("Валидация успешного ответа")
    def validate_success_response(self, response):
        response_json = response.json()
        print("Ответ сервера:", response_json)

    @allure.step("Валидация ошибки")
    def validate_error_response(self, response):
        error_response = RegistrationResponseError.model_validate(response.json())
        assert error_response.code == 0, "Ожидался код ошибки '0'"
        assert isinstance(error_response.message, str), "Сообщение об ошибке должно быть строкой"
        print(f"Ошибка: Код - {error_response.code}, Сообщение - {error_response.message}")
        allure.attach(f"Код ошибки: {error_response.code}, Сообщение: {error_response.message}",
                      name="Валидация ошибки", attachment_type=allure.attachment_type.TEXT)

    def validate_response(self, response, success_validator):
        with allure.step("Проверка статуса и валидация ответа"):
            if response.status_code == 201:
                success_validator(response)
                print("Тест успешен: Статус код 201")
            else:
                print(f"Неожиданный статус ответа: {response.status_code}")
                print(f"Ответ сервера: {response.text}")
                allure.attach(response.text, name="Ответ сервера", attachment_type=allure.attachment_type.JSON)
                assert False, f"Неожиданный статус ответа: {response.status_code}"
