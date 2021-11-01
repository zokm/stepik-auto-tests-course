import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_lesson6_step10():
    try:
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element(By.CLASS_NAME, "first_block .first")
        first_name.send_keys("Name")
        last_name = browser.find_element(By.CLASS_NAME, "first_block .second")
        last_name.send_keys("LastName")
        mail = browser.find_element(By.CLASS_NAME, "first_block .third")
        mail.send_keys("Mail")
        time.sleep(1)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert ("Congratulations! You have successfully registered!", welcome_text), "register test # 1 is " \
                                                                                     "failed "

    finally:
        browser.quit()


def test_lesson6_step11():
    try:
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element(By.CLASS_NAME, "first_block .first")
        first_name.send_keys("Name")
        last_name = browser.find_element(By.CLASS_NAME, "first_block .second")
        last_name.send_keys("LastName")
        mail = browser.find_element(By.CLASS_NAME, "first_block .third")
        mail.send_keys("Mail")
        time.sleep(4)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert ("Congratulations! You have successfully registered!",
                welcome_text), "register test # 2 is failed"

    finally:
        browser.quit()


if __name__ == '__main__':
    pytest.main()
