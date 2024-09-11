import pytest
import allure
from base.pages.api_pages.delete_user.methods_v1_delete_user import MethodsDeleteUser
from base.pages.api_pages.authorized.methods_v1_authorized import MethodsAuthorized
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


class TestUserV1AccountDelete:

    @staticmethod
    @allure.epic('API')
    @allure.title('Удаление пользователя по его userId и token')
    def test_delete_user(setup_user):
        """
        Тест для проверки удаления пользователя через эндпоинт /Account/v1/User/{user_id}.

        Этот тест:
        1. Использует сохраненные userId и token, полученные при регистрации и авторизации.
        2. Вызывает метод для удаления пользователя через DELETE-запрос.
        3. Проверяет успешность удаления (статус код 204).

        Результаты теста записываются в отчет Allure.
        """
        user_id, token = setup_user

        # Вызываем метод для удаления пользователя
        response = MethodsDeleteUser.delete_v1_user_account(user_id, token)

        # Проверяем статус код ответа
        assert response.status_code == 204, (f"Не удалось удалить пользователя, статус код: {response.status_code}, "
                                             f"тело ответа: {response.text}")
