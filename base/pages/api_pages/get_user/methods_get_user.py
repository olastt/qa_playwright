import allure
from base.pages.api_pages.get_user.get_user_base import GetUserBase
from base.pages.api_pages.authorized.auth_base import AuthBase


class MethodsGetUser:
    @staticmethod
    @allure.step("Получение токена для пользователя через POST /Account/v1/GenerateToken")
    def post_v1_generate_token():
        auth_base = AuthBase(username="Олеся19971", password="Someone3331!")
        data, url = auth_base.form_request_data(auth_base.get_generate_token_endpoint())
        response = auth_base.send_post_request(data, url)
        auth_base.validate_response(response, auth_base.validate_token_response)
        return response

    @staticmethod
    @allure.step("Получение данных пользователя через GET /Account/v1/User/{userID}")
    def get_v1_account_user(user_id: str, token: str):
        user_base = GetUserBase(username="Олеся123123", password="Someone123123!")
        response = user_base.get_user_data(user_id, token)
        MethodsGetUser.validate_response(response, MethodsGetUser.validate_user_data)

    @staticmethod
    def validate_response(response, success_validator):
        with allure.step("Проверка статуса и валидация ответа"):
            if response.status_code == 200:
                success_validator(response)
                print("Тест успешен: Статус код 200")
            else:
                print(f"Неожиданный статус ответа: {response.status_code}")
                print(f"Ответ сервера: {response.text}")
                allure.attach(response.text, name="Ответ сервера", attachment_type=allure.attachment_type.JSON)
                assert False, f"Неожиданный статус ответа: {response.status_code}"

    @staticmethod
    @allure.step("Валидация данных пользователя")
    def validate_user_data(response):
        try:
            response_json = response.json()
            assert response_json.get("userID"), "userID не найден в ответе"
            assert response_json.get("username"), "username не найден в ответе"
            print("Данные пользователя успешно валидированы.")
        except ValueError as e:
            assert False, f"Ошибка при парсинге JSON: {e}"
