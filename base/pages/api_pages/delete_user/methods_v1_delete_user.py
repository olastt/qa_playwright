import requests
import allure
from settings import Settings


class MethodsDeleteUser:
    @staticmethod
    @allure.step("Удаление пользователя с помощью userId и token")
    def delete_v1_user_account(user_id: str, token: str):
        """
        Выполняет DELETE-запрос на удаление пользователя по его userId.

        :param user_id: ID пользователя.
        :param token: Токен авторизации.
        :return: Объект ответа от сервера.
        """
        base_url = Settings().base_url
        url = f"{base_url}/Account/v1/User/{user_id}"
        headers = {
            "Authorization": f"Bearer {token}",
            "accept": "application/json"
        }

        # # Прикрепляем информацию для отладки
        # allure.attach(url, name="Request URL", attachment_type=allure.attachment_type.TEXT)
        # allure.attach(str(headers), name="Request Headers", attachment_type=allure.attachment_type.JSON)

        # try:
        # Отправка DELETE-запроса
        response = requests.delete(url, headers=headers)

        # Добавление информации в отчет Allure
        allure.attach(response.text, name="Ответ сервера", attachment_type=allure.attachment_type.JSON)
        allure.attach(url, name="URL запроса", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Status Code: {response.status_code}", name="Код статуса",
                      attachment_type=allure.attachment_type.TEXT)
        # allure.attach(str(response.status_code), name="Response Status Code",
        #               attachment_type=allure.attachment_type.TEXT)
        # allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.TEXT)

        return response

        # except requests.RequestException as e:
        #     # Ловим и добавляем исключения в отчет
        #     allure.attach(str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
        #     return None
