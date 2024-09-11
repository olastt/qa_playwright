import allure
from base.pages.api_pages.registration.registration_base import RegistrationBase


class RegistrationMethods:
    # это переменная для хранения айди
    user_id = None

    @staticmethod
    @allure.step("Регистрация пользователя через POST /Account/v1/User")
    def post_v1_account_registration():
        """
        Метод для регистрации пользователя через POST-запрос на эндпоинт /Account/v1/User

        Этот метод используется для регистрации пользователя, используя предоставленные имя пользователя и пароль.
        В процессе выполнения метода происходит несколько шагов:

        1. Создается экземпляр класса `RegistrationBase`, где задаются параметры регистрации (имя пользователя и пароль).
        2. Формируются данные для запроса и полный URL для генерации токена.
        3. Выполняется отправка POST-запроса на сервер с предоставленными данными.
        4. Выполняется валидация ответа сервера, проверяется успешность генерации токена.

        В случае успешного получения токена, результат валидации добавляется в отчет Allure и выводится в консоль,
        включая сгенерированный токен. Если запрос на генерацию токена не удался, тест завершится с ошибкой, и информация
        об этом также будет включена в отчет Allure.

        """

        registration_base = RegistrationBase(username="Тестик123321", password="Sometest123321!")

        with allure.step("Формирование данных и отправка запроса"):
            data, url = registration_base.form_request_data(registration_base.get_registration_endpoint())
            response = registration_base.send_post_request(data, url)

        with allure.step("Валидация ответа"):
            registration_base.validate_response(response, registration_base.validate_success_response)

        # Сохраняем userID из ответа и на всякий случай выводим его на печать
        RegistrationMethods.user_id = response.json().get("userID")
        allure.attach(RegistrationMethods.user_id, name="userID", attachment_type=allure.attachment_type.TEXT)
        print(f"UserID сохранен: {RegistrationMethods.user_id}")
