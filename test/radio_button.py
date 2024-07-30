import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация веб-драйвера
driver = webdriver.Chrome()

# Переход на сайт
driver.get('https://demoqa.com/')
driver.maximize_window()

# Нахождение и клик по первой карточке
search_elements = driver.find_element(By.XPATH, "(//div[@class='card mt-4 top-card'])[1]")
search_elements.click()

# Переход в боковое меню Radio Button
search_radio = driver.find_element(By.XPATH, "//span[text()='Radio Button']")
search_radio.click()

# Клик по первой радио кнопке
click_on_button_one = driver.find_element(By.XPATH, "//label[text()='Yes']")
click_on_button_one.click()
time.sleep(1)

# Клик по второй радио кнопке
click_on_button_one = driver.find_element(By.XPATH, "//label[text()='Impressive']")
click_on_button_one.click()
time.sleep(1)

driver.close()