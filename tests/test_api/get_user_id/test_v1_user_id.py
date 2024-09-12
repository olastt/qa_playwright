import allure
import pytest

from base.pages.api_pages.authorized.methods_v1_authorized import MethodsAuthorized
from base.pages.api_pages.get_user.get_user_base import GetUserBase
from base.pages.api_pages.registration.methods_v1_registration import RegistrationMethods


@pytest.fixture(scope="module")
def setup_user():
    """
    Фикстура для регистрации пользователя, получения токена и сохранения userId.
    """
    # Регистрация пользователя
    RegistrationMethods.post_v1_account_registration()

    # Получение токена
    token = MethodsAuthorized.post_token_authorized()
    assert token is not None, "Токен не был сгенерирован"

    # Сохранение userId
    user_id = RegistrationMethods.user_id
    assert user_id is not None, "userId не был сохранен"

    return user_id, token


class TestGetUser:
    @staticmethod
    @allure.epic('API')
    @allure.title('Получение токена и запрос на получение пользователя по его userId и token')
    def test_get_token(setup_user):
        """
        Тест для проверки генерации токена пользователя.

        Этот тест выполняет следующие шаги:
        1. Вызывает метод `post_token_authorized` и получает токен.
        2. Использует токен для получения данных пользователя через `get_v1_account_user`.

        Результаты теста записываются в отчет Allure.
        """

        user_id, token = setup_user

        # Создаем экземпляр класса GetUserBase с базовым URL
        get_user_base = GetUserBase()

        # Получаем данные пользователя
        response = get_user_base.get_user_data(user_id, token)

        # Проверяем статус код ответа
        assert response.status_code == 200, f"Не удалось получить данные пользователя, статус код: {response.status_code}, тело ответа: {response.text}"
