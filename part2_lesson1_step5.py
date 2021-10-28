from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:

    url = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(url)


    def calc(a):
        return str(math.log(abs(12 * math.sin(int(a)))))

    x_element = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]')
    x = x_element.text
    y = calc(x)
    time.sleep(2)
    
    input_text = browser.find_element(By.CSS_SELECTOR, 'input[id="answer"]')
    input_text.send_keys(y)
    time.sleep(2)

    checkbox = browser.find_element(By.CSS_SELECTOR, '.form-check-custom .form-check-input')
    checkbox.click()
    time.sleep(2)

    radio_robot = browser.find_element(By.CSS_SELECTOR, '.form-radio-custom [id="robotsRule"]')
    radio_robot.click()
    time.sleep(2)

    button_submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
