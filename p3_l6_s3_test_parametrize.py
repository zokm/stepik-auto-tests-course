import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_answer(browser, link):
    input_result = math.log(int(time.time()))
    url = f"https://stepik.org/lesson/{link}/step/1/"
    browser.get(url)
    browser.implicitly_wait(10)
    field_for_input = browser.find_element(By.TAG_NAME, 'textarea')
    field_for_input.send_keys(input_result)
    button = browser.find_element(By.CLASS_NAME, 'submit-submission')
    button.click()

    feedback = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text

    assert feedback == 'Correct!', 'Isn\'t correct'
