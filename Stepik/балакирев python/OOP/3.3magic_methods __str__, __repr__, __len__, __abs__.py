# magic methods (dunder methods or double underscope)
# __str__ - for output
# __repr__ - for debug

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'{self.__class__}: {self.name}'  #python console. там определяем класс -->
# cat = Cat('one')    #создаем экземпляр класса
# print(cat)  #<class '__main__.Cat'>: Vaska
# str(cat)    #"<class '__main__.Cat'>: Vaska" , тк метод str не переопределен
#
# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'{self.__class__}: {self.name}'  #python console. там определяем класс -->
#
#     def __str__(self):
#         return f'{self.name}'
#
# cat = Cat('Васька')
# print(cat) # Васька
# str(cat) # Васька
# cat # <class '__main__.Cat'>: 'Васька'  # это все в консоли


# есть также __len__ и __abs__


# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#
#     def __len__(self):
#         return len(self.__coords)
#
#     def __abs__(self):
#         return list(map(abs, self.__coords))
#
# coord = Point(1, -2, -9)
# print(len(coord))   #переопределили метод len(теперь работает как нам надо)
# print(abs(coord))




'''=================================================================================================='''


# Подвиг 2. Объявите класс с именем Book (книга), объекты которого создаются командой:
# book = Book(title, author, pages)
# где title - название книги (строка); author - автор книги (строка); pages - число страниц в книге (целое число).
# Также при выводе информации об объекте на экран командой:
# print(book)
# должна отображаться строчка в формате:
# "Книга: {title}; {author}; {pages}"
# Например:
# "Книга: Муму; Тургенев; 123"
# Прочитайте из входного потока строки с информацией по книге командой:
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# (строки идут в порядке: title, author, pages). Создайте объект класса Book и выведите его строковое представление в консоль.
# Sample Input:
# Python ООП
# Балакирев С.М.
# 1024
# Sample Output:
# Книга: Python ООП; Балакирев С.М.; 1024
#

# import sys
#
# # здесь пишите программу
#
# lst_in = list(map(str.strip, sys.stdin.readlines())) # считывание списка из входного потока (эту строчку не менять)
# ###
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return f"Книга: {self.title}; {self.author}; {self.pages}"
#
# title, author, pages = lst_in
# book = Book(title, author, pages)
# print(book)



'''======================================================================================'''



# Подвиг 3. Объявите класс с именем Model, объекты которого создаются командой:
# model = Model()
# Объявите в этом классе метод query() для формирования записи базы данных. Использоваться этот метод должен следующим образом:
# model.query(field_1=value_1, field_2=value_2, ..., field_N=value_N)
# Например:
# model.query(id=1, fio='Sergey', old=33)
# Все эти переданные данные должны сохраняться внутри объекта model класса Model. Затем, при выполнении команды:
# print(model)
# В консоль должна выводиться информация об объекте в формате:
# "Model: field_1 = value_1, field_2 = value_2, ..., field_N = value_N"
# Например:
# "Model: id = 1, fio = Sergey, old = 33"
# Если метод query() не вызывался, то в консоль выводится строка:
# "Model"
# P.S. В программе нужно только объявить класс, выводить в консоль ничего не нужно.
# from functools import reduce
# class Model:
#     def __init__(self):
#         self.__args = dict()
#
#     def query(self, **kwargs):
#         for key, value in kwargs.items():
#             self.__args.update({key: value})
#         # print(self.__args)
#
#     def __str__(self):
#         if len(self.__args) > 0:
#             # for i, v in self.__args.items():
#                 # print(i, v)
#             s = reduce(lambda a, b: a + f" {b[0]} = {b[1]},", self.__args.items(), 'Model:').rstrip(',')
#             return s
#         return 'Model'

# model = Model()
# print(model)
# model.query(id=1, fio='Sergey', old=33)
# print(model)
#


#=======================================================================================




# Подвиг 4. Объявите класс WordString, объекты которого создаются командами:
# w1 = WordString()
# w2 = WordString(string)
# где string - передаваемая строка. Например:
# words = WordString("Курс по Python ООП")
# Реализовать следующий функционал для объектов этого класса:
# len(words) - должно возвращаться число слов в переданной строке (слова разделяются одним или несколькими пробелами);
# words(indx) - должно возвращаться слово по его индексу (indx - порядковый номер слова в строке, начиная с 0).
# Также в классе WordString реализовать объект-свойство (property):
# string - для передачи и считывания строки.
# Пример пользования классом WordString (эти строчки в программе писать не нужно):
# words = WordString()
# words.string = "Курс по Python ООП"
# n = len(words)
# first = "" if n == 0 else words(0)
# print(words.string)
# print(f"Число слов: {n}; первое слово: {first}")
# P.S. В программе нужно только объявить класс, выводить в консоль ничего не нужно.


# class WordString:
#     def __init__(self, args=None):
#         if args:
#             self.__args = args
#         else:
#             self.__args = ''
#
#     def __len__(self):
#         return len(self.__args.split())
#
#     def __call__(self, number, *args, **kwargs):
#         if number < len(self.__args.split()):
#             return self.__args.split()[number]
#     # def __str__(self):
#     #     return str(list(self.__args))
#
#     @property
#     def string(self):
#         return self.__args
#
#     @string.setter
#     def string(self, string):
#         self.__args = string



# words = WordString()
# print(len(words))

# words = WordString()
# words.string = "Курс по Python ООП"
# words.string = 'Курс по Python    ООП от  Сергея Балакирева'
# words = WordString("1 2 3    4 5 6 7")
# n = len(words)
#
# k = words(0)
# print(words)
# first = "" if n == 0 else words(0)
# print(words.string)
# print(f"Число слов: {n}; первое слово: {first}")




# ====================================================================================================




# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/6-xKuQp9b7Y
# Теория по двусвязным спискам (при необходимости): https://youtu.be/0sTH9EwXT1I
# Подвиг 5. Объявите класс LinkedList (связный список) для работы со следующей структурой данных:
# Здесь создается список из связанных между собой объектов класса ObjList. Объекты этого класса создаются командой:
# obj = ObjList(data)
# где data - строка с некоторой информацией. Также в каждом объекте obj класса ObjList должны создаваться следующие локальные атрибуты:
# __data - ссылка на строку с данными;
# __prev - ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None);
# __next - ссылка на следующий объект связного списка (если объекта нет, то __next = None).
# В свою очередь, объекты класса LinkedList должны создаваться командой:
# linked_lst = LinkedList()
# и содержать локальные атрибуты:
# head - ссылка на первый объект связного списка (если список пуст, то head = None);
# tail - ссылка на последний объект связного списка (если список пуст, то tail = None).
# А сам класс содержать следующие методы:
# add_obj(obj) - добавление нового объекта obj класса ObjList в конец связного списка;
# remove_obj(indx) - удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу); индекс отсчитывается с нуля.
# Также с объектами класса LinkedList должны поддерживаться следующие операции:
# len(linked_lst) - возвращает число объектов в связном списке;
# linked_lst(indx) - возвращает строку __data, хранящуюся в объекте класса ObjList, расположенного под индексом indx (в связном списке).
# Пример использования классов (эти строчки в программе писать не нужно):
# linked_lst = LinkedList()
# linked_lst.add_obj(ObjList("Sergey"))
# linked_lst.add_obj(ObjList("Balakirev"))
# linked_lst.add_obj(ObjList("Python"))
# linked_lst.remove_obj(2)
# linked_lst.add_obj(ObjList("Python ООП"))
# n = len(linked_lst)  # n = 3
# s = linked_lst(1) # s = Balakirev
# P.S. На экран в программе ничего выводить не нужно. 
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def add_obj(self, obj):
#         if not self.head:
#             self.head = obj
#             self.tail = obj
#             self.tail.indx = 0
#         else:
#             self.tail.next = obj
#             obj.prev = self.tail
#             obj.indx = self.tail.indx + 1
#             self.tail = obj
#
#     def remove_obj(self, indx):
#         if 0 <= indx <= self.tail.indx:
#             temp = self.head
#             while indx != temp.indx:
#                 temp = temp.next        #ищу обьект в памяти с нужным индексом в виде временной ссылки
#
#             if temp.prev:   #если у этой времянки есть предыдущий, то стыковка предыдущего со следующим
#                 temp.prev.next = temp.next
#             else:       # если нет предыдущего , то следующий становится head'om
#                 self.head = temp.next
#             if temp.next:   #если есть следующий, то он стыкуется с предыдущим
#                 temp.next.prev = temp.prev
#             else:
#                 self.tail = temp.prev
#             while temp.next:
#                 temp = temp.next
#                 temp.indx -= 1  # замена индексов
#

#     def __len__(self):
#         counter = 0
#         if self.head:
#             temp = self.head
#             counter += 1
#             while temp.next:
#                 counter += 1
#                 temp = temp.next
#             return counter
#         return 0
#
#
#     def __call__(self, number, *args, **kwargs):
#         temp = self.head
#         while temp.indx != number:
#             temp = temp.next
#         return temp.data
#
#
#
# class ObjList:
#     def __init__(self, data):
#         self.__prev = None
#         self.__data = data
#         self.__next = None
#         self.__indx = None
#
#     @property
#     def indx(self):
#         return self.__indx
#     @indx.setter
#     def indx(self, indx):
#         self.__indx = indx
#
#     @property
#     def data(self):
#         return self.__data
#     @data.setter
#     def data(self, data):
#         self.__data = data
#
#     @property
#     def prev(self):
#         return self.__prev
#
#     @prev.setter
#     def prev(self, prev):
#         self.__prev = prev
#
#     @property
#     def next(self):
#         return self.__next
#     @next.setter
#     def next(self, next):
#         self.__next = next

# linked_lst = LinkedList()
# linked_lst.add_obj(ObjList("Sergey"))
# linked_lst.add_obj(ObjList("Balakirev"))
# linked_lst.add_obj(ObjList("Python"))
# linked_lst.remove_obj(2)
# linked_lst.add_obj(ObjList("Python ООП"))
# n = len(linked_lst)
# print(n)# n = 3
# s = linked_lst(1) # s = Balakirev
# print(s)


# TESTS

# ln = LinkedList()
# ln.add_obj(ObjList("Сергей"))
# ln.add_obj(ObjList("Балакирев"))
# ln.add_obj(ObjList("Python ООП"))
# ln.remove_obj(2)
# assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
# ln.add_obj(ObjList("Python"))
# assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
# assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
# assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"
#
# n = 0
# h = ln.head
# while h:
#     assert isinstance(h, ObjList)
#     h = h._ObjList__next
#     n += 1
#
# assert n == 3, "при перемещении по списку через __next не все объекты перебрались"
#
# n = 0
# h = ln.tail
# while h:
#     assert isinstance(h, ObjList)
#     h = h._ObjList__prev
#     n += 1
#
# assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"


'''ANOTHER WAY'''

# class Desc:
#     def __set_name__(self, owner, name):
#         self.name = f'_{owner.__name__}__{name}'
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         instance.__dict__[self.name] = value
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def add_obj(self, obj):
#         if not self.head:
#             self.head = obj
#             self.tail = obj
#         else:
#             self.tail.next = obj
#             obj.prev = self.tail
#             self.tail = obj
#
#     def remove_obj(self, indx):
#         c = 0
#         tmp = self.head
#         while c != indx:
#             c += 1
#             tmp = tmp.next
#
#         if tmp.next and tmp.prev:
#             tmp.next.prev = tmp.prev
#             tmp.prev = tmp.next
#
#         elif tmp == self.head == self.tail:
#             self.head = self.tail = None
#
#         elif tmp == self.head:
#             tmp.next.prev = None
#             self.head = tmp.next
#
#         elif tmp == self.tail:
#             tmp.prev.next = None
#             self.tail = tmp.prev
#
#     def __len__(self):
#         c = 1 if self.head else 0
#         tmp = self.head
#         while tmp.next:
#             c += 1
#             tmp = tmp.next
#         return c
#
#     def __call__(self, indx):
#         c = 0
#         tmp = self.head
#         while c != indx:
#             c += 1
#             tmp = tmp.next
#         return tmp.data
#
#
# class ObjList:
#     data = Desc()
#     prev = Desc()
#     next = Desc()
#
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None



# =============================================================================




# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/t8KuHjY71-o
# Подвиг 6. Объявите класс с именем Complex для представления и работы с комплексными числами. Объекты этого класса должны создаваться командой:
# cm = Complex(real, img)
# где real - действительная часть комплексного числа (целое или вещественное значение); img - мнимая часть комплексного числа
# (целое или вещественное значение).
# Объявите в этом классе следующие объекты-свойства (property):
# real - для записи и считывания действительного значения;
# img - для записи и считывания мнимого значения.
# При записи новых значений необходимо проверять тип передаваемых данных. Если тип не соответствует целому или вещественному
# числу, то генерировать исключение командой:
# raise ValueError("Неверный тип данных.")
# Также с объектами класса Complex должна поддерживаться функция:
# res = abs(cm)
# возвращающая модуль комплексного числа (вычисляется по формуле: sqrt(real*real + img*img) - корень квадратный от суммы
# квадратов действительной и мнимой частей комплексного числа).
# Создайте объект cmp класса Complex для комплексного числа с real = 7 и img = 8. Затем, через объекты-свойства real и img
# измените эти значения на real = 3 и img = 4. Вычислите модуль полученного комплексного числа (сохраните результат в переменной c_abs).
# P.S. На экран ничего выводить не нужно.

# class Complex:
#     def __init__(self, real, img):
#         self.__real = real
#         self.__img = img
#
#     @property
#     def real(self):
#         return self.__real
#     @real.setter
#     def real(self, real):
#         if type(real) in (int, float):
#             self.__real = real
#         else:
#             raise ValueError("Неверный тип данных.")
#
#     @property
#     def img(self):
#         return self.__img
#     @img.setter
#     def img(self, img):
#         if type(img) in (int, float):
#             self.__img = img
#         else:
#             raise ValueError("Неверный тип данных.")
#
#     def __abs__(self):
#         return (self.__real*self.__real + self.__img*self.__img) ** 0.5
#
# cmp = Complex(7,8)
# cmp.real = 3
# cmp.img = 4
# c_abs = abs(cmp)



# ============================================================================================================


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/lCYllyv9nVM
# Подвиг 7. Объявите класс с именем RadiusVector для описания и работы с n-мерным вектором (у которого n координат).
# Объекты этого класса должны создаваться командами:
# # создание 5-мерного радиус-вектора с нулевыми значениями координат (аргумент - целое число больше 1)
# vector = RadiusVector(5)  # координаты: 0, 0, 0, 0, 0
# # создание 4-мерного радиус-вектора с координатами: 1, -5, 3.4, 10 (координаты - любые целые или вещественные числа)
# vector = RadiusVector(1, -5, 3.4, 10)
# То есть, при передаче одного значения, оно интерпретируется, как размерность нулевого радиус-вектора. Если же
# передается более одного числового аргумента, то они интерпретируются, как координаты радиус-вектора.
# Класс RadiusVector должен содержать методы:
# set_coords(coord_1, coord_2, ..., coord_N) - для изменения координат радиус-вектора;
# get_coords() - для получения текущих координат радиус-вектора (в виде кортежа).
# Также с объектами класса RadiusVector должны поддерживаться следующие функции:
# len(vector) - возвращает число координат радиус-вектора (его размерность);
# abs(vector) - возвращает длину радиус-вектора (вычисляется как: sqrt(coord_1*coord_1 + coord_2*coord_2 + ... +
#                                                                      coord_N*coord_N) - корень квадратный из суммы квадратов координат).
# Пример использования класса RadiusVector (эти строчки в программе писать не нужно):
# vector3D = RadiusVector(3)
# vector3D.set_coords(3, -5.6, 8)
# a, b, c = vector3D.get_coords()
# vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
# vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
# res_len = len(vector3D) # res_len = 3
# res_abs = abs(vector3D)
# P.S. На экран ничего выводить не нужно, только объявить класс RadiusVector


# class RadiusVector:
#     def __init__(self, *args):
#         if len(args) == 1:
#             self.__coords = (0,) * args[0]
#         else:
#             self.__coords = args
#
#     def __str__(self):
#         return str(self.__coords)
#
#     def set_coords(self, *args):
#         lst = list(self.__coords)
#         length = len(args) if len(lst) >= len(args) else len(lst)
#         for ind in range(length):
#             lst[ind] = args[ind]
#         self.__coords = tuple(lst)
#
#     def get_coords(self):
#         return self.__coords
#
#     def __len__(self):
#         return len(self.__coords)
#
#     def __abs__(self):
#         return sum(map(lambda x: x * x, self.__coords)) ** 0.5
#
#
# # s = RadiusVector(5)
# # print(s)
# # s = RadiusVector(1,2,3,4)
# # print(s)
#
# vector3D = RadiusVector(3)
# vector3D.set_coords(3, -5.6, 8)
# a, b, c = vector3D.get_coords()
# print(a, b, c)
# vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
# print(vector3D.get_coords())
# vector3D.set_coords(1, -2) # ошибки быть не должно, меняются только первые две координаты
# print(vector3D.get_coords())
# res_len = len(vector3D) # res_len = 3
# res_abs = abs(vector3D)
# print(res_abs)





# ==============================================================================================================




# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/V7SV1pOWyEY
# Подвиг 8. Объявите класс DeltaClock для вычисления разницы времен. Объекты этого класса должны создаваться командой:
# dt = DeltaClock(clock1, clock2)
# где clock1, clock2 - объекты другого класса Clock для хранения текущего времени. Эти объекты должны создаваться командой:
# clock = Clock(hours, minutes, seconds)
# где hours, minutes, seconds - часы, минуты, секунды (целые неотрицательные числа).
# В классе Clock также должен быть (по крайней мере) один метод (возможны и другие):
# get_time() - возвращает текущее время в секундах (то есть, значение hours * 3600 + minutes * 60 + seconds).
# После создания объекта dt класса DeltaClock, с ним должны выполняться команды:
# str_dt = str(dt)   # возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
# len_dt = len(dt)   # разницу времен clock1 - clock2 в секундах (целое число)
# print(dt)   # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
# Если разность получается отрицательной, то разницу времен считать нулевой.
# Пример использования классов (эти строчки в программе писать не нужно):
# dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
# print(dt) # 01: 30: 00
# len_dt = len(dt) # 5400
# Обратите внимание, добавляется незначащий ноль, если число меньше 10.
# P.S. На экран ничего выводить не нужно, только объявить классы.

# class DeltaClock:
#     def __init__(self, clock1, clock2):
#         self.__clock1 = clock1
#         self.__clock2 = clock2
#
#     def __str__(self):
#         sec = self.__clock1.get_time() - self.__clock2.get_time()
#         if sec <=0:
#             return '00: 00: 00'
#         else:
#             h = sec // 3600
#             m = sec % 3600 // 60
#             s = sec % 3600 % 60
#             h = f'0{h}' if h < 10 else h
#             m = f'0{m}' if m < 10 else m
#             s = f'0{s}' if s < 10 else s
#             return f'{h}: {m}: {s}'
#
#     def __len__(self):
#         return self.__clock1.get_time() - self.__clock2.get_time()
#
#
#
# class Clock:
#     def __init__(self, hours, minutes, seconds):
#         self.__hours = hours
#         self.__minutes = minutes
#         self.__seconds = seconds
#
#     def get_time(self):
#         return self.__hours * 3600 + self.__minutes * 60 + self.__seconds
#
#
#
# dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
# print(dt) # 01: 30: 00
# len_dt = len(dt) # 5400
# print(len_dt)

# =======================================================================================================


# Подвиг 9. Объявите класс Recipe для представления рецептов. Отдельные ингредиенты рецепта должны определяться классом
# Ingredient. Объекты этих классов должны создаваться командами:
# ing = Ingredient(name, volume, measure)
# recipe = Recipe()
# recipe = Recipe(ing_1, ing_2,..., ing_N)
# где ing_1, ing_2,..., ing_N - объекты класса Ingredient.
# В каждом объекте класса Ingredient должны создаваться локальные атрибуты:
# name - название ингредиента (строка);
# volume - объем ингредиента в рецепте (вещественное число);
# measure - единица измерения объема ингредиента (строка), например, литр, чайная ложка, грамм, штук и т.д.;
# С объектами класса Ingredient должна работать функция:
# str(ing)  # название: объем, ед. изм.
# и возвращать строковое представление объекта в формате:
# "название: объем, ед. изм."
# Например:
# ing = Ingredient("Соль", 1, "столовая ложка")
# s = str(ing) # Соль: 1, столовая ложка
# Класс Recipe должен иметь следующие методы:
# add_ingredient(ing) - добавление нового ингредиента ing (объект класса Ingredient) в рецепт (в конец);
# remove_ingredient(ing) - удаление ингредиента по объекту ing (объект класса Ingredient) из рецепта;
# get_ingredients() - получение кортежа из объектов класса Ingredient текущего рецепта.
# Также с объектами класса Recipe должна поддерживаться функция:
# len(recipe) - возвращает число ингредиентов в рецепте.
# Пример использования классов (эти строчки в программе писать не нужно):
# recipe = Recipe()
# recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
# recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
# recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
# ings = recipe.get_ingredients()
# n = len(recipe) # n = 3
# P.S. На экран ничего выводить не нужно, только объявить классы.



# class Recipe:
#     def __init__(self, *args):
#         if args:
#             self.__recipe = list(args)
#         else:
#             self.__recipe = []
#
#     def __len__(self):
#         return len(self.__recipe)
#
#     def add_ingredient(self, ing):
#         self.__recipe.append(ing)
#
#     def remove_ingredient(self, ing):
#         self.__recipe.remove(ing)
#
#     def get_ingredients(self):
#         return tuple(self.__recipe)
#
# class Ingredient:
#     def __init__(self, name, volume, measure):
#         self.name = name
#         self.volume = volume
#         self.measure = measure
#
#     def __str__(self):
#         return f'{self.name}: {self.volume}, {self.measure}'

# ing = Ingredient("Соль", 1, "столовая ложка")
# s = str(ing) # Соль: 1, столовая ложка
# print(s)

# recipe = Recipe()
# recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
# recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
# recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
# ings = recipe.get_ingredients()
# n = len(recipe) # n = 3
# print(ings)
# print(n)


# TESTS

# i1 = Ingredient("Соль", 1, "столовая ложка")
# i2 = Ingredient("Мука", 1, "кг")
# i3 = Ingredient("Мясо баранины", 10, "кг")
# i4 = Ingredient("Масло", 100, "гр")
# recipe = Recipe(i1, i2, i3)
# recipe.add_ingredient(i4)
# recipe.remove_ingredient(i3)
#
# assert len(recipe) == 3, "функция len вернула неверное значение"
# lst = recipe.get_ingredients()
# for x in lst:
#     assert isinstance(x, Ingredient), "в списке рецептов должны быть только объекты класса Ingredient"
#     assert hasattr(x, 'name') and hasattr(x, 'volume') and hasattr(x, 'measure'), "объект класса Ingredient должен иметь атрибуты: name, volume, measure"
#
# assert str(i4) == "Масло: 100, гр", "метод __str__ вернул неверное значение"
#
# i4 = Ingredient("Масло", 120, "гр")
# recipe.add_ingredient(i4)
# assert len(recipe) == 4, "функция len вернула неверное значение"



# ===================================================================================================




# Подвиг 10 (на повторение). Объявите класс PolyLine (полилиния) для представления линии из последовательности прямолинейных сегментов.
# Объекты этого класса должны создаваться командой:
# poly = PolyLine(start_coord, coord_2, coord_3, ..., coord_N)
# Здесь start_coord - координата начала полилинии (кортеж из двух чисел x, y); coord_2, coord_3, ... -
# последующие координаты точек на плоскости (представленные кортежами), соединенных прямыми линиями.
# Например:
# poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
# В классе PolyLine должны быть объявлены следующие методы:
# add_coord(x, y) - добавление новой координаты (в конец);
# remove_coord(indx) - удаление координаты по индексу (порядковому номеру, начинается с нуля);
# get_coords() - получение списка координат (в виде списка из кортежей).
# P.S. На экран ничего выводить не нужно, только объявить класс.

# class PolyLine:
#     def __init__(self, *args):
#         self.__args = list(args)
#
#     def add_coord(self, x, y):
#         self.__args.append((x, y))
#
#     def remove_coord(self, indx):
#         self.__args.pop(indx)
#
#     def get_coords(self):
#         return self.__args


# poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
# print(poly.get_coords())
#
# poly.add_coord(4,6)
# poly.remove_coord(3)
# print(poly.get_coords())