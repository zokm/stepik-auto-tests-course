from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    url = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(url)

    button = browser.find_element(By.CLASS_NAME, 'trollface.btn')
    button.click()

    # пеерключение на новую вкладку
    window_2 = browser.window_handles[1]
    browser.switch_to.window(window_2)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    number = browser.find_element(By.ID, 'input_value').text
    number_input = calc(number)

    row_input = browser.find_element(By.ID, 'answer')
    row_input.send_keys(number_input)

    submit = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    submit.click()


finally:
    time.sleep(3)
    browser.quit()
