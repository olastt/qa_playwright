import allure
from base.pages.api_pages.authorized.methods_v1_authorized import MethodsAuthorized
from base.pages.api_pages.get_user.get_user_base import GetUserBase
from base.pages.api_pages.get_user.get_user_base import GetUserBase
from base.pages.api_pages.get_user.methods_get_user import MethodsGetUser
from base.pages.api_pages.registration.methods_v1_registration import RegistrationMethods


class TestUserV1Account:
    @allure.epic('API')
    @allure.title('Регистрация v1 и получение данных пользователя')
    def test_registration_v1_account_2(self):
        """
        Тест для проверки регистрации пользователя через эндпоинт /Account/v1/Register.

        Этот тест выполняет следующие шаги:
        - Вызывает метод `post_v1_account_registration` из класса `RegistrationMethods`, который:
        - Формирует данные для регистрации.
        - Отправляет POST-запрос на сервер.
        - Валидирует ответ сервера на успешность регистрации.

        Результаты теста записываются в отчет Allure.
        """
        RegistrationMethods.post_v1_account_registration()

    @staticmethod
    @allure.epic('API')
    @allure.title('Получение токена и запрос на получение пользователя по его userId и token')
    def test_get_token():
        """
        Тест для проверки генерации токена пользователя.

        Этот тест выполняет следующие шаги:
        1. Вызывает метод `post_token_authorized` и получает токен.
        2. Использует токен для получения данных пользователя через `get_v1_account_user`.

        Результаты теста записываются в отчет Allure.
        """
        # Получаем токен
        token = MethodsAuthorized.post_token_authorized()
        #
        # # Убедитесь, что токен не равен None
        # assert token is not None, "Не удалось получить токен"

        # Используем userId, который сохранили в RegistrationMethods
        user_id = RegistrationMethods.user_id
        # assert user_id is not None, "userID не был сохранен после регистрации"

        # Создаем экземпляр класса GetUserBase с базовым URL
        get_user_base = GetUserBase()

        # Получаем данные пользователя
        response = get_user_base.get_user_data(user_id, token)

        # Проверяем статус код ответа
        assert response.status_code == 200, f"Не удалось получить данные пользователя, статус код: {response.status_code}, тело ответа: {response.text}"
