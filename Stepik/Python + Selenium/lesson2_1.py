# Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
# Продолжим использовать силу роботов 🤖 для решения повседневных задач. На данной странице мы добавили капчу для роботов, то есть тест, являющийся простым для компьютера, но сложным для человека.
#
# Ваша программа должна выполнить следующие шаги:
#
# Открыть страницу https://suninjuly.github.io/math.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x (код для этого приведён ниже).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку Submit.
# Для этой задачи вам понадобится использовать атрибут .text для найденного элемента. Обратите внимание, что скобки здесь не нужны:
#
# x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
# x = x_element.text
# y = calc(x)
# Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента. Например, text для данного элемента <div class="message">У вас новое сообщение.</div> вернёт строку: "У вас новое сообщение".
#
# Используйте функцию calc(), которая рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле. Не забудьте добавить этот код в начало вашего скрипта:
#
# import math
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Скопируйте его в поле ниже.


# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# import math
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     link = 'https://suninjuly.github.io/math.html'
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     selector_value = "#input_value"
#     x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
#     x = x_element.text
#     y = calc(x)
#
#     place_for_x = browser.find_element(By.CSS_SELECTOR, "#answer")
#     place_for_x.send_keys(y)
#
#     checkbox = browser.find_element(By.CSS_SELECTOR, "label[for='robotCheckbox']")
#     checkbox.click()
#     radiobutton = browser.find_element(By.CSS_SELECTOR, "label[for='robotsRule']")
#     radiobutton.click()
#     button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
#     button.click()
# finally:
#     time.sleep(10)
#     browser.quit()


# ========================================

# Задание: поиск сокровища с помощью get_attribute
# В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании.
# Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.
#
# Ваша программа должна:
#
# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".
# Для вычисления значения выражения в п.4 используйте функцию calc(x) из предыдущей задачи.
#
#
#
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом.
# Скопируйте его в поле ниже и нажмите кнопку "Submit", чтобы получить баллы за задание.

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()

    prize = browser.find_element(By.CSS_SELECTOR, "#treasure")
    value_x = prize.get_attribute('valuex')

    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(calc(value_x))

    checkbox = browser.find_element(By.XPATH, "/div[1]/form[1]/div[1]/div[1]/div[2]")
    checkbox.click()
    radio = browser.find_element(By.CSS_SELECTOR, "div:nth-child(2)")
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
finally:
    sleep(10)
    browser.quit()






