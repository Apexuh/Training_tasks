# __iter__(self) - получение итератора для перебора обьекта
# __next__(self) - переход к следующему значению и его считывание
#
# range(start, stop, step) - арифметическая последовательность

# l = list(range(5)) #[0, 1, 2, 3, 4]
# a = iter(range(5))
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__()) #StopIteration


# class FRange:
#     def __init__(self, start=0.0, stop=0.0, step=1.0):
#         self.start = start
#         self.stop = stop
#         self.step = step
#         self.value = self.start - self.step # тогда начальное значение в итер будет self.start (вычли, при старте прибавилось)
#
#     def __next__(self):
#         if self.value + self.step < self.stop:
#             self.value += self.step
#             return self.value
#         else:
#             raise StopIteration
#
# fr = FRange(0, 2, 0.5)
# print(fr.__next__())
# print(fr.__next__())
# print(fr.__next__())
# print(fr.__next__())
# print(fr.__next__())
# or
# print(next(fr))
# print(next(fr))
# print(next(fr))
# print(next(fr))
# print(next(fr))

# for x in fr:
#     print(x) # TypeError: 'FRange' object is not iterable

# class FRange:
#     def __init__(self, start=0.0, stop=0.0, step=1.0):
#         self.start = start
#         self.stop = stop
#         self.step = step
#         self.value = self.start - self.step # тогда начальное значение в итер будет self.start (вычли, при старте прибавилось)
#
#     def __next__(self):
#         if self.value + self.step < self.stop:
#             self.value += self.step
#             return self.value
#         else:
#             raise StopIteration
#
#     def __iter__(self):
#         self.value = self.start - self.step
#         return self
#
# fr = FRange(0, 2, 0.5)
# # for x in fr:
# #     print(x)
#
# class FRange2D:
#     def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
#         self.rows = rows
#         self.fr = FRange(start,stop,step)
#
#     def __next__(self):
#         if self.value < self.rows:
#             self.value += 1
#             return iter(self.fr) #возвращает не значение , а итератор
#         else:
#             raise StopIteration
#
#
#     def __iter__(self):
#         self.value = 0
#         return self
#
# fr = FRange2D(0,2,0.5,4)
# for row in fr:
#     for x in row:
#         print(x, end=' ')   #4 итерации перебора
#     print()

# :
# 0.0 0.5 1.0 1.5
# 0.0 0.5 1.0 1.5
# 0.0 0.5 1.0 1.5
# 0.0 0.5 1.0 1.5

# =======================================================================================================


# Господа, ниже ссылки на несколько источников, инфа из которых помогла мне плотнее разобраться.
#
# Документацию, разумеется, никто не отменял, но это и сами найдёте при желании ;)
#
# Пошаговый разбор (статья свежая и очень вкусная): https://habr.com/ru/company/domclick/blog/674194/
#
# То же, но менее подробно: https://www.programiz.com/python-programming/methods/built-in/iter
#
# Разбор момента "два класса или один и почему": https://stackoverflow.com/questions/64577138/implement-iter-and-next-in-different
#
# Статья на общее развитие, помогает понять, что к чему вообще и куда))) https://habr.com/ru/post/488112/

# =======================================================================================================


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/-ZvYUtWMUFw
# Подвиг 5. Объявите в программе класс Person, объекты которого создаются командой:
# p = Person(fio, job, old, salary, year_job)
# где fio - ФИО сотрудника (строка); job - наименование должности (строка); old - возраст (целое число); salary -
# зарплата (число: целое или вещественное); year_job - непрерывный стаж на указанном месте работы (целое число).
# В каждом объекте класса Person автоматически должны создаваться локальные атрибуты с такими же именами: fio, job, old, salary, year_job
# и соответствующими значениями.
# Также с объектами класса Person должны поддерживаться следующие команды:
# data = p[indx] # получение данных по порядковому номеру (indx) атрибута (порядок: fio, job, old, salary, year_job и начинается с нуля)
# p[indx] = value # запись в поле с указанным индексом (indx) нового значения value
# for v in p: # перебор всех атрибутов объекта в порядке: fio, job, old, salary, year_job
#     print(v)
# При работе с индексами, проверить корректность значения indx. Оно должно быть целым числом в диапазоне [0; 4]. Иначе, генерировать исключение командой:
# raise IndexError('неверный индекс')
# Пример использования класса (эти строчки в программе не писать):
# pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
# pers[0] = 'Балакирев С.М.'
# for v in pers:
#     print(v)
# pers[5] = 123 # IndexError
# P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.

# class Person:
#     def __init__(self, fio, job, old, salary, year_job):
#         self.fio = fio
#         self.job = job
#         self.old = old
#         self.salary = salary
#         self.year_job = year_job
#         self.__data = [self.fio, self.job,self.old, self.salary, self.year_job]
#
#
#     def __check_index(self, index):
#         if index >= len(self.__data):
#             raise IndexError('неверный индекс')
#
#     def __getitem__(self, item):
#         self.__check_index(item)
#         return self.__data[item]
#
#     def __setitem__(self, key, value):
#         self.__check_index(key)
#         self.__data[key] = value
#
#     def __next__(self):
#         if self.value < len(self.__data) -1:
#             self.value += 1
#             return self.__data[self.value]
#         else:
#             raise StopIteration
#
#     def __iter__(self):
#         self.value = - 1
#         return self
#
#     def __str__(self):
#         s = ', '.join(list(map(str, self.__data)))
#         return s


# pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
# pers[0] = 'Балакирев С.М.'
# for v in pers:
#     print(v)
# pers[5] = 123 # IndexError
# print(pers)
#


# ================================================================================================


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/wfy7UyTSN_Y
# Подвиг 6. Вам дают задание разработать итератор для последовательного перебора элементов вложенных (двумерных) списков следующей структуры:
# lst = [[x00],
#        [x10, x11],
#        [x20, x21, x22],
#        [x30, x31, x32, x33],
#        ...
#       ]
# Для этого необходимо в программе объявить класс с именем TriangleListIterator, объекты которого создаются командой:
# it = TriangleListIterator(lst)
# где lst - ссылка на перебираемый список.
# Затем, с объектами класса TriangleListIterator должны быть доступны следующие операции:
# for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
#     print(x)
# it_iter = iter(it)
# x = next(it_iter)
# Итератор должен перебирать элементы списка по указанной треугольной форме.
# Даже если итератору на вход будет передан прямоугольная таблица (вложенный список),
# то ее перебор все равно должен осуществляться по треугольнику. Если же это невозможно (из-за структуры списка),
# то естественным образом должна возникать ошибка IndexError: index out of range (выход индекса за допустимый диапазон).
# P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.

# class TriangleListIterator:
#     def __init__(self, lst):
#         self.lst = lst
#         self.lst_out = self.__get_triangle(lst)
#
#     def __get_triangle(self, lst_in):
#         try:
#             lst = []
#             r = 1
#             for row in lst_in:
#                 lst.extend(row[0:r])
#                 r += 1
#             return lst
#         except IndexError:
#             raise IndexError
#
#
#     def __iter__(self):
#         self.row = -1
#         return self
#
#     def __next__(self):
#         self.row += 1
#         if self.row < len(self.lst_out):
#             return self.lst_out[self.row]
#         else:
#             raise StopIteration
#
#     def __getitem__(self, item):
#         return self.lst_out[item]

# lst = [['x00'], ['x10', 'x11'], ['x20', 'x21', 'x22'], ['x30', 'x31', 'x32', 'x33']]
# lst = [['x30', 'x31', 'x32', 'x33'], ['x30', 'x31', 'x32', 'x33'], ['x30', 'x31', 'x32', 'x33']]
# it = TriangleListIterator(lst)
# for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
#     print(x)
# it_iter = iter(it)
# x = next(it_iter)
# print(next(it_iter))

# ls = [['1'], [2, 3], [4, 5, 6], ['7', 8, '9', 10]]
# ls_one = [x for row in ls for x in row]
# # print(ls_one)
#
# t = TriangleListIterator(ls)
# for i, x in enumerate(t):
#     # print(ls_one[i])
#     # print(x)
#     assert x == ls_one[i], "итератор вернул неверное значение"
# # print(t.lst_out)


# ANOTHER WAY
# class TriangleListIterator:
#     def __init__(self, lst):
#         self.lst = lst
#
#     def __iter__(self):
#         for i in range(len(self.lst)):
#             for j in range(i + 1):
#                 yield self.lst[i][j]


# ANOTHER WAY
# class TriangleListIterator:
#     def __init__(self, lst):
#         self.__lst = lst
#
#     def __iter__(self):
#         self.__col = self.__row = -1
#         return self
#
#     def __next__(self):
#         if self.__row == self.__col:
#             self.__row += 1
#             self.__col = 0
#         else:
#             self.__col += 1
#
#         if self.__row == len(self.__lst):
#             raise StopIteration
#
#         return self.__lst[self.__row][self.__col]

# ======================================================================================


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/kxCAnaAqdOk
# Подвиг 7. Теперь, вам необходимо разработать итератор, который бы перебирал указанные столбцы двумерного списка.
# Список представляет собой двумерную таблицу из данных:
# lst = [[x11, x12, ..., x1N],
#        [x21, x22, ..., x2N],
#        ...
#        [xM1, xM2, ..., xMN]
#       ]
# Для этого в программе необходимо объявить класс с именем IterColumn, объекты которого создаются командой:
# it = IterColumn(lst, column)
# где lst - ссылка на двумерный список; column - индекс перебираемого столбца (отсчитывается от 0).
# Затем, с объектами класса IterColumn должны быть доступны следующие операции:
# it = IterColumn(lst, 1)
# for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
#     print(x)
# it_iter = iter(it)
# x = next(it_iter)
# P.S. В программе нужно объявить только класс итератора. Выводить на экран ничего не нужно.

# class IterColumn:
#     def __init__(self, lst, column):
#         self.lst = [i[column] for i in lst]
#         # self.column = column
#
#     def __iter__(self):
#         self.row = -1
#         return self
#
#     def __next__(self):
#         self.row += 1
#         if self.row < len(self.lst):
#             return self.lst[self.row]
#         else:
#             raise StopIteration
#
#
# lst = [['x00', 'x01', 'x02'],
#        ['x10', 'x11', 'x12'],
#        ['x20', 'x21', 'x22'],
#        ['x30', 'x31', 'x32']]


# it = IterColumn(lst, 1)
# for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
#     print(x)
# it_iter = iter(it)
# x = next(it_iter)
# print(x)
# x = next(it_iter)
#
# print(x)
# print(it.lst)


# ANOTHER WAY

# class IterColumn:
#     def __init__(self, lst, column):
#         self.data = [item[column] for item in lst]
#
#     def __iter__(self):
#         yield from self.data

# =========================================================================================================


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/WrZ1TMwuvis
# Теория по односвязным спискам (при необходимости): https://youtu.be/TrHAcHGIdgQ
# Подвиг 8. Вы несколько раз уже делали стек-подобную структуру, когда объекты последовательно связаны между собой:
# Доведем ее функционал до конца. Для этого, по прежнему, нужно объявить классы:
# Stack - для представления стека в целом;
# StackObj - для представления отдельных объектов стека.
# В классе Stack должны быть методы:
# push_back(obj) - для добавления нового объекта obj в конец стека;
# push_front(obj) - для добавления нового объекта obj в начало стека.
# В каждом объекте класса Stack должен быть публичный атрибут:
# top - ссылка на первый объект стека (при пустом стеке top = None).
# Объекты класса StackObj создаются командой:
# obj = StackObj(data)
# где data - данные, хранящиеся в объекте стека (строка).
# Также в каждом объекте класса StackObj должны быть публичные атрибуты:
# data - ссылка на данные объекта;
# next - ссылка на следующий объект стека (если его нет, то next = None).
# Наконец, с объектами класса Stack должны выполняться следующие команды:
# st = Stack()
# st[indx] = value # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
# data = st[indx]  # получение данных из объекта стека по индексу
# n = len(st) # получение общего числа объектов стека
# for obj in st: # перебор объектов стека (с начала и до конца)
#     print(obj.data)  # отображение данных в консоль
# При работе с индексами (indx), нужно проверять их корректность. Должно быть целое число от 0 до N-1, где N - число объектов в стеке.
# Иначе, генерировать исключение командой:
# raise IndexError('неверный индекс')
# P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

# class Stack:
#     def __init__(self):
#         self.top = None
#
#     def push_back(self, obj):
#         if not self.top:
#             self.top = obj
#         else:
#             temp = self.top
#             while temp.next:
#                 temp = temp.next
#             temp.next = obj
#
#     def push_front(self, obj):
#         obj.next = self.top
#         self.top = obj
#
#     def __getitem__(self, item):
#         self.__check_index(item)
#         return self.__find_obj(item).data
#
#     def __setitem__(self, key, value):
#         self.__check_index(key)
#         self.__find_obj(key).data = value
#
#
#     def __check_index(self, index):
#         if index < 0 or index >= self.__len__():
#             raise IndexError('неверный индекс')
#
#     def __find_obj(self, index):
#         self.__check_index(index)
#         temp = self.top
#         counter = 0
#         while counter != index:
#             temp = temp.next
#             counter += 1
#         return temp
#
#     def __len__(self):
#         counter = 0
#         if self.top:
#             temp = self.top
#             counter += 1
#             while temp.next:
#                 temp = temp.next
#                 counter += 1
#         return counter
#     def __next__(self):
#         temp = self.temp
#         if self.temp.next:
#             self.temp = self.temp.next
#             return temp
#         else:
#             raise StopIteration
#
#     def __iter__(self):
#         self.cnt = -1
#         self.temp = self.top
#         return self
# class StackObj:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# st = Stack()
# st.push_back(StackObj('one'))
# st.push_back(StackObj('two'))
# st.push_front(StackObj('three'))
# st.push_front(StackObj('four'))
#
# print(len(st))

# st[indx] = value # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
# data = st[indx]  # получение данных из объекта стека по индексу
# n = len(st) # получение общего числа объектов стека
# for obj in st: # перебор объектов стека (с начала и до конца)
#     print(obj.data)  # отображение данных в консоль


# tests
# st = Stack()
# st.push_back(StackObj("1"))
# st.push_front(StackObj("2"))
# print(st[0])
# assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"
#
# st[0] = "0"
# assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"
#
# for obj in st:
#     assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

# try:
#     a = st[3]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"


# ============================================================================================================


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/kmmvxZWxaAY
# Подвиг 9. В программе необходимо реализовать таблицу TableValues по следующей схеме:
# https://ucarecdn.com/fe9f4b6a-e4c5-4db2-ad0f-c859fbf81ca9/
# Каждая ячейка таблицы должна быть представлена классом Cell. Объекты этого класса создаются командой:
# cell = Cell(data)
# где data - данные в ячейке. В каждом объекте класса Cell должен формироваться локальный приватный атрибут __data
# с соответствующим значением. Для работы с ним в классе Cell должно быть объект-свойство (property):
# data - для записи и считывания информации из атрибута __data.
# Сам класс TableValues представляет таблицу в целом, объекты которого создаются командой:
# table = TableValues(rows, cols, type_data)
# где rows, cols - число строк и столбцов таблицы; type_data - тип данных ячейки (int - по умолчанию, float, list, str и т.п.).
# Начальные значения в ячейках таблицы равны 0 (целое число).
# С объектами класса TableValues должны выполняться следующие команды:
# table[row, col] = value# запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
# value = table[row, col] # считывание значения из ячейки с индексами row, col
# for row in table:  # перебор по строкам
#     for value in row: # перебор по столбцам
#         print(value, end=' ')  # вывод значений ячеек в консоль
#     print()
# При попытке записать по индексам table[row, col] данные другого типа (не совпадающего с атрибутом type_data объекта класса TableValues),
# должно генерироваться исключение командой:
# raise TypeError('неверный тип присваиваемых данных')
# При работе с индексами row, col, необходимо проверять их корректность. Если индексы не целое число или они выходят
# за диапазон размера таблицы, то генерировать исключение командой:
# raise IndexError('неверный индекс')
# P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

# class Cell:
#     def __init__(self, data):
#         self.__data = data
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, value):
#         self.__data = value
#
# class TableValues:
#     def __init__(self, rows, cols, type_data=int):
#         self.type_data = type_data
#         self.table = [[0] * cols for _ in range(rows)]
#
#     def __setitem__(self, key, value):
#         if type(value) != self.type_data:
#             raise TypeError('неверный тип присваиваемых данных')
#         self.table[key[0]][key[1]] = value
#
#     def __getitem__(self, item):
#         if type(item) == tuple:
#             x, y = item
#             if not self.table[x][y]:
#                 raise IndexError('неверный индекс')
#             return self.table[x][y]
#         return self.table[item]
#
#     def __str__(self):
#         return '\n'.join([' '.join(str(x)) for x in self.table])

# table = TableValues(2,3)
# print(table)

# TESTS
# tb = TableValues(3, 2)
# n = m = 0
# for row in tb:
#     n += 1
#     for value in row:
#         m += 1
#         assert type(
#             value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"
#
# assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"
#
# tb[0, 0] = 10
# assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"
#
# try:
#     tb[2, 0] = 5.2
# except TypeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение TypeError"
#
# try:
#     a = tb[2, 4]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"


# ANOTHER WAY

# class Cell:
#     def __init__(self, data=0):
#         self.data = data
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, value):
#         self.__data = value
#
# class TableValues:
#     def __init__(self, rows, cols, type_data=int):
#         self.__type_data = type_data
#         self.__rows = rows
#         self.__cols = cols
#         self.__cells = [[Cell() for _ in range(cols)] for _ in range(rows)]
#
#     def __check_data(self, value):
#         if type(value) != self.__type_data:
#             raise TypeError('неверный тип присваиваемых данных')
#
#     def __check_idx(self, idx):
#         r, c = idx
#         if r not in range(self.__rows) or c not in range(self.__cols):
#             raise IndexError('неверный индекс')
#
#     def __getitem__(self, item):
#         self.__check_idx(item)
#         r, c = item
#         return self.__cells[r][c].data
#
#     def __setitem__(self, key, value):
#         self.__check_idx(key)
#         self.__check_data(value)
#         r, c = key
#         self.__cells[r][c].data = value
#
#     def __iter__(self):
#         self.__n_row = -1
#         return self
#
#     @staticmethod
#     def row_iter(row):
#         for el in row:
#             yield el.data
#
#     def __next__(self):
#         if self.__n_row + 1 < len(self.__cells):
#             self.__n_row += 1
#             return self.row_iter(self.__cells[self.__n_row])
#         else:
#             raise StopIteration

# ================================================================================================


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/yX9qxE8X1OA
# Подвиг 10 (на повторение). Объявите класс Matrix (матрица) для операций с матрицами. Объекты этого класса должны создаваться командой:
# m1 = Matrix(rows, cols, fill_value)
# где rows, cols - число строк и столбцов матрицы; fill_value - заполняемое начальное значение элементов матрицы
# (должно быть число: целое или вещественное). Если в качестве аргументов передаются не числа, то генерировать исключение:
# raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
# Также объекты можно создавать командой:
# m2 = Matrix(list2D)
# где list2D - двумерный список (прямоугольный), состоящий из чисел (целых или вещественных). Если список list2D не прямоугольный,
# или хотя бы один из его элементов не число, то генерировать исключение командой:
# raise TypeError('список должен быть прямоугольным, состоящим из чисел')
# Для объектов класса Matrix должны выполняться следующие команды:
# matrix = Matrix(4, 5, 0)
# res = matrix[0, 0] # возвращается первый элемент матрицы
# matrix[indx1, indx2] = value # элементу матрицы с индексами (indx1, indx2) присваивается новое значение
# Если в результате присвоения тип данных не соответствует числу, то генерировать исключение командой:
# raise TypeError('значения матрицы должны быть числами')
# Если указываются недопустимые индексы матрицы (должны быть целыми числами от 0 и до размеров матрицы), то генерировать исключение:
# raise IndexError('недопустимые значения индексов')
# Также с объектами класса Matrix должны выполняться операторы:
# matrix = m1 + m2 # сложение соответствующих значений элементов матриц m1 и m2
# matrix = m1 + 10 # прибавление числа ко всем элементам матрицы m1
# matrix = m1 - m2 # вычитание соответствующих значений элементов матриц m1 и m2
# matrix = m1 - 10 # вычитание числа из всех элементов матрицы m1
# Во всех этих операция должна формироваться новая матрица с соответствующими значениями. Если размеры матриц не совпадают
# (разные хотя бы по одной оси), то генерировать исключение командой:
# raise ValueError('операции возможны только с матрицами равных размеров')
# Пример для понимания использования индексов (эти строчки в программе писать не нужно):
# mt = Matrix([[1, 2], [3, 4]])
# res = mt[0, 0] # 1
# res = mt[0, 1] # 2
# res = mt[1, 0] # 3
# res = mt[1, 1] # 4
# P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.


# class Matrix:
#     def __init__(self, *args):
#         if len(args) == 3:
#             rows, cols, fill_value = args
#             self.__check_value(rows, cols, fill_value)
#             self.matrix = [[fill_value] * cols for _ in range(rows)]
#         elif len(args) == 1:
#             self.__check_lst(*args)
#             self.__form_true(*args)
#             self.matrix = list(*args)
#
#     @staticmethod
#     def __check_value(rows, cols, fill_value):
#         if type(fill_value) not in (int, float) or not isinstance(rows,
#                                                                   (int, float) or not isinstance(cols, (int, float))):
#             raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
#
#     @staticmethod
#     def __check_lst(lst):
#         data = all(list(map(lambda row: all(list(map(lambda x: isinstance(x, (int, float)), row))), lst)))
#         if not data:
#             raise TypeError('список должен быть прямоугольным, состоящим из чисел')
#
#     @staticmethod
#     def __form_true(lst):
#         form_true = len(set(list(map(len, lst)))) == 1
#         if not form_true:
#             raise TypeError('список должен быть прямоугольным, состоящим из чисел')
#
#     @staticmethod
#     def __check_index(index):
#         x, y = index
#         if type(x) != int or type(y) != int or x < 0 or y < 0:
#             raise IndexError('недопустимые значения индексов')
#         return x, y
#
#     def __getitem__(self, item):
#         x, y = self.__check_index(item)
#         if self.matrix[x][y] is None:
#             raise IndexError('недопустимые значения индексов')
#         return self.matrix[x][y]
#
#     def __setitem__(self, key, value):
#         x, y = self.__check_index(key)
#         if not isinstance(value, (int, float)):
#             raise TypeError('значения матрицы должны быть числами')
#         if not self.matrix[x][y]:
#             raise IndexError('недопустимые значения индексов')
#         self.matrix[x][y] = value
#
#     def __add__(self, other):
#         m1 = self.matrix
#         m1_0 = len(m1[0])
#         if isinstance(other, Matrix):
#             m2 = other.matrix
#             m2_0 = len(m2[0])
#             if len(m1) != len(m2) or m1_0 != m2_0:
#                 raise ValueError('операции возможны только с матрицами равных размеров')
#             m3 = [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
#         else:
#             m3 = list(map(lambda row: list(map(lambda x: x + other, row)), m1))
#         return Matrix(m3)
#
#     def __sub__(self, other):
#         m1 = self.matrix
#         m1_0 = len(m1[0])
#         if isinstance(other, Matrix):
#             m2 = other.matrix
#             m2_0 = len(m2[0])
#             if len(m1) != len(m2) or m1_0 != m2_0:
#                 raise ValueError('операции возможны только с матрицами равных размеров')
#             m3 = [[m1[i][j] - m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
#         else:
#             m3 = list(map(lambda row: list(map(lambda x: x - other, row)), m1))
#         return Matrix(m3)


# TESTS

# list2D = [[1, 2], [3, 4], [5, 6, 7]]
# st = Matrix(list2D)
# try:
#     st = Matrix(list2D)
# except TypeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"

# list2D = [[1, []], [3, 4], [5, 6]]
# try:
#     st = Matrix(list2D)
# except TypeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"
#
# try:
#     st = Matrix('1', 2, 0)
# except TypeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"
#
# list2D = [[1, 2], [3, 4], [5, 6]]
# matrix = Matrix(list2D)
# assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"

# matrix = Matrix(4, 5, 10)
# assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"
#
# try:
#     v = matrix[3, -1]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"
#
# try:
#     v = matrix['0', 4]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"

# matrix[0, 0] = 7
# assert matrix[0, 0] == 7, "неверно отработал __setitem__"

# try:
#     matrix[0, 0] = 'a'
# except TypeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение TypeError в __setitem__"

# m1 = Matrix([[1, 2], [3, 4]])
# m2 = Matrix([[1, 1], [1, 1], [1, 1]])
#
# try:
#     matrix = m1 + m2
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError при сложении матриц разных размеров"

# m1 = Matrix([[1, 2], [3, 4]])
# m2 = Matrix([[1, 1], [1, 1]])
# matrix = m1 + m2
# assert isinstance(matrix, Matrix), "операция сложения матриц должна возвращать экземпляр класса Matrix"
# assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
# assert m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 \
#        and m2[0, 0] == 1, "исходные матрицы не должны меняться при операции сложения"
#
# m1 = Matrix(2, 2, 1)
# id_m1_old = id(m1)
# m2 = Matrix(2, 2, 1)
# m1 = m1 + m2
# id_m1_new = id(m1)
# assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"
#
# matrix = Matrix(2, 2, 0)
# m = matrix + 10
# assert matrix[0, 0] == matrix[1, 1] == 0, "исходные матрицa не должна меняться при операции сложения c числом"
# assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"
#
# m1 = Matrix(2, 2, 1)
# m2 = Matrix([[0, 1], [1, 0]])
# identity_matrix = m1 - m2  # должна получиться единичная матрица
# assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
#        and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
# assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"
#
# matrix = Matrix(2, 2, 1)
# m = matrix - 1
# assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
# assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"



# ANOTHER WAY
# class Matrix:
#     def __init__(self, *args):
#         if len(args) == 3:
#             if not all(isinstance(i, (int, float)) for i in args):
#                 raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
#             self.rows, self.cols, self.fill_value = args
#             self.matrix = [[self.fill_value for _ in range(self.cols)] for _ in range(self.rows)]
#         else:
#             self.check_rect_matrix(args[0])
#             self.matrix = args[0]
#             self.rows, self.cols = len(self.matrix), len(self.matrix[0])
#
#     def __getitem__(self, item):  # +
#         x, y = item
#         try:
#             return self.matrix[x][y]
#         except:
#             raise IndexError('недопустимые значения индексов')
#
#     def __setitem__(self, key, value):  # +
#         if not isinstance(value, (int, float)):
#             raise TypeError('значения матрицы должны быть числами')
#         x, y = key
#         try:
#             self.matrix[x][y] = value
#         except:
#             raise IndexError('недопустимые значения индексов')
#
#     def __add__(self, other):
#         if isinstance(other, Matrix):
#             self.check_dabl_mat(self.matrix, other.matrix)
#             mat = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
#             for i in range(self.cols):
#                 for j in range(self.rows):
#                     mat[i][j] = self.matrix[i][j] + other.matrix[i][j]
#             return Matrix(mat)
#         if isinstance(other, int):
#             mat = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
#             for i in range(self.cols):
#                 for j in range(self.rows):
#                     mat[i][j] = sum((self.matrix[i][j], other))
#             return Matrix(mat)
#
#     def __rsub__(self, other):
#         return self - other
#
#     def __sub__(self, other):
#         if isinstance(other, Matrix):
#             self.check_dabl_mat(self.matrix, other.matrix)
#             mat = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
#             for i in range(self.cols):
#                 for j in range(self.rows):
#                     mat[i][j] = self.matrix[i][j] - other.matrix[i][j]
#             return Matrix(mat)
#         if isinstance(other, int):
#             mat = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
#             for i in range(self.cols):
#                 for j in range(self.rows):
#                     mat[i][j] = sum((self.matrix[i][j], -other))
#             return Matrix(mat)
#
#     @staticmethod
#     def check_dabl_mat(m1, m2):  # проверка на равенство размеров матриц.
#         if set(map(len, m1)) != set(map(len, m2)):
#             raise ValueError('операции возможны только с матрицами равных размеров')
#     @staticmethod
#     def check_rect_matrix(lst):  # проверка одной матрицы на прямоугольность и int/float элементы.
#         lam = lambda x: isinstance(x, (int, float))
#         if len(set(map(len, lst))) != 1 or \
#                 not all(all(lam(x) for x in row) for row in lst):
#             raise TypeError('список должен быть прямоугольным, состоящим из чисел')




