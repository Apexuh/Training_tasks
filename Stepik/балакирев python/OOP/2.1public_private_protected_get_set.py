#без подчеркивания - публичное свойство
# _ - protected (для обращения внутри класса и дочерних) свойства предостерегают, но не оберегают от доступа извне
#  __ - private ( доступ только внутри класса)
#

# class Point:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if self.__check_value(x) and self.__check_value(y): #проверка на правильность введенных данных
#             self.__x = x
#             self.__y = y
#
#     @classmethod
#     def __check_value(cls, x):#сделаем методом класса,тк нужно иметь возможность обращаться к элементам класса
#         return type(x) in (int, float)
#
#     def set_coords(self, x , y):
#         if self.__check_value(x) and self.__check_value(y): #проверка на правильность введенных данных
#             self.__x = x
#             self.__y = y
#         else:
#             raise ValueError('введите число')
#     def get_coords(self):
#         return self.__x, self.__y
#     # геттеры и сеттеры - интерфейсные методы, если есть приватные данные(__), то требуется обращаться через них
#
# pt = Point(10, 20)
# print(pt.get_coords())
# pt.set_coords(11, 30)
# print(pt.get_coords())
# print(pt.__dir__()) #'_Point__x', '_Point__y'  -кодовые имена x и y


# также есть модуль accessify
# from accessify import private, protected
#
# class Point:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if self.check_value(x) and self.check_value(y): #проверка на правильность введенных данных
#             self.__x = x
#             self.__y = y
#
#     @private #декоратор до обозначения методом класса. с ним можно без подчеркиваний
#     @classmethod
#     def check_value(cls, x):#сделаем методом класса,тк нужно иметь возможность обращаться к элементам класса
#         return type(x) in (int, float)
#
#     def set_coords(self, x , y):
#         if self.check_value(x) and self.check_value(y): #проверка на правильность введенных данных
#             self.__x = x
#             self.__y = y
#         else:
#             raise ValueError('введите число')
#     def get_coords(self):
#         return self.__x, self.__y
#     # геттеры и сеттеры - интерфейсные методы, если есть приватные данные(__), то требуется обращаться через них
#
# pt = Point(10, 20)
# # print(pt.get_coords())
# # pt.set_coords(11, 30)
# # print(pt.get_coords())
# # print(pt.__dir__()) #'_Point__x', '_Point__y'  -кодовые имена x и y
#
# print(pt.check_value(1)) #ошибка доступа с декоратором(как надо), доступ без него






# Подвиг 3. Объявите класс с именем Clock и определите в нем следующие переменные и методы:
# - приватная локальная переменная time для хранения текущего времени, целое число (своя для каждого объекта класса Clock с начальным значением 0);
# - публичный метод set_time(tm) для установки текущего времени (присваивает значение tm приватному локальному свойству
# time, если метод check_time(tm) возвратил True);
# - публичный метод get_time() для получения текущего времени из приватной локальной переменной time;
# - приватный метод класса check_time(tm) для проверки корректности времени в переменной tm (возвращает True, если
# значение корректно и False - в противном случае).
# Проверка корректности выполняется по критерию: tm должна быть целым числом, больше или равна нулю и меньше 100 000.
# Объекты класса Clock предполагается использовать командой:
# clock = Clock(время)
# Создайте объект clock класса Clock и установите время, равным 4530.
# P.S. На экран ничего выводить не нужно.


# class Clock:
#     def __init__(self, time = 0):
#         if self._check_time(time):
#             self.time = time
#
#     def _check_time(self, x):
#         if type(x) is int and 0 <= x <= 100000:
#             return True
#         else:
#             return False
#
#     def set_time(self, tm):
#         if self._check_time(tm):
#             self.time = tm
#
#     def get_time(self):
#         return self.time

#
# clock = Clock(4530)







# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/iYcfCeRTyww
# Подвиг 4. Объявите класс с именем Money и определите в нем следующие переменные и методы:
# - приватная локальная переменная money (целочисленная) для хранения количества денег (своя для каждого объекта класса Money);
# - публичный метод set_money(money) для передачи нового значения приватной локальной переменной money (изменение
# выполняется только если метод check_money(money) возвращает значение True);
# - публичный метод get_money() для получения текущего объема средств (денег);
# - публичный метод add_money(mn) для прибавления средств из объекта mn класса Money к средствам текущего объекта;
# - приватный метод класса check_money(money) для проверки корректности объема средств в параметре money (возвращает True,
# если значение корректно и False - в противном случае).
# Проверка корректности выполняется по критерию: параметр money должен быть целым числом, больше или равным нулю.
# Пример использования класса Money (эти строчки в программе не писать):
# mn_1 = Money(10)
# mn_2 = Money(20)
# mn_1.set_money(100)
# mn_2.add_money(mn_1)
# m1 = mn_1.get_money()    # 100
# m2 = mn_2.get_money()    # 120



# class Money:
#     def __init__(self, money):
#         if self.__check_money(money):
#             self.__money = money
#
#     def __check_money(self, x):
#         if type(x) is int and x >= 0:
#             return True
#
#     def set_money(self, money):
#         if self.__check_money(money):
#             self.__money = money
#
#     def get_money(self):
#         return self.__money
#
#     def add_money(self, mn):
#         self.__money += mn.__money

# mn_1 = Money(10)
# mn_2 = Money(20)
# # print(mn_1._Money__money)
# mn_1.set_money(100)
# # print(mn_1._Money__money)
#
# mn_2.add_money(mn_1)
# # print(mn_1._Money__money)
# # print(mn_2._Money__money)
# m1 = mn_1.get_money()    # 100
# m2 = mn_2.get_money()    # 120
# print(m1)
# print(m2)


# mn_1 = Money(10)
# mn_2 = Money(20)
# assert mn_1._Money__money == 10 and mn_2._Money__money == 20, "неверные значения в локальном приватном атрибуте __money"
#
# mn_1.set_money(100)
# mn_2.add_money(mn_1)
# print(mn_1.get_money())
# print(mn_2.get_money())
# assert mn_1.get_money() == 100 and mn_2.get_money() == 120, "неверное количество средств: возможно некорректая работа методов set_money и/или add_money"
#
# mn_1.set_money(-1)
# assert mn_1.get_money() == 100, "неверное количество средств: некорректная работа метода set_money"






# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/w0SAD6zNLlw
# Подвиг 6. Объявите класс Book со следующим набором сеттеров и геттеров:
# set_title(self, title) - запись в локальное приватное свойство __title объектов класса Book значения title;
# set_author(self, author) - запись в локальное приватное свойство __author объектов класса Book значения author;
# set_price(self, price) - запись в локальное приватное свойство __price объектов класса Book значения price;
# get_title(self) - получение значения локального приватного свойства __title объектов класса Book;
# get_author(self) - получение значения локального приватного свойства __author объектов класса Book;
# get_price(self) - получение значения локального приватного свойства __price объектов класса Book;
# Объекты класса Book предполагается создавать командой:
# book = Book(автор, название, цена)
# При этом, в каждом объекте должны создаваться приватные локальные свойства:
# __author - строка с именем автора;
# __title - строка с названием книги;
# __price - целое число с ценой книги.
# P.S. В программе требуется объявить только класс. Ничего на экран выводить не нужно.

# class Book:
#     def __init__(self, author, title, price):
#         if type(title) == type(author) == str and self.__check_price(price):
#             self.__title = title
#             self.__author = author
#             self.__price = price
#
#     def __check_price(self, price):
#         if type(price) is int:
#             return True
#     def set_title(self, title):
#         '''- запись в локальное приватное свойство __title объектов класса Book значения title;'''
#         self.__title = title
#     def set_author(self, author):
#         '''- запись в локальное приватное свойство __author объектов класса Book значения author;'''
#         self.__author = author
#     def set_price(self, price):
#         ''' - запись в локальное приватное свойство __price объектов класса Book значения price;'''
#         if self.__check_price(price):
#             self.__price = price
#     def get_title(self):
#         '''- получение значения локального приватного свойства __title объектов класса Book;'''
#         return self.__title
#     def get_author(self):
#         '''- получение значения локального приватного свойства __author объектов класса Book;'''
#         return self.__author
#     def get_price(self):
#         ''' - получение значения локального приватного свойства __price объектов класса Book;'''
#         return self.__price
#
#
# book = Book('50 Cent', 'Aboba', 999)
# book.set_title('Amogus')
# book.set_author('NLE Choppa')
# book.set_price(123)
# book.get_title()
# book.get_author()
# book.get_price()
# print(book.get_author())









# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/ZX8fVI0KTfE
# Подвиг 7. Объявите класс Line для описания линии на плоскости, объекты которого предполагается создавать командой:
# line = Line(x1, y1, x2, y2)
# При этом в объекте line должны создаваться следующие приватные локальные свойства:
# __x1, __y1 - начальная координата;
# __x2, __y2 - конечная координата.
# В самом классе Line должны быть реализованы следующие сеттеры и геттеры:
# set_coords(self, x1, y1, x2, y2) - для изменения координат линии;
# get_coords(self) - для получения кортежа из текущих координат линии.
# А также метод:
# draw(self) - для отображения в консоли списка текущих координат линии (в одну строчку через пробел).
# P.S. В программе требуется объявить только класс. Ничего на экран выводить не нужно.

# class Line:
#     def __init__(self, *args):
#         self.__x1, self.__y1, self.__x2, self.__y2 = args
#
#     def set_coords(self, x1, y1, x2, y2):
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__x2 = x2
#         self.__y2 = y2
#
#     def get_coords(self):
#         return self.__x1, self.__y1, self.__x2, self.__y2
#
#     def draw(self):
#         lst = map(lambda x: str(x), [self.__x1, self.__y1, self.__x2, self.__y2])
#         print(' '.join(lst))
#
# d = Line(1,2,3,4)
# print(d.get_coords())
# d.draw()







# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/rcj0pB1aB5M
# Подвиг 8. Объявите в программе два класса Point и Rectangle. Объекты первого класса должны создаваться командой:
# pt = Point(x, y)
# где x, y - координаты точки на плоскости (целые или вещественные числа). При этом в объектах класса Point должны
# формироваться следующие локальные свойства:
# __x, __y - координаты точки на плоскости.
# и один геттер:
# get_coords() - возвращение кортежа текущих координат __x, __y
# Объекты второго класса Rectangle (прямоугольник) должны создаваться командами:
# r1 = Rectangle(Point(x1, y1), Point(x2, y2))
# или
# r2 = Rectangle(x1, y1, x2, y2)
# Здесь первая координата (x1, y1) - верхний левый угол, а вторая координата (x2, y2) - правый нижний. При этом,
# в объектах класса Rectangle (вне зависимости от способа их создания) должны формироваться следующие локальные свойства:
# __sp - объект класса Point с координатами x1, y1 (верхний левый угол);
# __ep - объект класса Point с координатами x2, y2 (нижний правый угол).
# Также к классе Rectangle должны быть реализованы следующие методы:
# set_coords(self, sp, ep) - изменение текущих координат, где sp, ep - объекты класса Point;
# get_coords(self) - возвращение кортежа из объектов класса Point с текущими координатами прямоугольника (ссылки на локальные свойства __sp и __ep);
# draw(self) - отображение в консоли сообщения: "Прямоугольник с координатами: (x1, y1) (x2, y2)". Здесь x1, y1, x2, y2 - соответствующие числовые значения координат.
# Создайте объект rect класса Rectangle с координатами (0, 0), (20, 34).
# P.S. На экран ничего выводить не нужно.
from cmath import rect


# class Point:
#     def __init__(self, x, y):
#         if self.__check_coord(x) and self.__check_coord(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_coord(self, x):
#         if type(x) in (int, float):
#             return True
#
#     def get_coords(self):
#         return self.__x, self.__y
#
# class Rectangle:
#     def __init__(self, *args):
#         if len(args) == 2:
#             self.__sp, self.__ep = args[0], args[1]
#         elif len(args) == 4:
#             self.__sp, self.__ep = args[:2], args[2:]
#
#     def set_coords(self, sp, ep):
#         self.__sp = sp
#         self.__ep = ep
#
#     def get_coords(self):
#         return self.__sp, self.__ep
#
#     def draw(self):
#         print(f"Прямоугольник с координатами: {self.__sp} {self.__ep}")
#
#
# rect = Rectangle(Point(0, 0), Point(20, 34))


# assert isinstance(rect, Rectangle) and hasattr(Rectangle, 'set_coords') and hasattr(Rectangle, 'get_coords') and hasattr(Rectangle, 'draw'), "в классе Rectangle присутствуют не все методы"

# r = Rectangle(1, 2.6, 3.3, 4)
# r.set_coords(Point(1, 2), Point(3, 4))
# sp, ep = r.get_coords()
# a, b = sp.get_coords()
# c, d = ep.get_coords()
# assert a == 1 and b == 2 and c == 3 and d == 4, "метод get_coords вернул неверные значения координат"
#
# r = Rectangle(Point(1, 2), Point(3, 4))
# sp, ep = r.get_coords()
# a, b = sp.get_coords()
# c, d = ep.get_coords()
# assert a == 1 and b == 2 and c == 3 and d == 4, "метод get_coords вернул неверные значения координат"

# assert isinstance(r._Rectangle__sp, Point) and isinstance(r._Rectangle__ep, Point), "атрибуты __sp и __ep должны ссылаться на объекты класса Point"







# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/YJiPpHVguyE
# Большой подвиг 9. Необходимо реализовать связный список (не список языка Python и не хранить объекты в списке Python),
# когда объекты класса ObjList связаны с соседними через приватные свойства __next и __prev:
# Для этого объявите класс LinkedList, который будет представлять связный список в целом и иметь набор следующих методов:
# add_obj(self, obj) - добавление нового объекта obj класса ObjList в конец связного списка;
# remove_obj(self) - удаление последнего объекта из связного списка;
# get_data(self) - получение списка из строк локального свойства __data всех объектов связного списка.
# И в каждом объекте этого класса должны создаваться локальные публичные атрибуты:
# head - ссылка на первый объект связного списка (если список пустой, то head = None);
# tail - ссылка на последний объект связного списка (если список пустой, то tail = None).
# Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:
# __next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
# __prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
# __data - строка с данными.
# Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:
# set_next(self, obj) - изменение приватного свойства __next на значение obj;
# set_prev(self, obj) - изменение приватного свойства __prev на значение obj;
# get_next(self) - получение значения приватного свойства __next;
# get_prev(self) - получение значения приватного свойства __prev;
# set_data(self, data) - изменение приватного свойства __data на значение data;
# get_data(self) - получение значения приватного свойства __data.
# Создавать объекты класса ObjList предполагается командой:
# ob = ObjList("данные 1")
# А использовать класс LinkedList следующим образом (пример, эти строчки писать в программе не нужно):
# lst = LinkedList()
# lst.add_obj(ObjList("данные 1"))
# lst.add_obj(ObjList("данные 2"))
# lst.add_obj(ObjList("данные 3"))
# res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
# Объявите в программе классы LinkedList и ObjList в соответствии с заданием.
# P.S. На экран ничего выводить не нужно.



