from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    url = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(url)

    button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    button.click()


    # переключаемся на конфирм и нажимаем ок


    def confirm():
        conf = browser.switch_to.alert
        conf.accept()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    def job_with_number():
        number_text = browser.find_element(By.ID, 'input_value').text
        number_for_input = calc(number_text)
        row_input = browser.find_element(By.ID, 'answer')
        row_input.send_keys(number_for_input)
        submit = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
        submit.click()

    confirm()
    job_with_number()

finally:
    time.sleep(3)
    browser.quit()
