# class Clock:
#     __DAY = 86400
#
#     def __init__(self, seconds: int):   #:int нотация для программиста, что в качестве аргумента надо передать число,несет информационный характер
#         if not isinstance(seconds, int):
#             raise TypeError('Seconds must be "int" type!')
#         self.seconds = seconds % self.__DAY  #в дне 86400 секунд, если цифра больше, то остаток от деления возвращает "хвост"
#
#     def get_time(self):
#         s = self.seconds % 60
#         m = (self.seconds // 60) % 60
#         h = (self.seconds // 3600) % 24
#         return f'{self.__get_formatted(h)} : {self.__get_formatted(m)} : {self.__get_formatted(s)}'
#
#     @classmethod
#     def __get_formatted(cls, x):
#         return str(x).rjust(2, '0')

# c1 = Clock(1000)
# print(c1.get_time())
# c1 = c1 + 100 # будет ошибка , так как нет метода add

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, seconds: int):   #:int нотация для программиста, что в качестве аргумента надо передать число,несет информационный характер
#         if not isinstance(seconds, int):
#             raise TypeError('Seconds must be "int" type!')
#         self.seconds = seconds % self.__DAY  #в дне 86400 секунд, если цифра больше, то остаток от деления возвращает "хвост"
#
#     def get_time(self):
#         s = self.seconds % 60
#         m = (self.seconds // 60) % 60
#         h = (self.seconds // 3600) % 24
#         return f'{self.__get_formatted(h)} : {self.__get_formatted(m)} : {self.__get_formatted(s)}'
#
#     @classmethod
#     def __get_formatted(cls, x):
#         return str(x).rjust(2, '0')
#
#     def __add__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise ValueError('Right operand must be "int" type or Clock')
#         sc = other
#         if isinstance(other, Clock):
#             sc = other.seconds
#         return Clock(self.seconds + sc)
#
# c1 = Clock(1000)
# c1 = c1 + 100 # будет ошибка , так как нет метода add
# print(c1.get_time())
# c2 = Clock(2000)
# c3 = Clock(3000)
# c4 = c1 + c2 + c3
# print(c4.get_time()) # 01 : 41 : 40
# c5 = 100 + c1   #TypeError: unsupported operand type(s) for +: 'int' and 'Clock'
# но если сложить 100 и с1 , то уже пойдет по другому алгоритму: не экземпляр класса Часы будет складываться с числом
# или другим экземпляром класса часы, а экземпляр класса числа с другими(поэтому ошибка, тк в числе подобного переопределения нет)
# для этого есть магический метод radd (если экземпляр класса справа от сложения)

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, seconds: int):   #:int нотация для программиста, что в качестве аргумента надо передать число,несет информационный характер
#         if not isinstance(seconds, int):
#             raise TypeError('Seconds must be "int" type!')
#         self.seconds = seconds % self.__DAY  #в дне 86400 секунд, если цифра больше, то остаток от деления возвращает "хвост"
#
#     def get_time(self):
#         s = self.seconds % 60
#         m = (self.seconds // 60) % 60
#         h = (self.seconds // 3600) % 24
#         return f'{self.__get_formatted(h)} : {self.__get_formatted(m)} : {self.__get_formatted(s)}'
#
#     @classmethod
#     def __get_formatted(cls, x):
#         return str(x).rjust(2, '0')
#
#     def __add__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError('Right operand must be "int" type or Clock')
#         sc = other
#         if isinstance(other, Clock):
#             sc = other.seconds
#         return Clock(self.seconds + sc)
#
#     def __radd__(self, other):  #для сложения чего-то с экземпляром класса
#         return self + other
#
#     def __iadd__(self, other):  #для определения с += 1 действия,но создается новый экземпляр класса, если не сделать нижеизложенное
#         print('__iadd__')
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError('Right operand must be "int" type or Clock')
#         sc = other
#         if isinstance(other, Clock):
#             sc = other.seconds
#         self.seconds += sc
#         return self
#
# c1 = Clock(1000)
# c2 = Clock(2000)
# c3 = Clock(3000)
# c4 = c1 + c2 + c3 # add
# print(c4.get_time()) # 01 : 41 : 40
# c5 = 100 + c1 # radd
# print(c5.get_time())
# c5 += 200
# print(c5.get_time())


# ==============================================================================================




# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/tkjqkiCSnqM
# Подвиг 4. Известно, что в Python мы можем соединять два списка между собой с помощью оператора +:
# lst = [1, 2, 3] + [4.5, -3.6, 0.78]
# Но нет реализации оператора -, который бы убирал из списка соответствующие значения вычитаемого списка, как это показано в примере:
# lst = [1, 2, 3, 4, 5, 6] - [5, 6, 7, 8, 1] # [2, 3, 4] (порядок следования оставшихся элементов списка должен сохраняться)
# Давайте это поправим и создадим такой функционал. Для этого нужно объявить класс с именем NewList, объекты которого создаются командами:
# lst = NewList() # пустой список
# lst = NewList([-1, 0, 7.56, True]) # список с начальными значениями
# Реализуйте для этого класса работу с оператором вычитания, чтобы над объектами класса NewList можно было выполнять следующие действия:
# lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
# lst2 = NewList([0, 1, 2, 3, True])
# res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
# lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
# res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
# res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
# a = NewList([2, 3])
# res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
# Также в классе NewList необходимо объявить метод:
# get_list() - для возвращения результирующего списка объекта класса NewList
# Например:
# lst = res_2.get_list() # [1, 2, 3]
# P.S. В программе требуется только объявить класс. На экран ничего выводить не нужно. 

# class NewList:
#     def __init__(self, lst=None): #если изменяемый тип данных, то лучше None
#         self.__lst = lst[:] if lst and type(lst) == list else []
#
#     def __sub__(self, other):
#         other_list = other if type(other) == list else other.get_list()
#         return NewList(self.__diff_list(self.__lst, other_list))
#
#     @staticmethod
#     def __diff_list(lst_1, lst_2):
#         if len(lst_2) == 0:
#             return lst_1
#         sub = lst_2[:]
#         return [i for i in lst_1 if not NewList.__iselem(i, sub)]
#
#
#     @staticmethod
#     def __iselem(x, sub):
#         res = any(map(lambda xx: type(x) == type(xx) and x == xx, sub))  # то есть если находится хоть одно совпадение по типу и значению
#         if res: #если бы не это действие, то могло произойти такое [1,2,2,3] - [2,3] = [1], а должно быть [1,2]
#             sub.remove(x)
#         return res
#
#     def __rsub__(self, other):
#         other_list = other if type(other) == list else other.get_list()
#         return NewList(self.__diff_list(other_list, self.__lst))
#
#     def __isub__(self, other):
#         st = self.__lst
#         ot = other
#         if isinstance(other, NewList):
#             ot = other.__lst
#             for i in ot:
#                 if i in st and type(i) == type(st[st.index(i)]):
#                     st.remove(i)
#         self.__lst = st
#         return self
#
#     def get_list(self):
#         return self.__lst
#
# # lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
# # lst2 = NewList([0, 1, 2, 3, True])
# # res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
# # print(res_1.get_list())
# # lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
# # print(lst1.get_list())
# # res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
# # print(res_2.get_list())
# # res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
# # print(res_3.get_list())
# #
# # # a = NewList([2, 3])
# # # res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
#
#
# # TESTS
# st = NewList()
# lst1 = NewList([0, 1, -3.4, "abc", True])
# lst2 = NewList([1, 0, True])
#
# assert lst1.get_list() == [0, 1, -3.4, "abc", True] and st.get_list() == [], "метод get_list вернул неверный список"
#
# res1 = lst1 - lst2  #
# # print(res1.get_list())
# res2 = lst1 - [0, True]
# # print(res2.get_list())
# res3 = [1, 2, 3, 4.5] - lst2
# # print(res3.get_list())
# lst1 -= lst2
# # print(lst1.get_list())
# #
# assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
# assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
# assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
# assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
# #
# lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
# lst_2 = NewList([10, True, False, True, 1, 7.87])
# res = lst_1 - lst_2
# assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"
#
# a = NewList([2, 3])
# res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
# assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"


# =============================================================================================


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/0Poea079PSs
# Подвиг 5. Объявите класс с именем ListMath, объекты которого можно создавать командами:
# lst1 = ListMath() # пустой список
# lst2 = ListMath([1, 2, -5, 7.68]) # список с начальными значениями
# В качестве значений элементов списка объекты класса ListMath должны отбирать только целые и вещественные числа, остальные игнорировать (если указываются в списке). Например:
# lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
# В каждом объекте класса ListMath должен быть публичный атрибут:
# lst_math - ссылка на текущий список объекта (для каждого объекта создается свой список).
# Также с объектами класса ListMath должны работать следующие операторы:
# lst = lst + 76 # сложение каждого числа списка с определенным числом
# lst = 6.5 + lst # сложение каждого числа списка с определенным числом
# lst += 76.7  # сложение каждого числа списка с определенным числом
# lst = lst - 76 # вычитание из каждого числа списка определенного числа
# lst = 7.0 - lst # вычитание из числа каждого числа списка
# lst -= 76.3
# lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
# lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
# lst *= 5.54
# lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
# lst = 3 / lst # деление числа на каждый элемент списка
# lst /= 13.0
# При использовании бинарных операторов +, -, *, / должны формироваться новые объекты класса ListMath с новыми списками, прежние списки не меняются.
# При использовании операторов +=, -=, *=, /= значения должны меняться внутри списка текущего объекта (новый объект не создается).
# P.S. В программе достаточно только объявить класс. На экран ничего выводить не нужно.
#

# class ListMath:
#     def __init__(self, lst=None):
#         self.lst_math = [i for i in lst if type(i) in (int, float)] if lst else []
#
#     def __add__(self, other):
#         return ListMath(list(map(lambda x: x + other, self.lst_math)))
#
#     def __radd__(self, other):
#         return ListMath(list(map(lambda x: x + other, self.lst_math)))
#
#     def __iadd__(self, other):
#         s = [i + other for i in self.lst_math]
#         self.lst_math = s
#         return self
#
#     def __sub__(self, other):
#         return ListMath(list(map(lambda x: x - other, self.lst_math)))
#
#     def __rsub__(self, other):
#         return ListMath(list(map(lambda x: other - x, self.lst_math)))
#
#     def __isub__(self, other):
#         s = [i - other for i in self.lst_math]
#         self.lst_math = s
#         return self
#
#     def __mul__(self, other):
#         return ListMath(list(map(lambda x: x * other, self.lst_math)))
#
#     def __rmul__(self, other):
#         return ListMath(list(map(lambda x: x * other, self.lst_math)))
#
#     def __imul__(self, other):
#         s = [i * other for i in self.lst_math]
#         self.lst_math = s
#         return self
#
#     def __truediv__(self, other):
#         return ListMath(list(map(lambda x: x / other, self.lst_math)))
#
#     def __rtruediv__(self, other):
#         return ListMath(list(map(lambda x: x / other, self.lst_math)))
#
#     def __itruediv__(self, other):
#         s = [i / other for i in self.lst_math]
#         self.lst_math = s
#         return self


# def p():
#     print(lst.lst_math)
# lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
# lst = lst + 76 # сложение каждого числа списка с определенным числом
# p()
# lst = 6.5 + lst # сложение каждого числа списка с определенным числом
# p()
# lst += 76.7  # сложение каждого числа списка с определенным числом
# p()
# lst = lst - 76 # вычитание из каждого числа списка определенного числа
# lst = 7.0 - lst # вычитание из числа каждого числа списка
# lst -= 76.3
# lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
# lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
# lst *= 5.54
# lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
# lst = 3 / lst # деление числа на каждый элемент списка
# lst /= 13.0


# TESTS
# lst1 = ListMath()
# lp = [1, False, 2, -5, "abc", 7]
# lst2 = ListMath(lp)
# lst3 = ListMath(lp)
#
# assert id(lst2.lst_math) != id(lst3.lst_math), "внутри объектов класса ListMath должна создаваться копия списка"
#
# assert lst1.lst_math == [] and lst2.lst_math == [1, 2, -5, 7], "неверные значения в списке объекта класса ListMath"
#
# res1 = lst2 + 76
# lst = ListMath([1, 2, 3])
# lst += 5
# assert lst.lst_math == [6, 7, 8] and res1.lst_math == [77, 78, 71, 83], "неверные значения, полученные при операциях сложения"
#
# lst = ListMath([0, 1, 2])
# res3 = lst - 76
# res4 = 7 - lst
# assert res3.lst_math == [-76, -75, -74] and res4.lst_math == [7, 6, 5], "неверные значения, полученные при операциях вычитания"

# lst -= 3
# assert lst.lst_math == [-3, -2, -1], "неверные значения, полученные при операции вычитания -="
#
# lst = ListMath([1, 2, 3])
# res5 = lst * 5
# res6 = 3 * lst
# lst *= 4
# assert res5.lst_math == [5, 10, 15] and res6.lst_math == [3, 6, 9], "неверные значения, полученные при операциях умножения"
# assert lst.lst_math == [4, 8, 12], "неверные значения, полученные при операциях умножения"
#
# lst = lst / 2
# lst /= 13.0


# ===================================================================================================

# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/PY-E4OSh1gM
# Теория по односвязным спискам (при необходимости): https://youtu.be/TrHAcHGIdgQ
# Подвиг 6. Ранее, в одном из подвигов мы с вами создавали односвязный список с объектами класса StackObj
# (когда один объект ссылается на следующий и так далее):
# Давайте снова создадим такую структуру данных. Для этого объявим два класса:
# Stack - для управления односвязным списком в целом;
# StackObj - для представления отдельных объектов в односвязным списком.
# Объекты класса StackObj должны создаваться командой:
# obj = StackObj(data)
# где data - строка с некоторыми данными.
# Каждый объект класса StackObj должен иметь локальные приватные атрибуты:
# __data - ссылка на строку с переданными данными;
# __next - ссылка на следующий объект односвязного списка (если следующего нет, то __next = None).
# Объекты класса Stack создаются командой:
# st = Stack()
# и каждый из них должен содержать локальный атрибут:
# top - ссылка на первый объект односвязного списка (если объектов нет, то top = None).
# Также в классе Stack следует объявить следующие методы:
# push_back(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
# pop_back(self) - удаление последнего объекта из односвязного списка.
# Дополнительно нужно реализовать следующий функционал (в этих операциях копии односвязного списка создавать не нужно):
# добавление нового объекта класса StackObj в конец односвязного списка st
# st = st + obj
# st += obj
# добавление нескольких объектов в конец односвязного списка
# st = st * ['data_1', 'data_2', ..., 'data_N']
# st *= ['data_1', 'data_2', ..., 'data_N']
# В последних двух строчках должны автоматически создаваться N объектов класса StackObj с данными, взятыми из списка (каждый элемент списка для очередного добавляемого объекта).
# P.S. В программе достаточно только объявить классы. На экран ничего выводить не нужно.


# class Stack:
#     def __init__(self, top=None):
#         self.top = top
#         self.tail = None
#
#     def __add__(self, other):
#         self.tail.next = other
#         self.tail = other
#         return self
#
#     def __iadd__(self, other):
#         self.tail.next = other
#         self.tail = other
#         return self
#
#     def __mul__(self, other): # for st = st *[data_1, data_2]
#         for data in other:
#             self.push_back(StackObj(data))
#         return self
#
#     def __imul__(self, other):  #for st *= [data_3,data_4]
#         for data in other:
#             self.push_back(StackObj(data))
#         return self
#
#
#     def push_back(self, obj):
#         '''- добавление объекта класса StackObj в конец односвязного списка;'''
#         if not self.top:
#             self.top = obj
#             self.tail = obj
#         else:
#             #temp = self.tail
#             self.tail.next = obj
#             self.tail = obj
#
#
#     def pop_back(self):
#         '''- удаление последнего объекта из односвязного списка.'''
#         if self.top == self.tail:
#             self.top = None
#             self.tail = None
#         else:
#             temp = self.top
#             while temp.next:
#                 if temp.next == self.tail:
#                     break
#                 temp = temp.next
#             self.tail = temp
#             self.tail.next = None
#
#     def get_stack_list(self, data=False):
#         s = []
#         if not self.top:
#             return s
#         temp = self.top
#         if data:
#             while temp.next:
#                 s.append(temp.get_data())
#                 temp = temp.next
#             s.append(self.tail.get_data())
#         else:
#             while temp.next:
#                 s.append(temp)
#                 temp = temp.next
#             s.append(self.tail)
#         return s
#
# class StackObj:
#     def __init__(self, data):
#         self.__data = data
#         self.__next = None
#
#     def get_data(self):
#         return self.__data
#
#     @property
#     def next(self):
#         return self.__next
#     @next.setter
#     def next(self, next):
#         self.__next = next



# s = Stack()
# s.push_back(StackObj(1))
# s.push_back(StackObj(2))
# s.push_back(StackObj(3))
# s.push_back(StackObj(4))
# s.pop_back()
# obj = StackObj(8)
# obj1 = StackObj(9)
# s = s + obj
# s += obj1
#
# print(s.get_stack_list())
# print(s.get_stack_list(True))

# TESTS

# assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"
#
# st = Stack()
# top = StackObj("1")
# st.push_back(top)
# assert st.top == top, "неверное значение атрибута top"
#
# st = st + StackObj("2")
# st = st + StackObj("3")
# obj = StackObj("4")
# st += obj
#
# st = st * ['data_1', 'data_2']
# st *= ['data_3', 'data_4']
# print(st.get_stack_list())
#
# d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
# h = top
# i = 0
# while h:
#     assert h._StackObj__data == d[
#         i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
#     h = h._StackObj__next
#     i += 1
#
# assert i == len(d), "неверное число объектов в стеке"





# ================================================================================================


# Подвиг 7. Вам поручается создать программу по учету книг (библиотеку). Для этого необходимо в программе объявить два класса:
# Lib - для представления библиотеки в целом;
# Book - для описания отдельной книги.
# Объекты класса Book должны создаваться командой:
# book = Book(title, author, year)
# где title - заголовок книги (строка); author - автор книги (строка); year - год издания (целое число).
# Объекты класса Lib создаются командой:
# lib = Lib()
# Каждый объект должен содержать локальный публичный атрибут:
# book_list - ссылка на список из книг (объектов класса Book). Изначально список пустой.
# Также объекты класса Lib должны работать со следующими операторами:
# lib = lib + book # добавление новой книги в библиотеку
# lib += book
# lib = lib - book # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
# lib -= book
# lib = lib - indx # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
# lib -= indx
# При реализации бинарных операторов + и - создавать копии библиотек (объекты класса Lib) не нужно.
# Также с объектами класса Lib должна работать функция:
# n = len(lib) # n - число книг
# которая возвращает число книг в библиотеке.
# P.S. В программе достаточно только объявить классы. На экран ничего выводить не нужно

# class Lib:
#     def __init__(self, book_list=None): # None и такая формулировка снизу, тк лучше не присваивать знач по умолч в виде изменяемых типов данных
#         self.book_list = book_list[:] if book_list else []
#
#     def __add__(self, other):
#         self.book_list.append(other)
#         return self
#
#     def __iadd__(self, other):
#         self.book_list.append(other)
#         return self
#
#     def __sub__(self, other):
#         if isinstance(other, Book):
#             self.book_list.remove(other)
#         elif type(other) == int:
#             self.book_list.pop(other)
#         return self
#
#     def __isub__(self, other):
#         if isinstance(other, Book):
#             self.book_list.remove(other)
#         elif type(other) == int:
#             self.book_list.pop(other)
#         return self
#
#     def __len__(self):
#         return len(self.book_list)
#
#
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year


# l = Lib()
# b1 = Book('asda','sadas','asd')
# b2 = Book('324','324','a2343sd')
# b3 = Book('fdf', 'sdfsd', 'sdfsdfdf')
# l = l + b1
# l += b2
# l += b3
# l = l - b3
# l -= 0
# print(len(l))




# ====================================================================================================



# Подвиг 8. Вам необходимо создать простую программу по учету семейного бюджета. Для этого в программе объявите два класса с именами:
# Budget - для управления семейным бюджетом;
# Item - пункт расходов бюджета.
# Объекты класса Item должны создаваться командой:
# it = Item(name, money)
# где name - название статьи расхода; money - сумма расходов (вещественное или целое число).
# Соответственно, в каждом объекте класса Item должны формироваться локальные атрибуты name и money с переданными значениями. Также с объектами класса Item должны выполняться следующие операторы:
# s = it1 + it2 # сумма для двух статей расходов
# и в общем случае:
# s = it1 + it2 + ... + itN # сумма N статей расходов
# При суммировании оператор + должен возвращать число - вычисленную сумму по атрибутам money соответствующих объектов класса Item.
# Объекты класса Budget создаются командой:
# my_budget = Budget()
# А сам класс Budget должен иметь следующие методы:
# add_item(self, it) - добавление статьи расхода в бюджет (it - объект класса Item);
# remove_item(self, indx) - удаление статьи расхода из бюджета по его порядковому номеру indx (индексу: отсчитывается с нуля);
# get_items(self) - возвращает список всех статей расходов (список из объектов класса Item).
# Пример использования классов (эти строчки в программе писать не нужно):
# my_budget = Budget()
# my_budget.add_item(Item("Курс по Python ООП", 2000))
# my_budget.add_item(Item("Курс по Django", 5000.01))
# my_budget.add_item(Item("Курс по NumPy", 0))
# my_budget.add_item(Item("Курс по C++", 1500.10))
# # вычисление общих расходов
# s = 0
# for x in my_budget.get_items():
#     s = s + x
# P.S. В программе требуется только объявить класс. На экран ничего выводить не нужно.

# class Budget:
#     def __init__(self):
#         self.lst = []
#
#     def add_item(self, it):
#         self.lst.append(it)
#
#     def remove_item(self, indx):
#         self.lst.pop(indx)
#
#     def get_items(self):
#         return self.lst
#
#
# class Item:
#     def __init__(self, name, money):
#         self.name = name
#         self.money = money
#
#     def __add__(self, other):
#         money = other
#         if isinstance(other, Item):
#             money = other.money
#         return self.money + money
#
#     def __radd__(self, other):
#         money = other
#         if isinstance(other, Item):
#             money = other.money
#         return self.money + money

# it1 = Item('sdfsdf', 2343)
# it2 = Item('ewrrew',54332)
# it3 = Item('234234',23423423)
# s = it1 + it2 + it3
# print(s)

# TESTS

# my_budget = Budget()
# my_budget.add_item(Item("Курс по Python ООП", 2000))
# my_budget.add_item(Item("Курс по Django", 5000.01))
# my_budget.add_item(Item("Курс по NumPy", 0))
# my_budget.add_item(Item("Курс по C++", 1500.10))
# вычисление общих расходов
# s = 0
# for x in my_budget.get_items():
#     s = s + x

# print(s)

# ==================================================================================================

# Подвиг 9. Объявите класс Box3D для представления прямоугольного параллелепипеда (бруска), объекты которого создаются командой:
# box = Box3D(width, height, depth)
# где width, height, depth - ширина, высота и глубина соответственно (числа: целые или вещественные)
# В каждом объекте класса Box3D должны создаваться публичные атрибуты:
# width, height, depth - ширина, высота и глубина соответственно.
# С объектами класса Box3D должны выполняться следующие операторы:
# box1 = Box3D(1, 2, 3)
# box2 = Box3D(2, 4, 6)
# box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
# box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
# box = 3 * box2    # Box3D: width=6, height=12, depth=18
# box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
# box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
# box = box2 % 3    # Box3D: width=2, height=1, depth=0
# При каждой арифметической операции следует создавать новый объект класса Box3D с соответствующими значениями локальных атрибутов.
# P.S. В программе достаточно только объявить класс Box3D. На экран ничего выводить не нужно.

# class Box3D:
#     def __init__(self, width, height, depth):
#         self.width = width
#         self.height = height
#         self.depth = depth
#
#     def __add__(self, other):
#         if isinstance(other, Box3D):
#             w = self.width + other.width
#             h = self.height + other.height
#             d = self.depth + other.depth
#             return Box3D(w, h, d)
#
#     def __mul__(self, other):
#         if type(other) in (int, float):
#             w = self.width * other
#             h = self.height * other
#             d = self.depth * other
#             return Box3D(w, h, d)
#
#     def __rmul__(self, other):
#         if type(other) in (int, float):
#             w = self.width * other
#             h = self.height * other
#             d = self.depth * other
#             return Box3D(w, h, d)
#
#     def __sub__(self, other):
#         if isinstance(other, Box3D):
#             w = self.width - other.width
#             h = self.height - other.height
#             d = self.depth - other.depth
#             return Box3D(w, h, d)
#
#     def __floordiv__(self, other):
#         if type(other) in (int, float):
#             w = self.width // other
#             h = self.height // other
#             d = self.depth // other
#             return Box3D(w, h, d)
#
#     def __mod__(self, other):
#         if type(other) in (int, float):
#             w = self.width % other
#             h = self.height % other
#             d = self.depth % other
#             return Box3D(w, h, d)
#
#     def ret(self):
#         return print(f'width={self.width}, height={self.height}, depth={self.depth}')


# box1 = Box3D(1, 2, 3)
# box2 = Box3D(2, 4, 6)
# box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности  складываются)
# box.ret()
# box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
# box.ret()
# box = 3 * box2    # Box3D: width=6, height=12, depth=18
# box.ret()
# box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
# box.ret()
# box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
# box.ret()
# box = box2 % 3    # Box3D: width=2, height=1, depth=0
# box.ret()


# =========================================================================================




# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/9wNoWmEHdfo

# Подвиг 10 (на повторение). В нейронных сетях использую операцию под названием Max Pooling.
# Суть ее состоит в сканировании прямоугольной таблицы чисел (матрицы) окном определенного размера (обычно, 2x2 элемента)
# и выбора наибольшего значения в пределах этого окна:
# https://ucarecdn.com/76d8ded0-e630-4fc6-be3d-eb43e2b8f0fb/
#  Или, если окна выходят за пределы матрицы, то они пропускаются (игнорируются):
# https://ucarecdn.com/6dcc098d-9c7e-4fe2-a86c-56420c81d5e1/
# Мы повторим эту процедуру. Для этого в программе нужно объявить класс с именем MaxPooling, объекты которого создаются командой:
# mp = MaxPooling(step=(2, 2), size=(2,2))
# где step - шаг смещения окна по горизонтали и вертикали; size - размер окна по горизонтали и вертикали.
# Параметры step и size по умолчанию должны принимать кортеж со значениями (2, 2).
# Для выполнения операции Max Pooling используется команда:
# res = mp(matrix)
# где matrix - прямоугольная таблица чисел; res - ссылка на результат обработки таблицы matrix (должна создаваться новая таблица чисел.
# Прямоугольную таблицу чисел следует описывать вложенными списками. Если при сканировании таблицы часть окна выходит за ее пределы,
# то эти данные отбрасывать (не учитывать все окно).
# Если matrix не является прямоугольной таблицей или содержит хотя бы одно не числовое значение, то должно генерироваться исключение командой:
# raise ValueError("Неверный формат для первого параметра matrix.")
# Пример использования класса (эти строчки в программе писать не нужно):
# mp = MaxPooling(step=(2, 2), size=(2,2))
# res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
# Результатом будет таблица чисел:
# 6 8
# 9 7
# P.S. В программе достаточно объявить только класс. Выводить на экран ничего не нужно.

# class MaxPooling:
#     def __init__(self, step=(2, 2), size=(2, 2)):
#         self.step = step
#         self.size = size
#
#     def __call__(self, matrix):
#         rows = len(matrix)
#         cols = len(matrix[0]) if rows > 0 else 0
#         for row in matrix:
#             if len(row) != len(matrix) or not all(map(lambda x: type(x) in (int,float), row)):
#                 raise ValueError("Неверный формат для первого параметра matrix.")
#         step_row, step_col = self.step
#         size_row, size_col = self.size
#         rows_range = (rows - step_row) // size_row + 1
#         cols_range = (cols - step_col) // size_col + 1
#         matrix_next = [[0] * cols_range for _ in range(rows_range)]
#
#         for i in range(rows_range):
#             for j in range(cols_range):
#                 s = (x for r in matrix[i * step_row: i * step_row + size_row] for x in r[j * step_col: j * step_col + size_row])
#                 matrix_next[i][j] = max(s)
#
#         return matrix_next


# mp = MaxPooling(step=(2, 2), size=(2,2))
#
# res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
# print(res)

#TESTS


# mp = MaxPooling(step=(2, 2), size=(2,2))
# m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
# m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
# res1 = mp(m1)
# res2 = mp(m2)

# assert res1 == [[10]], "неверный результат операции MaxPooling"
# assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"
#
# mp = MaxPooling(step=(3, 3), size=(2,2))
# m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
# res3 = mp(m3)
# assert res3 == [[12]], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"
#
# try:
#     res = mp([[1, 2], [3, 4, 5]])
# except ValueError:
#     assert True
# else:
#     assert False, "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"
#
# try:
#     res = mp([[1, 2], [3, '4']])
# except ValueError:
#     assert True
# else:
#     assert False, "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"
#



# ============================================================================================================


