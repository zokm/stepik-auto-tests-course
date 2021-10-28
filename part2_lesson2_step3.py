import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    url = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(url)

    number1 = browser.find_element(By.CLASS_NAME, 'nowrap[id="num1"]')
    num1 = number1.text
    number2 = browser.find_element(By.CLASS_NAME, 'nowrap[id="num2"]')
    num2 = number2.text
    # sign = browser.find_element(By.CSS_SELECTOR, '.nowrap:nth-child(3)').text
    s = int(num1) + int(num2)
    select = Select(browser.find_element(By.CSS_SELECTOR, 'select[id="dropdown"]'))
    select.select_by_value(str(s))
    time.sleep(2)

    button = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    button.click()


finally:
    time.sleep(5)
    browser.quit()

