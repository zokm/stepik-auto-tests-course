import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    # Дожидаемся, когда цена дома уменьшится до $100 и нажимаем на кнопку
    button = browser.find_element(By.ID, 'book')
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button.click()

    # берем число, решаем математическое действие и нажимем на кнопку
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    number = browser.find_element(By.ID, 'input_value').text
    number_input = calc(number)
    row_input = browser.find_element(By.CLASS_NAME, 'form-control')
    row_input.send_keys(number_input)

    # нажимаем Submit
    button = browser.find_element(By.ID, 'solve')
    button.click()

finally:
    time.sleep(4)
    browser.quit()
