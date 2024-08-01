from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def find_element(driver: WebDriver, by: By, value: str):
    return driver.find_element(by, value)


def click_element(driver: WebDriver, by: By, value: str):
    element = find_element(driver, by, value)
    element.click()


def input_text(driver: WebDriver, by: By, value: str, text: str):
    element = find_element(driver, by, value)
    element.send_keys(text)


def double_click_element(driver: WebDriver, by: By, value: str):
    action = ActionChains(driver)
    element = find_element(driver, by, value)
    action.double_click(element).perform()


def right_click_element(driver: WebDriver, by: By, value: str):
    action = ActionChains(driver)
    element = find_element(driver, by, value)
    action.context_click(element).perform()
