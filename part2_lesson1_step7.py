import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

try:

    url = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(url)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    box = browser.find_element(By.ID, 'treasure')
    tag_valuex = box.get_attribute('valuex')
    value_for_writen = calc(tag_valuex)
    time.sleep(2)

    write_number = browser.find_element(By.ID, 'answer')
    write_number.send_keys(value_for_writen)
    time.sleep(2)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    time.sleep(2)

    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()
    time.sleep(2)

    button = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    button.click()




finally:
    time.sleep(6)
    browser.quit()

