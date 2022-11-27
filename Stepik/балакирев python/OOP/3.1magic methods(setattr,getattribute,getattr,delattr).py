# class Point:
#     MAX_COORD = 100     #атрибуты класса являются общими для всех его экземпляров
#     MIN_COORD = 0
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coord(self, x, y):
#         self.x = x if self.MIN_COORD <= x <= self.MAX_COORD else self.x
#         self.y = y if self.MIN_COORD <= y <= self.MAX_COORD else self.y
#
#     # def change_min(self, min):        #такой метод не работает ,тк добаляет локальный атрибут в экз класса со значением -100,
#     #     self.MIN_COORD = min          #а в самом классе атрибут не поменялся
#
#     @classmethod        #вот так работает, выше метод не может менять атрибуты класса
#     def change_min(cls, min):
#         cls.MIN_COORD = min
#
#     # def __getattribute__(self, item):
#     #     print('__getattribute__')    #метод срабатывает при обращении к родительскому классу через экземпляр класса
#     #     return object.__getattribute__(self, item)   #обратились к родительскому классу object
#
#     def __getattribute__(self, item): # можно запретить доступ к атрибутам класса, например так
#         if item == 'x':
#             raise TypeError('Access denied')
#         else:
#             return object.__getattribute__(self, item)
#
#     # def __setattr__(self, key, value):
#     #     print('setattr')
#     #     object.__setattr__(self, key, value) #при переназначении метода будет 4 вывода принта, х и у для двух экземпляров класса
#
#     def __setattr__(self, key, value):  #запрет на создание атрибута с определенным именем
#         if key == 'z':
#             raise AttributeError('bad name for attribute')
#         else:
#             object.__setattr__(self, key, value)
#             # self.x = value # не делать так, тк магический метод уйдет в бесконечную рекурсию
#             # self.__dict__[key] = value  #а так можно делать
#
#     def __getattr__(self, item):    #обращение к несуществующему атрибуту! класса
#         print('get attr')
#         return False    #можно переопределить и использовать , тк не срабатывает когда есть атрибут
#
#     def __delattr__(self, item):    #срабатывает при удалении атрибута
#         print('del attr')
#         object.__delattr__(self, item)  #удаление атрибута
# pt1 = Point(3,1)
# pt2 = Point(2,100)
# a = pt1.y #__getattribute__ , а при X будет ошибка о запрете доступа
# print(a)    #1


# ==============================================================================================================


# Подвиг 3. Объявите класс Book для представления информации о книге. Объекты этого класса должны создаваться командами:
# book = Book()
# book = Book(название, автор, число страниц, год издания)
# В каждом объекте класса Book автоматически должны формироваться следующие локальные свойства:
# title - заголовок книги (строка, по умолчанию пустая строка);
# author - автор книги (строка, по умолчанию пустая строка);
# pages - число страниц (целое число, по умолчанию 0);
# year - год издания (целое число, по умолчанию 0).
# Объявите в классе Book магический метод __setattr__ для проверки типов присваиваемых данных локальным
# свойствам title, author, pages и year. Если типы не соответствуют локальному атрибуту (например, title
# должна ссылаться на строку, а pages - на целое число), то генерировать исключение командой:
# raise TypeError("Неверный тип присваиваемых данных.")
# Создайте в программе объект book класса Book для книги:
# автор: Сергей Балакирев
# заголовок: Python ООП
# pages: 123
# year: 2022
# P.S. На экран ничего выводить не нужно.


# class Book:
#     def __init__(self, title='', author='', pages=0, year=0):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.year = year
#
#     def __setattr__(self, key, value):
#         if key in ('title', 'author') and type(value) == str:
#             object.__setattr__(self, key, value)
#         elif key in ('pages', 'year') and type(value) == int:
#             object.__setattr__(self, key, value)
#         else:
#             raise TypeError("Неверный тип присваиваемых данных.")
#
# # автор: Сергей Балакирев
# # заголовок: Python ООП
# # pages: 123
# # year: 2022
# p = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
# print(p.__dict__)
# p1 = Book(100, 'Python ООП', 123, 2022) #error , title int)))


# ==================================================================================


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/DVydksYIejk
# Подвиг 4. Вы создаете интернет-магазин. Для этого нужно объявить два класса:
# Shop - класс для управления магазином в целом;
# Product - класс для представления отдельного товара.
# Объекты класса Shop следует создавать командой:
# shop = Shop(название магазина)
# В каждом объекте класса Shop должно создаваться локальное свойство:
# goods - список товаров (изначально список пустой).
# А также в классе объявить методы:
# add_product(self, product) - добавление нового товара в магазин (в конец списка goods);
# remove_product(self, product) - удаление товара product из магазина (из списка goods);
# Объекты класса Product следует создавать командой:
# p = Product(название, вес, цена)
# В них автоматически должны формироваться локальные атрибуты:
# id - уникальный идентификационный номер товара (генерируется автоматически как целое положительное число от 1 и далее);
# name - название товара (строка);
# weight - вес товара (целое или вещественное положительное число);
# price - цена (целое или вещественное положительное число).
# В классе Product через магические методы (подумайте какие) осуществить проверку на тип присваиваемых
# данных локальным атрибутам объектов класса (например, id - целое число, name - строка и т.п.).
# Если проверка не проходит, то генерировать исключение командой:
# raise TypeError("Неверный тип присваиваемых данных.")
# Также в классе Product с помощью магического(их) метода(ов) запретить удаление локального атрибута id.
# При попытке это сделать генерировать исключение:
# raise AttributeError("Атрибут id удалять запрещено.")
# Пример использования классов (в программе эти строчки не писать):
# shop = Shop("Балакирев и К")
# book = Product("Python ООП", 100, 1024)
# shop.add_product(book)
# shop.add_product(Product("Python", 150, 512))
# for p in shop.goods:
#     print(f"{p.name}, {p.weight}, {p.price}")
# P.S. На экран ничего выводить не нужно.

# class Shop:
#     def __init__(self, name):
#         self.goods = []
#         self.name = name
#
#     def add_product(self, product):
#         self.goods.append(product)
#
#     def remove_product(self, product):
#         self.goods.remove(product)
#
# class Product:
#     ID = 1
#
#     def __init__(self, name, weight, price):
#         self.id = self.ID
#         self.name = name
#         self.weight = weight
#         self.price = price
#         self.id_plus()
#
#     @classmethod
#     def id_plus(cls):
#         cls.ID += 1
#
#     def __setattr__(self, key, value):
#         if key in ('id', 'ID') and type(value) == int:
#             object.__setattr__(self, key, value)
#         elif key == 'name' and type(value) == str:
#             object.__setattr__(self, key, value)
#         elif key in ('weight', 'price') and type(value) in (float, int) and value >= 0:
#             object.__setattr__(self, key, value)
#         else:
#             raise TypeError("Неверный тип присваиваемых данных.")
#
#     def __delattr__(self, item):
#         if item == 'id':
#             raise AttributeError("Атрибут id удалять запрещено.")
#         else:
#             object.__delattr__(self, item)
#
#
# shop = Shop("Балакирев и К")
# book = Product("Python ООП", 100, 1024)
# shop.add_product(book)
# shop.add_product(Product("Python", 150, 512))
# for p in shop.goods:
#     print(f"{p.id} {p.name}, {p.weight}, {p.price}")


# ========================================================================================================


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/7b8d5zqiiAM
# Подвиг 5. Необходимо создать программу для обучающего курса. Для этого объявляются три класса:
# Course - класс, отвечающий за управление курсом в целом;
# Module - класс, описывающий один модуль (раздел) курса;
# LessonItem - класс одного занятия (урока).
# Структура курса на уровне этих классов, приведена на рисунке ниже:
# Объекты класса LessonItem должны создаваться командой:
# lesson = LessonItem(название урока, число практических занятий, общая длительность урока)
# Соответственно, в каждом объекте класса LessonItem должны создаваться локальные атрибуты:
# title - название урока (строка);
# practices - число практических занятий (целое положительное число);
# duration - общая длительность урока (целое положительное число).
# Необходимо с помощью магических методов реализовать следующую логику взаимодействия с объектами класса LessonItem:
# 1. Проверять тип присваиваемых данных локальным атрибутам. Если типы не соответствуют требованиям, то генерировать исключение командой:
# raise TypeError("Неверный тип присваиваемых данных.")
# 2. При обращении к несуществующим атрибутам объектов класса LessonItem возвращать значение False.
# 3. Запретить удаление атрибутов title, practices и duration в объектах класса LessonItem.
# Объекты класса Module должны создаваться командой:
# module = Module(название модуля)
# Каждый объект класса Module должен содержать локальные атрибуты:
# name - название модуля;
# lessons - список из уроков (объектов класса LessonItem), входящих в модуль (изначально список пуст).
# Также в классе Module должны быть реализованы методы:
# add_lesson(self, lesson) - добавление в модуль (в конец списка lessons) нового урока (объекта класса LessonItem);
# remove_lesson(self, indx) - удаление урока по индексу в списке lessons.
# Наконец, объекты класса Course создаются командой:
# course = Course(название курса)
# И содержат следующие локальные атрибуты:
# name - название курса (строка);
# modules - список модулей в курсе (изначально список пуст).
# Также в классе Course должны присутствовать следующие методы:
# add_module(self, module) - добавление нового модуля в конце списка modules;
# remove_module(self, indx) - удаление модуля из списка modules по индексу в этом списке.
# Пример использования классов (в программе эти строчки не писать):
# course = Course("Python ООП")
# module_1 = Module("Часть первая")
# module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
# module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
# module_1.add_lesson(LessonItem("Урок 3", 5, 800))
# course.add_module(module_1)
# module_2 = Module("Часть вторая")
# module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
# module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
# course.add_module(module_2)
# P.S. На экран ничего выводить не нужно.

# class Course:   #класс с самим курсом
#     def __init__(self, name):
#         self.name = name
#         self.modules = []
#
#     def add_module(self, module):
#         self.modules.append(module)
#
#     def remove_module(self, indx):
#         self.modules.pop(indx)
#
# class Module:   # класс с модулями
#     def __init__(self, name):
#         self.name = name
#         self.lessons = []
#
#     def add_lesson(self, lesson):
#         self.lessons.append(lesson)
#
#     def remove_lesson(self, indx):
#         self.lessons.pop(indx)
#
# class LessonItem: # класс с уроками
#     def __init__(self, title, practices, duration):
#         self.title = title
#         self.practices = practices
#         self.duration = duration
#
#     def __setattr__(self, key, value):
#         if key == 'title' and type(value) == str:
#             object.__setattr__(self, key, value)
#         elif key in ('practices', 'duration') and type(value) == int:
#             object.__setattr__(self, key, value)
#         else:
#             raise TypeError("Неверный тип присваиваемых данных.")
#
#     def __getattr__(self, item):
#         return False
#
#     def __delattr__(self, item):
#         if item not in ('title', 'practices', 'duration'):
#             object.__delattr__(self, item)

# course = Course("Python ООП")
# module_1 = Module("Часть первая")
# module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
# module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
# module_1.add_lesson(LessonItem("Урок 3", 5, 800))
# course.add_module(module_1)
# module_2 = Module("Часть вторая")
# module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
# module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
# course.add_module(module_2)
# for i in course.modules:
#     for j in i.lessons:
#         print(j.title)


# ==================================================================================================


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/oyeub94DCKw
# Подвиг 6. Вам необходимо написать программу описания музеев. Для этого нужно объявить класс Museum, объекты которого формируются командой:
# mus = Museum(название музея)
# В объектах этого класса должны формироваться следующие локальные атрибуты:
# name - название музея (строка);
# exhibits - список экспонатов (изначально пустой список).
# Сам класс Museum должен иметь методы:
# add_exhibit(self, obj) - добавление нового экспоната в музей (в конец списка exhibits);
# remove_exhibit(self, obj) - удаление экспоната из музея (из списка exhibits по ссылке obj - на экспонат)
# get_info_exhibit(self, indx) - получение информации об экспонате (строка) по индексу списка (нумерация с нуля).
# Экспонаты представляются объектами своих классов. Для примера объявите в программе следующие классы экспонатов:
# Picture - для картин;
# Mummies - для мумий;
# Papyri - для папирусов.
# Объекты этих классов должны создаваться следующим образом (с соответствующим набором локальных атрибутов):
# p = Picture(название, художник, описание)            # локальные атрибуты: name - название; author - художник; descr - описание
# m = Mummies(имя мумии, место находки, описание)      # локальные атрибуты: name - имя мумии; location - место находки; descr - описание
# pr = Papyri(название папируса, датировка, описание)  # локальные атрибуты: name - название папируса; date - датировка (строка); descr - описание
# Метод get_info_exhibit() класса Museum должен возвращать значение атрибута descr указанного экспоната в формате:
# "Описание экспоната {name}: {descr}"
# Например:
# "Описание экспоната Девятый вал: Айвазовский написал супер картину."
# Пример использования классов (в программе эти строчки писать не нужно - только для примера):
# mus = Museum("Эрмитаж")
# mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая картина"))
# mus.add_exhibit(Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации"))
# p = Papyri("Ученья для, не злата ради", "Древняя Россия", "Самое древнее найденное рукописное свидетельство о языках программирования")
# mus.add_exhibit(p)
# for x in mus.exhibits:
#     print(x.descr)
# P.S. На экран ничего выводить не нужно.

# class Museum:
#     def __init__(self, name):
#         self.name = name
#         self.exhibits = []
#     def add_exhibit(self, obj):
#         self.exhibits.append(obj)
#
#     def remove_exhibit(self, obj):
#         self.exhibits.remove(obj)
#
#     def get_info_exhibit(self, indx):
#         s = self.exhibits[indx]
#         return f"Описание экспоната {s.name}: {s.descr}"
#
# class Picture:  # - для картин;
#     def __init__(self, name, author, descr):
#         self.name = name
#         self.author = author
#         self.descr = descr
#
# class Mummies:
#     def __init__(self, name, location, descr):
#         self.name = name
#         self.location = location
#         self.descr = descr
#
# class Papyri:
#     def __init__(self, name, date, descr):
#         self.name = name
#         self.date = date
#         self.descr = descr


# mus = Museum("Эрмитаж")
# mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая картина"))
# mus.add_exhibit(Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации"))
# p = Papyri("Ученья для, не злата ради", "Древняя Россия", "Самое древнее найденное рукописное свидетельство о языках программирования")
# mus.add_exhibit(p)
# for x in mus.exhibits:
#     print(x.descr)

# +++++++++++++++
# можно было через наследование классы определить
#
# class Exhibit:
#     overridable_attr = None
#
#     def __init__(self, name, overridable, descr):
#         self.name = name
#         self.overridable = overridable
#         self.descr = descr
#
#     def __setattr__(self, key, value):
#         if key == 'overridable':
#             key = self.overridable_attr
#         object.__setattr__(self, key, value)
#
#
# class Picture(Exhibit):
#     overridable_attr = 'author'
#
#
# class Mummies(Exhibit):
#     overridable_attr = 'location'
#
#
# class Papyri(Exhibit):
#     overridable_attr = 'date'

# ==============================================================================


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/Xq19kCDRaag
# Подвиг 7 (на повторение). Объявите класс SmartPhone, объекты которого предполагается создавать командой:
# sm = SmartPhone(марка смартфона)
# Каждый объект должен содержать локальные атрибуты:
# model - марка смартфона (строка);
# apps - список из установленных приложений (изначально пустой).
# Также в классе SmartPhone должны быть объявлены следующие методы:
# add_app(self, app) - добавление нового приложения на смартфон (в конец списка apps);
# remove_app(self, app) - удаление приложения по ссылке на объект app.
# При добавлении нового приложения проверять, что оно отсутствует в списке apps (отсутствует объект соответствующего класса).
# Каждое приложение должно определяться своим классом. Для примера объявите следующие классы:
# AppVK - класс приложения ВКонтаке;
# AppYouTube - класс приложения YouTube;
# AppPhone - класс приложения телефона.
# Объекты этих классов должны создаваться следующим образом (с соответствующим набором локальных атрибутов):
# app_1 = AppVK() # name = "ВКонтакте"
# app_2 = AppYouTube(1024) # name = "YouTube", memory_max = 1024
# app_3 = AppPhone({"Балакирев": 1234567890, "Сергей": 98450647365, "Работа": 112}) # name = "Phone", phone_list = словарь с контактами
# Пример использования классов (в программе эти строчки не писать):
# sm = SmartPhone("Honor 1.0")
# sm.add_app(AppVK())
# sm.add_app(AppVK())  # второй раз добавляться не должно
# sm.add_app(AppYouTube(2048))
# for a in sm.apps:
#     print(a.name)
# P.S. На экран ничего выводить не нужно.

# class SmartPhone:
#     def __init__(self, model):
#         self.model = model
#         self.apps = []
#
#     def __setattr__(self, key, value):
#         if key == 'model' and type(value) == str:
#             object.__setattr__(self, key, value)
#         object.__setattr__(self, key, value)
#
#
#     def add_app(self, app):
#         s = [i.name for i in self.apps]
#         if app.name not in s:
#             self.apps.append(app)
#
#     def remove_app(self, app):
#         self.apps.remove(app)
#
# class AppVK:
#     def __init__(self):
#         self.name = "ВКонтакте"
#
# class AppYouTube:
#     def __init__(self, memory_max):
#         self.name = "YouTube"
#         self.memory_max = memory_max
#
# class AppPhone:
#     def __init__(self, phone_list):
#         self.name = 'Phone'
#         self.phone_list = phone_list


# sm = SmartPhone("Honor 1.0")
#
# sm.add_app(AppVK())
# sm.add_app(AppVK())
# print(sm.apps)# второй раз добавляться не должно
# sm.add_app(AppYouTube(2048))
# for a in sm.apps:
#     print(a.name)


# ===========================================================================================

# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/vOh4gzHnMWg
# Подвиг 8. Объявите класс Circle (окружность), объекты которого должны создаваться командой:
# circle = Circle(x, y, radius)   # x, y - координаты центра окружности; radius - радиус окружности
# В каждом объекте класса Circle должны формироваться локальные приватные атрибуты:
# __x, __y - координаты центра окружности (вещественные или целые числа);
# __radius - радиус окружности (вещественное или целое положительное число).
# Для доступа к этим приватным атрибутам в классе Circle следует объявить объекты-свойства (property):
# x, y - для изменения и доступа к значениям __x, __y, соответственно;
# radius - для изменения и доступа к значению __radius.
# При изменении значений приватных атрибутов через объекты-свойства нужно проверять, что присваиваемые значения
# - числа (целые или вещественные). Дополнительно у радиуса проверять, что число должно быть положительным (строго больше нуля).
# Сделать все эти проверки нужно через магические методы. При некорректных переданных числовых значениях,
# прежние значения меняться не должны (исключений никаких генерировать при этом не нужно).
# Если присваиваемое значение не числовое, то генерировать исключение командой:
# raise TypeError("Неверный тип присваиваемых данных.")
# При обращении к несуществующему атрибуту объектов класса Circle выдавать булево значение False.
# Пример использования класса (эти строчки в программе писать не нужно):
# circle = Circle(10.5, 7, 22)
# circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
# x, y = circle.x, circle.y
# res = circle.name # False, т.к. атрибут name не существует
# P.S. На экран ничего выводить не нужно.

# class Coord:
#     def __set_name__(self, owner, name):
#         self.name = '__' + name
#     def __set__(self, instance, value):
#         setattr(instance, self.name, value)
#
# class Circle:
#     x = Coord()
#     y = Coord()
#     radius = Coord()
#
#     def __init__(self, x, y, radius):
#         self.x = x
#         self.y = y
#         self.radius = radius
#
#     def __getattr__(self, item):
#         return False
#
#     @property
#     def x(self):
#         return self.__x
#     @x.setter
#     def x(self, x):
#         if type(x) in (int, float):
#             self.__x = x
#         else:
#             raise TypeError("Неверный тип присваиваемых данных.")
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, y):
#         if type(y) in (int, float):
#             self.__y = y
#         else:
#             raise TypeError("Неверный тип присваиваемых данных.")
#
#     @property
#     def radius(self):
#         return self.__radius
#
#     @radius.setter
#     def radius(self, radius):
#         if type(radius) in (int, float):
#             if radius > 0:
#                 self.__radius = radius
#         else:
#             raise TypeError("Неверный тип присваиваемых данных.")


# circle = Circle(10.5, 7, 22)
# circle.radius = -10
# print(circle.radius)
# x, y = circle.x, circle.y
# res = circle.name

# TEST


# assert type(Circle.x) == property and type(Circle.y) == property and type(
#     Circle.radius) == property, "в классе Circle должны быть объявлены объекты-свойства x, y и radius"

#
# cr = Circle(20, 7, 22)
# print(cr.x, cr.y, cr.radius)
# try:
#     cr = Circle(20, '7', 22)
# except TypeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение TypeError при инициализации объекта с недопустимыми аргументами"

# cr = Circle(20, 7, 22)
# assert cr.x == 20 and cr.y == 7 and cr.radius == 22, "объекты-свойства x, y и radius вернули неверные значения"
#
# cr.radius = -10  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
# assert cr.radius == 22, "при присваивании некорректного значения, прежнее значение изменилось"
#
# x, y = cr.x, cr.y
# assert x == 20 and y == 7, "объекты-свойства x, y вернули некорректные значения"
# assert cr.name == False, "при обращении к несуществующему атрибуту должно возвращаться значение False"
#
# try:
#     cr.x = '20'
# except TypeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение TypeError"
#
# cr.y = 7.8
# cr.radius = 10.6


# ===============================================================================================

# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/2iS8qnEK9to
# Подвиг 9. Объявите в программе класс Dimensions (габариты) с атрибутами:
# MIN_DIMENSION = 10
# MAX_DIMENSION = 1000
# Каждый объект класса Dimensions должен создаваться командой:
# d3 = Dimensions(a, b, c)   # a, b, c - габаритные размеры
# и содержать локальные атрибуты:
# __a, __b, __c - габаритные размеры (целые или вещественные числа).
# Для работы с этими локальными атрибутами в классе Dimensions следует прописать следующие объекты-свойства:
# a, b, c - для изменения и считывания соответствующих локальных атрибутов __a, __b, __c.
# При изменении значений __a, __b, __c следует проверять, что присваиваемое значение число в диапазоне [MIN_DIMENSION; MAX_DIMENSION].
# Если это не так, то новое значение не присваивается (игнорируется).
# С помощью магических методов данного занятия запретить создание локальных атрибутов MIN_DIMENSION и MAX_DIMENSION
# в объектах класса Dimensions. При попытке это сделать генерировать исключение:
# raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
# Пример использования класса  (эти строчки в программе писать не нужно):
# d = Dimensions(10.5, 20.1, 30)
# d.a = 8
# d.b = 15
# a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
# d.MAX_DIMENSION = 10  # исключение AttributeError
# P.S. В программе нужно объявить только класс Dimensions. На экран ничего в

# class Dimensions:
#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 1000
#     def __init__(self, a, b, c):
#         self.__a = a
#         self.__b = b
#         self.__c = c
#
#     @property
#     def a(self):
#         return self.__a
#     @a.setter
#     def a(self, a):
#         if self.MIN_DIMENSION <= a <= self.MAX_DIMENSION:
#             self.__a = a
#
#     @property
#     def b(self):
#         return self.__b
#
#     @b.setter
#     def b(self, b):
#         if self.MIN_DIMENSION <= b <= self.MAX_DIMENSION:
#             self.__b = b
#
#     @property
#     def c(self):
#         return self.__c
#
#     @c.setter
#     def c(self, c):
#         if self.MIN_DIMENSION <= c <= self.MAX_DIMENSION:
#             self.__c = c
#
#     def __setattr__(self, key, value):
#         if key not in ('MIN_DIMENSION', 'MAX_DIMENSION'):
#             object.__setattr__(self, key, value)
#         else:
#             raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")

# d = Dimensions(10.5, 20.1, 30)
# d.a = 8
# d.b = 15
# a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
# print(a,b,c)
# d.MAX_DIMENSION = 10  # исключение AttributeError
#


# ======================================================================================================


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/FaHqn8Yr45o
# Подвиг 10. Объявите класс GeyserClassic - фильтр для очистки воды. В этом классе должно быть три слота для фильтров.
# Каждый слот строго для своего класса фильтра:
# Mechanical - для очистки от крупных механических частиц;
# Aragon - для последующей очистки воды;
# Calcium - для обработки воды на третьем этапе.
# Объекты классов фильтров должны создаваться командами:
# filter_1 = Mechanical(дата установки)
# filter_2 = Aragon(дата установки)
# filter_3 = Calcium(дата установки)
# Во всех объектах этих классов должен формироваться локальный атрибут:
# date - дата установки фильтров (для простоты - положительное вещественное число).
# Также нужно запретить изменение этого атрибута после создания объектов этих классов (только чтение).
# В случае присвоения нового значения, прежнее значение не менять. Ошибок никаких не генерировать.
# Объекты класса GeyserClassic должны создаваться командой:
# g = GeyserClassic()
# А сам класс иметь атрибут:
# MAX_DATE_FILTER = 100 - максимальное время работы фильтра (любого)
# и следующие методы:
# add_filter(self, slot_num, filter) - добавление фильтра filter в указанный слот slot_num (номер слота: 1, 2 и 3),
# если он (слот) пустой (без фильтра). Также здесь следует проверять, что в первый слот можно установить только объекты класса
# Mechanical, во второй - объекты класса Aragon и в третий - объекты класса Calcium. Иначе слот должен оставаться пустым.
# remove_filter(self, slot_num) - извлечение фильтра из указанного слота (slot_num: 1, 2, и 3);
# get_filters(self) - возвращает кортеж из набора трех фильтров в порядке их установки (по возрастанию номеров слотов);
# water_on(self) - включение воды: возвращает True, если вода течет и False - в противном случае.
# Метод water_on() должен возвращать значение True при выполнении следующих условий:
# - все три фильтра установлены в слотах;
# - все фильтры работают в пределах срока службы (значение (time.time() - date) должно быть в пределах [0; MAX_DATE_FILTER])
# Пример использования классов  (эти строчки в программе писать не нужно):
# my_water = GeyserClassic()
# my_water.add_filter(1, Mechanical(time.time()))
# my_water.add_filter(2, Aragon(time.time()))
# w = my_water.water_on() # False
# my_water.add_filter(3, Calcium(time.time()))
# w = my_water.water_on() # True
# f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
# my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
# my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно
# P.S. На экран ничего выводить не нужно.

import time
class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slot_dict = {1: None, 2: None, 3: None}

    def add_filter(self, slot_num, filter):
        if not self.slot_dict[filter.slot] and slot_num == filter.slot:
            self.slot_dict[filter.slot] = filter

    def remove_filter(self, slot_num):
        self.slot_dict[slot_num] = None

    def get_filters(self):
        s = []
        for i in self.slot_dict.values():
            if i:
                s.append(i)
        return tuple(s)

    def water_on(self):
        s = all(map(lambda x: 0 < time.time() - x.date <= self.MAX_DATE_FILTER, self.get_filters()))
        if len(self.get_filters()) == 3 and s:
            return True
        return False


class Mechanical:
    def __init__(self, date):
        self.date = date
        self.slot = 1

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            object.__setattr__(self, key, value)

class Aragon:
    def __init__(self, date):
        self.date = date
        self.slot = 2

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            object.__setattr__(self, key, value)

class Calcium:
    def __init__(self, date):
        self.date = date
        self.slot = 3

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            object.__setattr__(self, key, value)


# my_water = GeyserClassic()
# my_water.add_filter(1, Mechanical(time.time()))

# my_water.add_filter(2, Aragon(time.time()))
# print(my_water.slot_dict)
# print(my_water.get_filters())
# w = my_water.water_on() # False
# print(w)
# my_water.add_filter(3, Calcium(time.time()))
# w = my_water.water_on()
# print(w)# True
# f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
# my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
# my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно


# TEST

# import time
#
# my_water = GeyserClassic()
# my_water.add_filter(1, Mechanical(time.time()))
# my_water.add_filter(2, Aragon(time.time()))
#
# assert my_water.water_on() == False, "метод water_on вернул True, хотя не все фильтры были установлены"
#
# my_water.add_filter(3, Calcium(time.time()))
# assert my_water.water_on(), "метод water_on вернул False при всех трех установленных фильтрах"
# #
# f1, f2, f3 = my_water.get_filters()
# assert isinstance(f1, Mechanical) and isinstance(f2, Aragon) and isinstance(f3, Calcium), "фильтры должны быть устанлены в порядке: Mechanical, Aragon, Calcium"
#
# my_water.remove_filter(1)
# assert my_water.water_on() == False, "метод water_on вернул True, хотя один из фильтров был удален"
#
# my_water.add_filter(1, Mechanical(time.time()))
# assert my_water.water_on(), "метод water_on вернул False, хотя все три фильтра установлены"
#
# f1, f2, f3 = my_water.get_filters()
# my_water.remove_filter(1)
#
# my_water.add_filter(1, Mechanical(time.time() - GeyserClassic.MAX_DATE_FILTER - 1))
# assert my_water.water_on() == False, "метод water_on вернул True, хотя у одного фильтра истек срок его работы"
#
# f1 = Mechanical(1.0)
# f2 = Aragon(2.0)
# f3 = Calcium(3.0)
# assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "неверное значение атрибута date в объектах фильтров"
#
# f1.date = 5.0
# f2.date = 5.0
# f3.date = 5.0
#
# assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "локальный атрибут date в объектах фильтров должен быть защищен от изменения"