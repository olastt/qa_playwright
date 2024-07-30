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

search_text_box = driver.find_element(By.XPATH, "//span[text() = 'Text Box']")
search_text_box.click()

driver.find_element(By.XPATH, "//input[@class=' mr-sm-2 form-control']").send_keys('Олеся')
driver.find_element(By.XPATH, "//input[@class='mr-sm-2 form-control']").send_keys('test@mail.ru')
driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys('Россия, Москва')
driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys('Россия, Москва')

submit_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
driver.execute_script("arguments[0].scrollIntoView();", submit_button)
submit_button.click()


get_url = driver.current_url
url = 'https://demoqa.com/text-box'
assert url == get_url, 'ОШИБКА, URL не совпадают'
print('URL корректна')


# Закрытие браузера
time.sleep(2)  # Добавлено время ожидания, чтобы увидеть результат перед закрытием
driver.close()
