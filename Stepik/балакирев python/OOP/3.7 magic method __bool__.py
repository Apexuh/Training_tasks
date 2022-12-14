# __len__ вызывается функцией bool() если не определен магический метод __bool__
# __bool__ вызывается приоритетно функцией bool()
# правдивость класса- когда к функции класса явно или неявно применется функция bool()
# bool(123) - true
# bool(-1) - true
# bool(0) - false


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     # def __len__(self):
#     #     print('__len__')
#     #     return self.x ** 2 + self.y ** 2
#
#     def __bool__(self):
#         print('__bool__')
#         return self.x == self.y # сделаем так, чтобы возвращался True,если х и у равны
#
# p = Point(3, 4)
# print(bool(p)) #True . при применении к обьектам позьзовательского класса изначально всегда True,надо переопределать через __len__ or __bool__
# # p1 = Point(0,0) #после переопределения bool  будет True, до переопределения False. А обьект р будет давать False
# # print(bool(p1))
#
# # как используется в основном?:
# # if p1:
# #     print('Обьект р1 дает True')
# # else:
# #     print('обьект р1 дает False')
#
# if p:
#     print('Обьект р дает True')
# else:
#     print('обьект р дает False')
# print(p)



# ===================================================================================================




# Подвиг 4. Объявите в программе класс Player (игрок), объекты которого создаются командой:
# player = Player(name, old, score)
# где name - имя игрока (строка); old - возраст игрока (целое число); score - набранные очки в игре (целое число).
# В каждом объекте класса Player должны создаваться аналогичные локальные атрибуты: name, old, score.
# С объектами класса Player должна работать функция:
# bool(player)
# которая возвращает True, если число очков больше нуля, и False - в противном случае.
# С помощью команды:
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# считываются строки из входного потока в список строк lst_in. Каждая строка записана в формате:
# "имя; возраст; очки"
# Например:
# Балакирев; 34; 2048
# Mediel; 27; 0
# Влад; 18; 9012
# Nina P; 33; 0
# Каждую строку списка lst_in необходимо представить в виде объекта класса Player с соответствующими данными.
# И из этих объектов сформировать список players.
# Отфильтруйте этот список (создайте новый: players_filtered), оставив всех игроков с числом очков больше нуля.
# Используйте для этого стандартную функцию filter() совместно с функцией bool() языка Python. 
# P.S. На экран ничего выводить не нужно.
# Sample Input:
# Балакирев; 34; 2048
# Mediel; 27; 0
# Влад; 18; 9012
# Nina P; 33; 0
# Sample Output:

# class Player:
#     def __init__(self, name, old, score):
#         self.name = name
#         self.old = int(old)
#         self.score = int(score)
#
#     def __bool__(self):
#         return self.score > 0
#
# # lst_in = ['Балакирев; 34; 2048', 'Mediel; 27; 0', 'Влад; 18; 9012', 'Nina P; 33; 0']
# players = list(map(lambda x: Player(*x.split('; ')), lst_in))
# # print(players)
# players_filtered = list(filter(bool, players))
# # print(players_filtered)


# ======================================================================================================

# Подвиг 5. Объявите в программе класс MailBox (почтовый ящик), объекты которого создаются командой:
# mail = MailBox()
# Каждый объект этого класса должен содержать локальный публичный атрибут:
# inbox_list - список из принятых писем.
# Также в классе MailBox должен присутствовать метод:
# receive(self) - прием новых писем
# Этот метод должен читать данные из входного потока командой:
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# В результате формируется список lst_in из строк. Каждая строка записана в формате:
# "от кого; заголовок; текст письма"
# Например:
# sc_lib@list.ru; От Балакирева; Успехов в IT!
# mail@list.ru; Выгодное предложение; Вам одобрен кредит.
# mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.
# Каждая строчка списка lst_in должна быть представлена объектом класса MailItem, объекты которого создаются командой:
# item = MailItem(mail_from, title, content)
# где mail_from - email отправителя (строка); title - заголовок письма (строка), content - содержимое письма (строка).
# В каждом объекте класса MailItem должны формироваться соответствующие локальные атрибуты (с именами: mail_from, title, content).
# И дополнительно атрибут is_read (прочитано ли) с начальным значением False.
# В классе MailItem должен быть реализован метод:
# set_read(self, fl_read) - для отметки, что письмо прочитано (метод должен устанавливать атрибут is_read = fl_read, если True,
# то письмо прочитано, если False, то не прочитано).
# С каждым объектом класса MailItem должна работать функция:
# bool(item)
# которая возвращает True для прочитанного письма и False для непрочитанного.
# Вызовите метод:
# mail.receive()
# Отметьте первое и последнее письмо в списке mail.inbox_list, как прочитанное (используйте для этого метод set_read).
# Затем, сформируйте в программе список (глобальный) с именем inbox_list_filtered из прочитанных писем, используя стандартную
# функцию filter() совместно с функцией bool() языка Python.
# P.S. На экран ничего выводить не нужно.
# Sample Input:
# sc_lib@list.ru; От Балакирева; Успехов в IT!
# mail@list.ru; Выгодное предложение; Вам одобрен кредит.
# mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.
# Sample Output:

# import sys
#
# class MailBox:
#     def __init__(self):
#         self.inbox_list = []
#
#     def receive(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))
#         self.inbox_list.extend(list(map(lambda x: MailItem(*x.split('; ')), lst_in)))
#
#
# class MailItem:
#     def __init__(self, mail_from, title, content):
#         self.mail_from = mail_from
#         self.title = title
#         self.content = content
#         self.is_read = False
#
#     def set_read(self, fl_read=False):
#         self.is_read = fl_read
#
#     def __bool__(self):
#         return self.is_read
#
# # lst_in = ['sc_lib@list.ru; От Балакирева; Успехов в IT!', 'mail@list.ru; Выгодное предложение; Вам одобрен кредит.',
# # 'mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.']
#
# mail = MailBox()
# mail.receive()
# # print(mail.inbox_list)
# mail.inbox_list[0].set_read(True)
# mail.inbox_list[-1].set_read(True)
# inbox_list_filtered = list(filter(bool, mail.inbox_list))
# # print(inbox_list_filtered)
#
#


# =============================================================================================




# Подвиг 6 (релакс). Объявите класс Line, объекты которого создаются командой:
# line = Line(x1, y1, x2, y2)
# где x1, y1, x2, y2 - координаты начала линии (x1, y1) и координаты конца линии (x2, y2).
# Могут быть произвольными числами. В объектах класса Line должны создаваться соответствующие локальные атрибуты с именами x1, y1, x2, y2.
# В классе Line определить магический метод __len__() так, чтобы функция:
# bool(line)
# возвращала False, если длина линии меньше 1.
# P.S. На экран ничего выводить не нужно. Только объявить класс.

# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#
#     # def __bool__(self):
#     #     return True if ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5 >= 1 else False
#
#     def __len__(self):
#         s = int(((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5)
#         return s
#
#     def __bool__(self):
#         return len(self) >= 1

# line = Line(1,2,6,5)
# print(bool(line))


# ====================================================================================================




# Подвиг 7. Объявите класс Ellipse (эллипс), объекты которого создаются командами:
# el1 = Ellipse()  # без создания локальных атрибутов x1, y1, x2, y2
# el2 = Ellipse(x1, y1, x2, y2)
# где x1, y1 - координаты (числа) левого верхнего угла; x2, y2 - координаты (числа) нижнего правого угла.
# Первая команда создает объект класса Ellipse без локальных атрибутов x1, y1, x2, y2. Вторая команда создает
# объект с локальными атрибутами x1, y1, x2, y2 и соответствующими переданными значениями.
# В классе Ellipse объявите магический метод __bool__(), который бы возвращал True, если все локальные атрибуты
# x1, y1, x2, y2 существуют и False - в противном случае.
# Также в классе Ellipse нужно реализовать метод:
# get_coords() - для получения кортежа текущих координат объекта.
# Если координаты отсутствуют (нет локальных атрибутов x1, y1, x2, y2), то метод get_coords() должен генерировать исключение командой:
# raise AttributeError('нет координат для извлечения')
# Сформируйте в программе список с именем lst_geom, содержащий четыре объекта класса Ellipse. Два объекта должны быть созданы командой 
# Ellipse()
# и еще два - командой:
# Ellipse(x1, y1, x2, y2)
# Переберите список в цикле и вызовите метод get_coords() только для объектов, имеющих координаты x1, y1, x2, y2.
# (Помните, что для этого был определен магический метод __bool__()).
# P.S. На экран ничего выводить не нужно.


# class Ellipse:
#     def __init__(self, *args):
#         if args:
#             if len(args) == 4:
#                 self.x1 = args[0]
#                 self.y1 = args[1]
#                 self.x2 = args[2]
#                 self.y2 = args[3]
#
#     def test_data(self):
#         try:
#             s = self.x1, self.y1, self.x2, self.y2
#             return True
#         except:
#             return False
#
#     def __bool__(self):
#         return self.test_data()
#
#     def get_coords(self):
#         try:
#             return self.x1, self.y1, self.x2, self.y2
#         except:
#             raise AttributeError('нет координат для извлечения')
# # el1 = Ellipse()  # без создания локальных атрибутов x1, y1, x2, y2
# # el2 = Ellipse('x1', 'y1', 'x2', 'y2')
# # print(bool(el1))
# # print(el1.get_coords())
# # print(bool(el2))
# # print(el2.get_coords())
# s = Ellipse(1, 2, 3, 4)
# lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]
# for i in lst_geom:
#     if bool(i):
#         i.get_coords()





# =======================================================================================================




# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/2lnbu3n7Y_w
# Большой подвиг 8. Вы начинаете разрабатывать игру "Сапер". Для этого вам нужно уметь представлять и управлять игровым полем.
# Будем полагать, что оно имеет размеры N x M клеток. Каждая клетка будет представлена объектом класса Cell и содержать либо число
# мин вокруг этой клетки, либо саму мину.
# Для начала в программе объявите класс GamePole, который будет создавать и управлять игровым полем. Объект этого класса должен формироваться командой:
# pole = GamePole(N, M, total_mines)
# И, так как поле в игре одно, то нужно контролировать создание только одного объекта класса GamePole (используйте паттерн Singleton,
# о котором мы с вами говорили, когда рассматривали магический метод __new__()).
# Объект pole должен иметь локальный приватный атрибут:
# __pole_cells - двумерный (вложенный) кортеж, размерами N x M элементов (N строк и M столбцов), состоящий из объектов класса Cell.
# Для доступа к этой коллекции объявите в классе GamePole объект-свойство (property):
# pole - только для чтения (получения) ссылки на коллекцию __pole_cells.
# Далее, в самом классе GamePole объявите следующие методы:
# init_pole() - для инициализации начального состояния игрового поля (расставляет мины и делает все клетки закрытыми);
# open_cell(i, j) - открывает ячейку с индексами (i, j); нумерация индексов начинается с нуля; метод меняет значение атрибута
# __is_open объекта Cell в ячейке (i, j) на True;
# show_pole() - отображает игровое поле в консоли (как именно сделать - на ваше усмотрение, этот метод - домашнее задание).
# Расстановку мин выполняйте случайным образом по игровому полю (для этого удобно воспользоваться функцией randint модуля random).
# После расстановки всех total_mines мин, вычислите их количество вокруг остальных клеток (где нет мин). Область охвата - соседние
# (прилегающие) клетки (8 штук).
# В методе open_cell() необходимо проверять корректность индексов (i, j). Если индексы указаны некорректно, то генерируется исключение командой:
# raise IndexError('некорректные индексы i, j клетки игрового поля')
# Следующий класс Cell описывает состояние одной ячейки игрового поля. Объекты этого класса создаются командой:
# cell = Cell()
# При этом в самом объекте создаются следующие локальные приватные свойства:
# __is_mine - булево значение True/False; True - в клетке находится мина, False - мина отсутствует;
# __number - число мин вокруг клетки (целое число от 0 до 8);
# __is_open - флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.
# Для работы с этими приватными атрибутами объявите в классе Cell следующие объекты-свойства с именами:
# is_mine - для записи и чтения информации из атрибута __is_mine;
# number - для записи и чтения информации из атрибута __number;
# is_open - для записи и чтения информации из атрибута __is_open.
# В этих свойствах необходимо выполнять проверку на корректность переданных значений (либо булево значение True/False,
# либо целое число от 0 до 8). Если передаваемое значение некорректно, то генерировать исключение командой:
# raise ValueError("недопустимое значение атрибута")
# С объектами класса Cell должна работать функция:
# bool(cell)
# которая возвращает True, если клетка закрыта и False - если открыта.
# Пример использования классов (эти строчки в программе писать не нужно):
# pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
# pole.init_pole()
# if pole.pole[0][1]:
#     pole.open_cell(0, 1)
# if pole.pole[3][5]:
#     pole.open_cell(3, 5)
# pole.open_cell(30, 100)  # генерируется исключение IndexError
# pole.show_pole()
# P.S. В программе на экран выводить ничего не нужно, только объявить классы.
# from random import randint
# class Cell:
#     def __init__(self):
#         self.__is_open = False
#         self.__is_mine = False
#         self.__number = 0
#
#     @property
#     def is_open(self):
#         return self.__is_open
#
#     @is_open.setter
#     def is_open(self, value):
#         if type(value) != bool:
#             raise ValueError("недопустимое значение атрибута")
#         else:
#             self.__is_open = value
#
#     @property
#     def is_mine(self):
#         return self.__is_mine
#
#     @is_mine.setter
#     def is_mine(self, mine):
#         if type(mine) != bool:
#             raise ValueError("недопустимое значение атрибута")
#         else:
#             self.__is_mine = mine
#
#     @property
#     def number(self):
#         return self.__number
#
#     @number.setter
#     def number(self, num):
#         if type(num) != int or num < 0 or num > 8:
#             raise ValueError("недопустимое значение атрибута")
#         else:
#             self.__number = num
#
#     def __bool__(self):
#         return not self.__is_open
#
#
# class GamePole:
#     __instance = None
#
#     def __init__(self, N, M, total_mines):
#         self._N = N
#         self._M = M
#         self._total_mines = total_mines
#         self.__pole_cells = tuple(tuple(Cell() for _ in range(M)) for _ in range(N))
#         self.init_pole() #вызов инициализатора поля
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __del__(self):
#         GamePole.__instance = None
#
#     @property
#     def pole(self):
#         return self.__pole_cells
#
#     def init_pole(self):
#         '''расставляет мины и делает все клетки закрытыми'''
#
#         '''закрыл поля и сбросил мины'''
#         for row in self.__pole_cells:
#             for x in row:
#                 x.is_open = False
#                 x.is_mine = False
#
#         '''наполнение минами'''
#         m = 0
#         while m < self._total_mines:
#             i = randint(0, self._N - 1)
#             j = randint(0, self._M - 1)
#             if self.__pole_cells[i][j].is_mine:
#                 continue
#             self.__pole_cells[i][j].is_mine = True
#             m += 1
#
#         '''проверка на мины, без добавления дополнительных полей, супер'''
#         indx = (-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1),(1, -1), (1, 0), (1, 1)
#         for x in range(self._N):
#             for y in range(self._M):
#                 if not self.pole[x][y].is_mine:
#                     mines = sum((self.pole[x + i][y + j].is_mine for i, j in indx if 0 <= x + i < self._N and 0 <= y + j < self._M))
#                     self.pole[x][y].number = mines
#
#
#
#     def open_cell(self, i, j):
#         if not 0 <= i < self._N or not 0 <= j < self._M:
#             raise IndexError('некорректные индексы i, j клетки игрового поля')
#         self.pole[i][j].is_open = True
#
#     def show_pole(self):
#         for row in self.pole:
#             print(*map(lambda x: '#' if not x.is_open else x.number if not x.is_mine else '*', row))
#         print('=' * self._M)



# pole = GamePole(4,7, 12)
# # print(pole)
# pole.init_pole()
# print(pole.open_cell(2,3))

# test
# pole = GamePole(10, 12, 10)  # создается поле размерами 10x12 с общим числом мин 10
# pole.init_pole()

# pole.open_cell(1,3)
# pole.show_pole()
# if pole.pole[0][1]:
#     pole.open_cell(0, 1)
# if pole.pole[3][5]:
#     pole.open_cell(3, 5)
# pole.open_cell(0,1)
# pole.show_pole()
# # pole.open_cell(30, 100)  # генерируется исключение IndexError
# pole.show_pole()


# TESTS

# p1 = GamePole(10, 20, 10)
# p2 = GamePole(10, 20, 10)
# assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
# p = p1
#
# cell = Cell()
# assert type(Cell.is_mine) == property and type(Cell.number) == property and type(
#     Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

# cell.is_mine = True
# cell.number = 5
# cell.is_open = True
# assert bool(cell) == False, "функция bool() вернула неверное значение"
#
# try:
#     cell.is_mine = 10
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"
#
# try:
#     cell.number = 10
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"
#
# p.init_pole()
# m = 0
# for row in p.pole:
#     for x in row:
#         assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
#         if x.is_mine:
#             m += 1
#
# assert m == 10, "на поле расставлено неверное количество мин"
# p.open_cell(0, 1)
# p.open_cell(9, 19)

# p.show_pole()
# try:
#     p.open_cell(10, 20)
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"
#
#
# def count_mines(pole, i, j):
#     n = 0
#     for k in range(-1, 2):
#         for l in range(-1, 2):
#             ii, jj = k + i, l + j
#             if ii < 0 or ii > 9 or jj < 0 or jj > 19:
#                 continue
#             if pole[ii][jj].is_mine:
#                 n += 1
#
#     return n
#
#
# for i, row in enumerate(p.pole):
#     for j, x in enumerate(row):
#         if not p.pole[i][j].is_mine:
#             m = count_mines(p.pole, i, j)
#             assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"





# ===============================================================================================
# Подвиг 9 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:
# v = Vector(x1, x2, x3,..., xN)
# где x1, x2, x3,..., xN - координаты вектора (числа: целые или вещественные).
# С каждым объектом класса Vector должны выполняться операторы:
# v1 + v2 # суммирование соответствующих координат векторов
# v1 - v2 # вычитание соответствующих координат векторов
# v1 * v2 # умножение соответствующих координат векторов
# v1 += 10 # прибавление ко всем координатам вектора числа 10
# v1 -= 10 # вычитание из всех координат вектора числа 10
# v1 += v2
# v2 -= v1
# v1 == v2 # True, если соответствующие координаты векторов равны
# v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает
# При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с новыми (вычисленными)
# координатами. При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.
# Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -, * должно генерироваться исключение командой:
# raise ArithmeticError('размерности векторов не совпадают')
# P.S. В программе на экран выводить ничего не нужно, только объявить класс.


class Vector:
    def __init__(self, *args):
        self.coords = args

    def __add__(self, other):
        if isinstance(other, Vector):
            if len(self.coords) == len(other.coords):
                return Vector(*(self.coords[i] + other.coords[i] for i in range(len(self.coords))))
            else:
                raise ArithmeticError('размерности векторов не совпадают')
        else:
            return Vector(*(self.coords[i] + other for i in range(len(self.coords))))

    def __sub__(self, other):
        if isinstance(other, Vector):
            if len(self.coords) == len(other.coords):
                return Vector(*(self.coords[i] - other.coords[i] for i in range(len(self.coords))))
            else:
                raise ArithmeticError('размерности векторов не совпадают')
        else:
            return Vector(*(self.coords[i] - other for i in range(len(self.coords))))

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.coords) == len(other.coords):
                return Vector(*(self.coords[i] * other.coords[i] for i in range(len(self.coords))))
            else:
                raise ArithmeticError('размерности векторов не совпадают')
        else:
            return Vector(*(self.coords[i] * other for i in range(len(self.coords))))

    def __iadd__(self, other):
        if isinstance(other, Vector):
            if len(self.coords) == len(other.coords):
                self.coords = tuple(self.coords[i] + other.coords[i] for i in range(len(self.coords)))
                return self
            else:
                raise ArithmeticError('размерности векторов не совпадают')
        else:
            self.coords = tuple(self.coords[i] + other for i in range(len(self.coords)))
            return self

    def __isub__(self, other):
        if isinstance(other, Vector):
            if len(self.coords) == len(other.coords):
                self.coords = tuple(self.coords[i] - other.coords[i] for i in range(len(self.coords)))
                return self
            else:
                raise ArithmeticError('размерности векторов не совпадают')
        else:
            self.coords = tuple(self.coords[i] - other for i in range(len(self.coords)))
            return self

    def __eq__(self, other):
        return tuple(self.coords) == tuple(other.coords)

    # def __eq__(self, other):
    #     if isinstance(other, Vector):
    #         if len(self.coords) == len(other.coords):
    #             self.coords = all(tuple(self.coords[i] == other.coords[i] for i in range(len(self.coords))))
    #             return self
    #         else:
    #             raise ArithmeticError('размерности векторов не совпадают')

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).coords)  # [5, 7, 9]
print((v1 - v2).coords)  # [-3, -3, -3]
print((v1 * v2).coords)  # [4, 10, 18]

v1 += 10
print(v1.coords)  # [11, 12, 13]
v1 -= 10
print(v1.coords)  # [1, 2, 3]
v1 += v2
print(v1.coords)  # [5, 7, 9]
v2 -= v1
print(v2.coords)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True