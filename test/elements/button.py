from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
import time
import pytest
import time
import pytest
from selenium.webdriver.common.by import By
from src.Elements import BaseTest
from src.func import find_element, click_element, input_text, double_click_element, right_click_element


class DemoTest(BaseTest):
    url = 'https://demoqa.com/'  # Переменная с URL для открытия сайта

    def test_button(self):
        self.setup_method()
        self.open_site(self.url)

        # Нахождение и клик по первой карточке
        click_element(self.driver, By.XPATH, "(//div[@class='card mt-4 top-card'])[1]")

        # Переход в раздел Buttons
        click_element(self.driver, By.XPATH, "//span[text()='Buttons']")

        # Двойной клик по кнопке
        double_click_element(self.driver, By.XPATH, "//button[@id='doubleClickBtn']")
        print('Произвели двойной клик')

        # Клик правой кнопкой
        right_click_element(self.driver, By.XPATH, "//button[@id='rightClickBtn']")
        print('Произвели клик правой кнопкой')

        # Закрытие браузера
        time.sleep(2)  # Добавлено время ожидания, чтобы увидеть результат перед закрытием
        self.teardown_method()


te = DemoTest()
te.test_button()
