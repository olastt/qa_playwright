import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# Инициализация веб-драйвера
driver = webdriver.Chrome()

# Переход на сайт
driver.get('https://demoqa.com/')
driver.maximize_window()

# Нахождение и клик по первой карточке
search_elements = driver.find_element(By.XPATH, "(//div[@class='card mt-4 top-card'])[1]")
search_elements.click()

search_web_tables = driver.find_element(By.XPATH, "//span[text()='Web Tables']")
search_web_tables.click()

input_text = driver.find_element(By.XPATH, "//input[@class='form-control']")
input_text.send_keys('Cierra')
time.sleep(1)
input_text.send_keys(Keys.CONTROL + 'a')
input_text.send_keys(Keys.BACKSPACE)

search_add_button = driver.find_element(By.XPATH, "//button[@id='addNewRecordButton']")
search_add_button.click()

driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys('Олеся')
driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys('Астраханцева')
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys('test@mail.ru')
driver.find_element(By.XPATH, "//input[@id='age']").send_keys('27')
driver.find_element(By.XPATH, "//input[@id='salary']").send_keys('100')
driver.find_element(By.XPATH, "//input[@id='department']").send_keys('QA')
time.sleep(1)
driver.find_element(By.XPATH, "//button[text()='Submit']").click()

record_text = driver.find_element(By.XPATH, "//div[text()='Олеся']")
assert record_text is not None, 'ОШИБКА: Новая запись не найдена в таблице'
print('Запись успешно найдена в таблице')

time.sleep(2)  # Добавлено время ожидания, чтобы увидеть результат перед закрытием
driver.close()
