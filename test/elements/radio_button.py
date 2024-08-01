import time
import pytest
from selenium.webdriver.common.by import By
from src.Elements import BaseTest
from src.func import find_element, click_element, input_text


class TestDemoQA(BaseTest):
    def test_radio_buttons(self):
        self.setup_method()

        self.open_site(self.url)

        # Нахождение и клик по первой карточке
        click_element(self.driver, By.XPATH, "(//div[@class='card mt-4 top-card'])[1]")

        # Переход в боковое меню Radio Button
        click_element(self.driver, By.XPATH, "//span[text()='Radio Button']")

        # Клик по первой радио кнопке
        click_element(self.driver, By.XPATH, "//label[text()='Yes']")
        time.sleep(1)

        # Клик по второй радио кнопке
        click_element(self.driver, By.XPATH, "//label[text()='Impressive']")
        time.sleep(1)

        self.teardown_method()


#
# if __name__ == "__main__":
#     pytest.main()

test = TestDemoQA()
test.test_radio_buttons()
