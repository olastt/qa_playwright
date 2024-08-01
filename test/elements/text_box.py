import time
import pytest
from selenium.webdriver.common.by import By
from src.Elements import BaseTest
from src.func import find_element, click_element, input_text


class DemoTest(BaseTest):
    def test_text_box(self):
        self.setup_method()
        self.open_site(self.url)

        # Нахождение и клик по первой карточке
        click_element(self.driver, By.XPATH, "(//div[@class='card mt-4 top-card'])[1]")

        # Переход в раздел Text Box
        click_element(self.driver, By.XPATH, "(//span[text()='Text Box')")

        # Заполнение полей
        input_text(self.driver, By.XPATH, "//input[@class=' mr-sm-2 form-control']", 'Олеся')
        input_text(self.driver, By.XPATH, "//input[@class='mr-sm-2 form-control']']", 'test@mail.ru')
        input_text(self.driver, By.XPATH, "//textarea[@id='currentAddress']", 'Россия, Москва')
        input_text(self.driver, By.XPATH, "//textarea[@id='permanentAddress']", 'Россия, Москва')

        # Починить
        submit_button = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()

        get_url = self.driver.current_url
        url = 'https://demoqa.com/text-box'
        assert url == get_url, 'ОШИБКА, URL не совпадают'
        print('URL корректна')

        # Закрытие браузера
        time.sleep(2)  # Добавлено время ожидания, чтобы увидеть результат перед закрытием
        self.teardown_method()
