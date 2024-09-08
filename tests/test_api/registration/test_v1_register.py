import allure

from base.pages.api_pages.registration.methods_v1_registration import RegistrationMethods


class TestRegistrationV1Account:
    """
        Класс, содержащий тесты для проверки регистрации пользователя.

        Тест выполняются с использованием Allure для документирования шагов и результатов.
        """

    @allure.epic('API')
    @allure.title('Регистрация v1')
    def test_registration_v1_account(self):
        """
        Тест для проверки регистрации пользователя через POST-запрос на эндпоинт /Account/v1/User.

        Этот тест выполняет следующие шаги:
        1. Вызывает метод `post_v1_account_registration` из класса `RegistrationMethods`, который:
           - Формирует данные для запроса.
           - Отправляет POST-запрос на сервер для регистрации пользователя.
           - Валидирует ответ сервера, проверяя успешность авторизации.

        Результаты теста записываются в отчет Allure, включая шаги формирования данных, отправки запроса и валидации ответа.
        Если тест проходит успешно, в консоль выводится информация о статусе регистрации. В случае ошибки тест завершится
        с сообщением об ошибке, которое будет включено в отчет Allure.
        """
        RegistrationMethods.post_v1_account_registration()
