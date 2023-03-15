import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который заполняет обязательные поля
    forms_1 = browser.find_element(By.CSS_SELECTOR, "div.form-group.first_class > label + input")

    forms_1.send_keys('1')
    forms_2 = browser.find_element(By.CSS_SELECTOR, "// input[ @ placeholder = 'Input your last name']")

    forms_2.send_keys('2')
    forms_3 = browser.find_element(By.CSS_SELECTOR, "// input[ @ placeholder = 'Input your email']")
    forms_3.send_keys('3')

    # Отправляем заполненную форму

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
except:
    raise NoSuchElementException
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()