import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

try:
    url = 'http://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(url)
    number = browser.find_element(By.CLASS_NAME, 'nowrap[id="input_value"]')
    num = number.text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    number_for_input = calc(num)
    row = browser.find_element(By.ID, 'answer')
    row.send_keys(number_for_input)

    # скроллим страницу вниз
    browser.execute_script('window.scrollBy(0,150)')

    # Выбрать checkbox "I'm the robot"
    checkbox = browser.find_element(By.CLASS_NAME, 'form-check-input[id="robotCheckbox"]')
    checkbox.click()

    # Переключить radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.CLASS_NAME, 'form-check-input[id="robotsRule"]')
    radiobutton.click()

    # Нажать на кнопку "Submit"
    submit = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    submit.click()

finally:
    time.sleep(3)
    browser.quit()
