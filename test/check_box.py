import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация веб-драйвера
driver = webdriver.Chrome()

# Переход на сайт
driver.get('https://demoqa.com/')
driver.maximize_window()

# Переход в раздел Elements
search_elements = driver.find_element(By.XPATH, "(//div[@class='card mt-4 top-card'])[1]")
search_elements.click()

# Переход в боковое меню Check Box
search_check_box = driver.find_element(By.XPATH, "//span[text()='Check Box']")
search_check_box.click()
time.sleep(1)

# Клик по чекбоксу
click_on_check_box = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']")
click_on_check_box.click()

# Клик по дропдауну
time.sleep(1)
dropdown_check_box = driver.find_element(By.XPATH, "//button[@aria-label='Toggle']")
dropdown_check_box.click()

# Клик по плюсу
time.sleep(1)
click_on_plus = driver.find_element(By.XPATH, "//button[@class='rct-option rct-option-expand-all']")
click_on_plus.click()

# Клик по минусу
time.sleep(1)
click_on_minus = driver.find_element(By.XPATH, "//button[@class='rct-option rct-option-collapse-all']")
click_on_minus.click()


# Закрытие браузера
time.sleep(2)  # Добавлено время ожидания, чтобы увидеть результат перед закрытием
driver.refresh()
driver.close()