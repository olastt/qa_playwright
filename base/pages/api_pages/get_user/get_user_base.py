import requests
import allure

from settings import Settings


class GetUserBase:
    def __init__(self):
        self.base_url = Settings().base_url

    def get_user_endpoint(self):
        """
        Возвращает полный URL для выполнения GET-запроса получения данных пользователя.
        """
        return f"{self.base_url}/Account/v1/User"

    @allure.step("Получение данных пользователя с помощью userId и token")
    def get_user_data(self, user_id: str, token: str):
        """
        Отправляет GET запрос на /Account/v1/User на указанный URL с предоставленными данными и возвращает ответ сервера.
        Получаем данные пользователя по его userId и token.

        :param user_id: ID пользователя.
        :param token: Токен авторизации.
        :return: Объект ответа от сервера.
        """
        url = f"{self.base_url}/Account/v1/User/{user_id}"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {token}"
        }

        # Добавление информации в Allure
        allure.attach(url, name="Request URL", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(headers), name="Request Headers", attachment_type=allure.attachment_type.JSON)

        # Получаем ответ
        response = requests.get(url, headers=headers)

        # Из ответа получаем тело
        body = response.json()

        # Теперь сохраняем тело ответа в отчет Allure
        allure.attach(str(body), name="Response Body", attachment_type=allure.attachment_type.JSON)

        return response
