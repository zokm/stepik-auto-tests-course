import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

try:
    url = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(url)
    name = browser.find_element(By.CLASS_NAME, 'form-control[name="firstname"]')
    name.send_keys('firstName')

    lastName = browser.find_element(By.CLASS_NAME, 'form-control[name="lastname"]')
    lastName.send_keys('LastName')

    email = browser.find_element(By.CLASS_NAME, 'form-control[name="email"]')
    email.send_keys('email')

    # определяем путь к папке и путь к файлу
    currentDir = os.path.abspath(os.path.dirname(__file__))
    fileName = 'file.txt'
    filePath = os.path.join(currentDir, fileName)

    # находим кнопку для отправки файла и выполняем отправку
    element = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    element.send_keys(filePath)

    submit = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    submit.click()

finally:
    time.sleep(3)
    browser.quit()
