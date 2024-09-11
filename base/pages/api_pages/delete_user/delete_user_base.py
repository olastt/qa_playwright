import requests
import allure

from settings import Settings


class DeleteUserBase:
    def __init__(self):
        self.base_url = Settings().base_url

    def get_delete_user_endpoint(self):
        """
        Возвращает полный URL для выполнения DELETE-запроса удаления данных пользователя.
        """
        return f"{self.base_url}/Account/v1/User"

    @allure.step("Удаление данных пользователя с помощью userId и token")
    def delete_user_data(user_id: str, token: str):
        """
        Отправляет DELETE запрос на /Account/v1/User на указанный URL с предоставленными данными и возвращает ответ сервера
        Удаляет данные пользователя по его userId и token

        :param user_id: ID пользователя
        :param token: Токен авторизации
        :return: Объект ответа от сервера
        """
        base_url = Settings().base_url
        url = f"{base_url}/Account/v1/User/{user_id}"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {token}"
        }

        allure.attach(url, name="Request URL", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(headers), name="Request Headers", attachment_type=allure.attachment_type.JSON)

        # Отправляем DELETE-запрос
        response = requests.delete(url, headers=headers)

        # allure.attach(response.text or "No Content", name="Response Body", attachment_type=allure.attachment_type.JSON)
        return response
