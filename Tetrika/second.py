'''Задача №2.
В нашей школе мы не можем разглашать персональные данные пользователей,
но чтобы преподаватель и ученик смогли объяснить нашей поддержке, кого они имеют в виду (у преподавателей, например,
часто учится несколько Саш), мы генерируем пользователям уникальные и легко произносимые имена.
Имя у нас состоит из прилагательного, имени животного и двузначной цифры.
В итоге получается, например, "Перламутровый лосось 77". Для генерации таких имен мы и решали следующую задачу:
Получить с русской википедии список всех животных (https://inlnk.ru/jElywR) и
вывести количество животных на каждую букву алфавита. Результат должен получиться в следующем виде:
А: 642
Б: 412
В:....'''

import requests
from bs4 import BeautifulSoup
# from time import time   #для вывода времени выполнения кода

url = 'https://ru.wikipedia.org/w/index.php?title=Категория%3AЖивотные_по_алфавиту&from=А'
first_page = requests.get(url).text
dict_animals = {}
list_animals = []
abc_cyr = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
abc_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def lets_find(page):
    """Основная функция"""
    # print('|', end='')    #Печать '|' перед обработкой каждой страницы
    soup = BeautifulSoup(page, 'lxml')
    names = soup.find('div', class_='mw-category mw-category-columns').find_all('a')
    for name in names:
        list_animals.append(name.text)
    links = soup.find('div', id='mw-pages').find_all('a')
    link1 = links[1].text
    if link1 == 'Следующая страница':
        url_next = 'https://ru.wikipedia.org/' + links[1].get('href')
        page_next = requests.get(url_next).text
        lets_find(page_next)


def list_to_dict():
    """Конвертация полученного списка в словарь"""
    for animal in list_animals:
        first_letter = animal[0]
        if first_letter in dict_animals:
            dict_animals[first_letter] += 1
        else:
            dict_animals[first_letter] = 1


def print_items_value(dict_input, abc):
    """Вывод пар ключ - значение словаря.
        Если нет животных на какую-то букву, то будет '-' """
    for letter in abc:
        if letter in dict_input:
            print(f"{letter}: {dict_input[letter]}")
        else:
            print(f"{letter}: - ")


# start_time = time()   #стартовое время программы
lets_find(first_page)
# print()   #перевод на новую строку, тк в функции печать с параметром  end=''
list_to_dict()
print_items_value(dict_animals, abc_cyr)
print_items_value(dict_animals, abc_eng)
# print(f'Time for all operations: {time() - start_time}')    #Вывод затраченного времени.
# print(f'Amount of animals {sum(dict_animals.values())}')    #Для вывода общего количества животных.




# ANOTHER WAY with dictionary:


# url = 'https://ru.wikipedia.org/w/index.php?title=Категория%3AЖивотные_по_алфавиту&from=А'
# first_page = requests.get(url).text
# dict_animals = {}
# abc_cyr = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# abc_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
#
# def lets_find(page):
#     # print('.', end='')
#     soup = BeautifulSoup(page, 'lxml')
#     names = soup.find('div', class_='mw-category mw-category-columns').find_all('a')
#     for name in names:
#         first_letter = name.text[0].upper()
#         if first_letter in dict_animals:
#             dict_animals[first_letter] += 1
#         else:
#             dict_animals[first_letter] = 1
#     links = soup.find('div', id='mw-pages').find_all('a')
#     link1 = links[1].text
#
#     if link1 == 'Следующая страница':
#         url_next = 'https://ru.wikipedia.org/' + links[1].get('href')
#         page_next = requests.get(url_next).text
#         lets_find(page_next)
#
#
# def print_items_value(dict_input, abc):
#     for letter in abc:
#         if letter in dict_input:
#             print(f"{letter}: {dict_input[letter]}")
#         else:
#         print(f"{letter}: - ")
#
#
# start_time = time()
# lets_find(first_page)
# # print()
# print_items_value(dict_animals, abc_cyr)
# print_items_value(dict_animals, abc_eng)
# # print(f'Time for all operations: {time() - start_time}')    #Вывод затраченного времени.
# # print(f'Amount of animals {sum(dict_animals.values())}')    #Для вывода общего количества животных.




