# hash функция и хэши обьектов
# если обьекты одинаковые , то и хэш одинаковый . Однако обратно неверно!Если хэш одинаковый, то обьекты могут быть разными
#При этом если кэши разные, то обьекты разные!
# Изменяемы обьекты являются нехешируемыми
# хэш можно использовать как ключи словаря
# print(hash(234234))
# print(hash('python'))
# для чего? поиск ключа в первую очередь осуществяется по хешу(ускорения поиска значений в словаре)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# p1 = Point(1,2)
# p2 = Point(1,2)
# print(hash(p1), hash(p2), sep='\n') #хеши разные, хотя обьекты идентичные
# print(p1 == p2) #False , для этого нужно переопределить магический метод eq


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other): #переопределили магический метод
#         return self.x == other.x and self.y == other.y
#
#     def __hash__(self):
#         return hash((self.x, self.y)) # хэш от кортежа координат
#
#
# p1 = Point(1,2)
# p2 = Point(1,2)
# # print(hash(p1), hash(p2), sep='\n') #TypeError: unhashable type: 'Point' если не переопределить __hash__
# # print(p1 == p2) #False если не переопределен метод eq
#
# d = {}
# d[p1] = 1
# d[p2] = 2
# print(d) #{<__main__.Point object at 0x10f273c10>: 2}  говорит о том, что обьекты p1 и p2 воспринимаются как идентичные из-за eq и hash
#


# =========================================================================================================


# Подвиг 4. Объявите в программе класс с именем Rect (прямоугольник), объекты которого создаются командой:
# rect = Rect(x, y, width, height)
# где x, y - координата верхнего левого угла (числа: целые или вещественные); width, height -
# ширина и высота прямоугольника (числа: целые или вещественные).
# В этом классе определите магический метод, чтобы хэши объектов класса Rect с равными width, height были равны. Например
# r1 = Rect(10, 5, 100, 50)
# r2 = Rect(-10, 4, 100, 50)
# h1, h2 = hash(r1), hash(r2)   # h1 == h2
# P.S. На экран ничего выводить не нужно, только объявить класс.

# class Rect:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def __eq__(self, other):
#         return self.width == other.width and self.height == other.height
#
#     def __hash__(self):
#         return hash((self.width, self.height))


# ===================================================================================================




# Подвиг 6. Объявите класс с именем ShopItem (товар), объекты которого создаются командой:
# item = ShopItem(name, weight, price)
# где name - название товара (строка); weight - вес товара (число: целое или вещественное); price - цена товара (число: целое или вещественное).
# Определите в этом классе магические методы:
# __hash__() - чтобы товары с одинаковым названием (без учета регистра), весом и ценой имели бы равные хэши;
# __eq__() - чтобы объекты с одинаковыми хэшами были равны.
# Затем, из входного потока прочитайте строки командой:
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# Строки имеют следующий формат:
# название товара 1: вес_1 цена_1
# ...
# название товара N: вес_N цена_N
# Например:
# Системный блок: 1500 75890.56
# Монитор Samsung: 2000 34000
# Клавиатура: 200.44 545
# Монитор Samsung: 2000 34000
# Как видите, товары в этом списке могут совпадать.
# Необходимо для всех этих строчек сформировать соответствующие объекты класса ShopItem и добавить в словарь с именем shop_items.
# Ключами словаря должны выступать сами объекты, а значениями - список в формате:
# [item, total]
# где item - объект класса ShopItem; total - общее количество одинаковых объектов (с одинаковыми хэшами). Подумайте,
# как эффективно программно наполнять такой словарь, проходя по списку lst_in один раз.
# P.S. На экран ничего выводить не нужно, только объявить класс и сформировать словарь.
# Sample Input:
# Системный блок: 1500 75890.56
# Монитор Samsung: 2000 34000
# Клавиатура: 200.44 545
# Монитор Samsung: 2000 34000
# Sample Output:
#
import sys


# class ShopItem:
#     def __init__(self, name, weight, price):
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def __eq__(self, other):
#         return self.name == other.name and self.weight == other.weight and self.price == other.price
#
#     def __hash__(self):
#         return hash((self.name.lower(), self.weight, self.price))
#
# # lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = ['Системный блок: 1500 75890.56', 'Монитор Samsung: 2000 34000', 'Клавиатура: 200.44 545', 'Монитор Samsung: 2000 34000']
# shop_items = {}
# for i in lst_in:
#     data = i.split(': ')
#     name = data[0]
#     weight, price = data[1].split()
#     obj = ShopItem(name, weight, price)
#     if obj not in shop_items:
#         shop_items[obj] = [obj, 1]
#     else:
#         shop_items[obj][1] += 1
# print(shop_items)

# ---------------------------
# another way for dict
# for item in lst_in:
#     name, weight, price = item.rsplit(maxsplit=2)
#     obj = ShopItem(name[:-1], weight, price)
#     shop_items.setdefault(obj, [obj, 0])[1] += 1
#
# # ------------------------

# tests
# it1 = ShopItem('name', 10, 11)
# it2 = ShopItem('name', 10, 11)
# assert hash(it1) == hash(it2), "разные хеши у равных объектов"
#
# it2 = ShopItem('name', 10, 12)
# assert hash(it1) != hash(it2), "равные хеши у разных объектов"
#
# it2 = ShopItem('name', 11, 11)
# assert hash(it1) != hash(it2), "равные хеши у разных объектов"
#
# it2 = ShopItem('NAME', 10, 11)
# assert hash(it1) == hash(it2), "разные хеши у равных объектов"
#
# name = lst_in[0].split(':')
# for sp in shop_items.values():
#     assert isinstance(sp[0], ShopItem) and type(sp[1]) == int, "в значениях словаря shop_items первый элемент должен быть объектом класса ShopItem, а второй - целым числом"
#
# v = list(shop_items.values())
# if v[0][0].name.strip() == "Системный блок":
#     assert v[0][1] == 1 and v[1][1] == 2 and v[2][1] == 1 and len(v) == 3, "неверные значения в словаре shop_items"
#
# if v[0][0].name.strip() == "X-box":
#     assert v[0][1] == 2 and v[1][1] == 1 and v[2][1] == 2 and len(v) == 3, "неверные значения в словаре shop_items"



# =================================================================================================



# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/rqCqhjtl6Lw
# Подвиг 7. Объявите класс с именем DataBase (база данных - БД), объекты которого создаются командой:
# db = DataBase(path)
# где path - путь к файлу с данными БД (строка).
# Также в классе DataBase нужно объявить следующие методы:
# write(self, record) - для добавления новой записи в БД, представленной объектом record;
# read(self, pk) - чтение записи из БД (возвращает объект Record) по ее уникальному идентификатору pk
# (уникальное целое положительное число); запись ищется в значениях словаря (см. ниже)
# Каждая запись БД должна описываться классом Record, а объекты этого класса создаваться командой:
# record = Record(fio, descr, old)
# где fio - ФИО некоторого человека (строка); descr - характеристика человека (строка); old - возраст человека (целое число).
# В каждом объекте класса Record должны формироваться следующие локальные атрибуты:
# pk - уникальный идентификатор записи (число: целое, положительное); формируется автоматически при создании каждого нового объекта;
# fio - ФИО человека (строка);
# descr - характеристика человека (строка);
# old - возраст человека (целое число).
# Реализовать для объектов класса Record вычисление хэша по атрибутам: fio и old (без учета регистра). Если
# они одинаковы для разных записей, то и хэши должны получаться равными. Также для объектов класса Record  с
# одинаковыми хэшами оператор == должен выдавать значение True, а с разными хэшами - False.
# Хранить записи в БД следует в виде словаря dict_db (атрибут объекта db класса DataBase), ключами которого являются
# объекты класса Record, а значениями список из объектов с равными хэшами:
# dict_db[rec1] = [rec1, rec2, ..., recN]
# где rec1, rec2, ..., recN - объекты класса Record с одинаковыми хэшами.
# Для наполнения БД прочитайте строки из входного потока с помощью команды:
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# где каждая строка представлена в формате:
# "ФИО; характеристика; возраст"
# Например:
# Балакирев С.М.; программист; 33
# Кузнецов А.В.; разведчик-нелегал; 35
# Суворов А.В.; полководец; 42
# Иванов И.И.; фигурант всех подобных списков; 26
# Балакирев С.М.; преподаватель; 37
# Каждая строка должна быть представлена объектом класса Record и записана в БД db (в словарь db.dict_db).
# P.S. На экран ничего выводить не нужно.
# Sample Input:
# Балакирев С.М.; программист; 33
# Кузнецов Н.И.; разведчик-нелегал; 35
# Суворов А.В.; полководец; 42
# Иванов И.И.; фигурант всех подобных списков; 26
# Балакирев С.М.; преподаватель; 33
# Sample Output:

# class DataBase:
#     def __init__(self, path):
#         self.path = path
#         self.dict_db = {}
#
#     def write(self, record):
#         if record not in self.dict_db:
#             self.dict_db[record] = [record]
#         else:
#             self.dict_db[record].append(record)
#
#     def read(self, pk):
#         for i in self.dict_db.values():
#             for obj in i:
#                 if obj.pk == pk:
#                     return obj
#
# class Record:
#     PK = 1
#
#     def __init__(self, fio, descr, old):
#         self.fio = fio
#         self.descr = descr
#         self.old = int(old)
#         self.pk = self.PK
#
#     def __new__(cls, *args, **kwargs):
#         cls.PK += 1
#         return super().__new__(cls)
#
#     def __hash__(self):
#         return hash((self.fio.lower(), self.old))
#
#     def __eq__(self, other):
#         return self.__hash__() == other.__hash__()
#
# lst_in = ['Балакирев С.М.; программист; 33', 'Кузнецов Н.И.; разведчик-нелегал; 35', 'Суворов А.В.; полководец; 42', 'Иванов И.И.; фигурант всех подобных списков; 26', 'Балакирев С.М.; преподаватель; 33']
# db = DataBase('c://database')
# for i in lst_in:
#     fio, descr, old = i.split('; ')
#     db.write(Record(fio, descr, old))
#
# # print(db.dict_db)
#
## TESTS
# db22345 = DataBase('123')
# r1 = Record('fio', 'descr', 10)
# r2 = Record('fio', 'descr', 10)
# r3 = Record('fio', 'descr', 10)
# # print(r1.pk, hash(r1))
# # print(r2.pk, hash(r2))
# assert r1.pk != r2.pk, "равные значения атрибута pk у разных объектов класса Record"
#
# db22345.write(r2)
# r22 = db22345.read(r2.pk)
# assert r22.pk == r2.pk and r22.fio == r2.fio and r22.descr == r2.descr and r22.old == r2.old, "при операциях write и read прочитанный объект имеет неверные значения атрибутов"
#
# assert len(db22345.dict_db) == 1, "неверное число объектов в словаре dict_db"
#
# fio = lst_in[0].split(';')[0].strip()
# v = list(db.dict_db.values())
# if fio == "Балакирев С.М.":
#     assert len(v[0]) == 2 and len(v[1]) == 1 and len(v[2]) == 1 and len(
#         v[3]) == 1, "неверно сформирован словарь dict_db"
# #
# if fio == "Гейтс Б.":
#     assert len(v[0]) == 2 and len(v[1]) == 2 and len(v[2]) == 1 and len(
#         v[3]) == 1, "неверно сформирован словарь dict_db"



# ================================================================================================



# Подвиг 8. Из входного потока необходимо прочитать список строк командой:
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# Каждая строка содержит информацию об учебном пособии в формате:
# "Название; автор; год издания"
# Например:
# Python; Балакирев С.М.; 2020
# Python ООП; Балакирев С.М.; 2021
# Python ООП; Балакирев С.М.; 2022
# Python; Балакирев С.М.; 2021
# Необходимо каждую из этих строк представить объектом класса BookStudy, которые создаются командой:
# bs = BookStudy(name, author, year)
# где name - название пособия (строка); author - автор пособия (строка); year - год издания (целое число).
# Такие же публичные локальные атрибуты должны быть в объектах класса BookStudy.
# Для каждого объекта реализовать вычисление хэша по двум атрибутам: name и author (без учета регистра).
# Сформировать список lst_bs из объектов класса BookStudy на основе прочитанных строк (списка lst_in).
# После этого определить число книг с уникальными хэшами. Это число сохранить через переменную unique_books (целое число).
# P.S. На экран ничего выводить не нужно.
# Sample Input:
# Python; Балакирев С.М.; 2020
# Python ООП; Балакирев С.М.; 2021
# Python ООП; Балакирев С.М.; 2022
# Python; Балакирев С.М.; 2021
# Sample Output:
#

# lst_in = [
#     'Python; Балакирев С.М.; 2020',
#     'Python ООП; Балакирев С.М.; 2021',
#     'Python ООП; Балакирев С.М.; 2022',
#     'Python; Балакирев С.М.; 2021',
# ]

# lst_in = list(map(str.strip, sys.stdin.readlines()))

# class BookStudy:
#     def __init__(self, name, author, year):
#         self.name = name
#         self.author = author
#         self.year = int(year)
#
#     def __hash__(self):
#         return hash((self.name.lower(), self.author.lower()))
#
#     def __eq__(self, other):
#         return self.name.lower() == other.name.lower() and self.author.lower() == other.author.lower()
#
# lst_bs = list(map(lambda x: BookStudy(*x.split('; ')), lst_in))
# unique_books = len(set(lst_bs))
# print(unique_books)

# ======================================================================================================



# Подвиг 9 (релакс). Объявите класс с именем Dimensions, объекты которого создаются командой:
# d = Dimensions(a, b, c)
# где a, b, c - положительные числа (целые или вещественные), описывающие габариты некоторого тела: высота, ширина и глубина.
# Каждый объект класса Dimensions должен иметь аналогичные публичные атрибуты a, b, c (с соответствующими числовыми значениями).
# Также для каждого объекта должен вычисляться хэш на основе всех трех габаритов: a, b, c.
# С помощью функции input() прочитайте из входного потока строку, записанную в формате:
# "a1 b1 c1; a2 b2 c2; ... ;aN bN cN"
# Например:
# "1 2 3; 4 5 6.78; 1 2 3; 0 1 2.5"
# Если какой-либо габарит оказывается отрицательным значением или равен нулю, то при создании объектов должна генерироваться ошибка командой:
# raise ValueError("габаритные размеры должны быть положительными числами")
# Сформируйте на основе прочитанной строки список lst_dims из объектов класса Dimensions. После этого отсортируйте этот список по
# возрастанию (неубыванию) хэшей этих объектов так, чтобы объекты с равными хэшами стояли друг за другом.
# P.S. На экран ничего выводить не нужно.
# Sample Input:
# 1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5
# Sample Output:

# s_inp = '1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5'
#
# class Dimensions:
#     def __init__(self, a, b, c):
#         self.a = self.__check_value(a)
#         self.b = self.__check_value(b)
#         self.c = self.__check_value(c)
#
#     def __check_value(self, x):
#         if str(x).isdigit() and int(x) > 0:
#             return int(x)
#         elif self.is_float(x) and float(x) > 0:
#             return float(x)
#         else:
#             raise ValueError("габаритные размеры должны быть положительными числами")
#
#     def is_float(self, x):
#         try:
#             float(x)
#             return True
#         except:
#             return False
#
#     def __eq__(self, other):
#         return self.a == other.a and self.b == other.b and self.c == other.c
#
#     def __hash__(self):
#         return hash((self.a, self.b, self.c))
#
#
# d1 = Dimensions(1, 4, 3)
#
# lst_in = list(map(lambda x: Dimensions(*x.split()), s_inp.split('; ')))
# # print(lst_in)
# lst_in_hashes = list(sorted(lst_in, key=lambda x: hash(x)))
# print(lst_in_hashes)



# =================================================================================================



# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/0EYz8-qG2iU
# Подвиг 10 (на повторение). Объявите класс с именем Triangle, объекты которого создаются командой:
# tr = Triangle(a, b, c)
# где a, b, c - длины сторон треугольника (числа: целые или вещественные). В классе Triangle объявите следующие дескрипторы данных:
# a, b, c - для записи и считывания длин сторон треугольника.
# При записи нового значения нужно проверять, что присваивается положительное число (целое или вещественное). Иначе, генерируется исключение командой:
# raise ValueError("длины сторон треугольника должны быть положительными числами")
# Также нужно проверять, что все три стороны a, b, c могут образовывать стороны треугольника. То есть, должны выполняться условия:
# a < b+c; b < a+c; c < a+b
# Иначе генерируется исключение командой:
# raise ValueError("с указанными длинами нельзя образовать треугольник")
# Наконец, с объектами класса Triangle должны выполняться функции:
# len(tr) - возвращает периметр треугольника, приведенный к целому значению с помощью функции int();
# tr() - возвращает площадь треугольника (можно вычислить по формуле Герона: s = sqrt(p * (p-a) * (p-b) * (p-c)), где p - полупериметр треугольника).
# P.S. На экран ничего выводить не нужно, только объявить класс Triangle.



# class Descript:
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         setattr(instance, self.name, value)
#
#     @classmethod
#     def verify_coord(cls, coord):
#         if not isinstance(coord, (int, float)):
#             raise ValueError("с указанными длинами нельзя образовать треугольник")
#
# class Triangle:
#     a = Descript()
#     b = Descript()
#     c = Descript()
#
#     def __init__(self, a, b, c):
#         self.check_len(a, b, c)
#         self.a = a
#         self.b = b
#         self.c = c
#
#     @classmethod
#     def check_len(cls, a, b, c):
#         if a < b + c and b < a+c and c < a+b:
#             return True
#         raise ValueError("1с указанными длинами нельзя образовать треугольник")
#
#     def __len__(self):
#         return int(self.a + self.b + self.c)
#
#     def __call__(self):
#         p = (self.a + self.b + self.c) / 2
#         return int((p * (p-self.a) * (p-self.b) * (p-self.c))** 0.5)  #формула герона
#
#
# # tr = Triangle(3,6,6)
# # print(len(tr))
# # print(tr())
#
# # TESTS
# tr = Triangle(5, 4, 3)
# assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"
#
# try:
#     tr = Triangle(-5, 4, 3)
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"
#
# try:
#     tr = Triangle(10, 1, 1)
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"
#
# tr = Triangle(5, 4, 3)
# assert len(tr) == 12, "функция len вернула неверное значение"
# assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"