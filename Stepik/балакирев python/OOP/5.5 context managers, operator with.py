# менеджер контекста with


# # когда открываем файловый поток с помощью функции open(), то в конце работы с ним, его желательно закрыть с помощью метода close().
# # Если реализовать эту логику через конструкцию try/except/finally, то получим примерно вот такой текст программы:
# #
# # fp = None
# # try:
# #     fp = open("myfile.txt")
# #     for t in fp:
# #         print(t)
# # except Exception as e:
# #     print(e)
# # finally:
# #     if fp is not None:
# #         fp.close()
#
# # Благодаря блоку finally мы гарантированно закрываем файл, даже если в блоке try возникло какое-либо исключение.
# # Но, если воспользоваться файловым менеджером контекста, то программа принимает вид:
# #
# # try:
# #     with open("myfile.txt") as fp:
# #         for t in fp:
# #             print(t)
# # except Exception as e:
# #     print(e)
#
# В целом менеджер контекста – это класс, в котором реализованы два магических метода:
#
# __enter__() и __exit__()
#
# Давайте создадим свой класс менеджера, который бы контролировал работу при изменении списка: если программа в теле менеджера приводит к исключению (ошибке), то список должен оставаться прежним (без изменений):
#
# v1 = [1, 2, 3]
# v2 = [1, 2]

# class DefenerVector:
#     def __init__(self, v):
#         self.__v = v
#
#     def __enter__(self):
#         self.__temp = self.__v[:]  # делаем копию вектора v
#         return self.__temp    #возврат ссылку на копию списка
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is None:
#             self.__v[:] = self.__temp
#         return False

# with DefenerVector(v1) as dv:     # то есть список выше (self.__temp из def __enter__) возвращается представляется как dv
#     for i in enumerate(dv):
#         dv[i] += v2[i]
#
# print(v1)
#
#
# А класс DefenderVector менеджера контекста будет выглядеть так:
#
# class DefenerVector:
#     def __init__(self, v):
#         self.__v = v
#
#     def __enter__(self):
#         self.__temp = self.__v[:]  # делаем копию вектора v
#         return self.__temp
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is None:  #если не проихошли ошибки, то
#             self.__v[:] = self.__temp #присваиваем вектору значение временной переменной
#         return False  #если возрвращает False, то исключения вызванные внутри менеджера контекста, если True , то исключения , которые происходят внутри менеджера контекста

# exc_type - None если никаких ошибок не происходило

# Мы здесь в приватном свойстве сохраняем ссылку на вектор, который следует «защитить».
# Далее, в методе enter создаем копию этого вектора и возвращаем его.
# То есть, переменная dv будет ссылаться на эту копию и обработка внутри менеджера будет происходить с элементами этой копии,
# а не исходным вектором. Затем, в методе exit мы проверяем: если исключений не произошло, то заменяем все элементы вектора
# __v на преобразованные __temp. В результате, при выходе из менеджера, мы получим измененный вектор v1.
# Если же было какое-либо исключение, то запись новых данных выполняться не будет и у нас останется прежний вектор v1.
#
#
# Метод exit у нас возвращает значение False, что означает обработку исключения (если оно произошло) вышестоящим блоком.
# Обычно именно так и делают, чтобы не скрывать возможные ошибки и в обработчике верхнего уровня реагировать должным образом на ошибочные ситуации.
# Кстати, оператор return можно вовсе опустить, тогда метод exit возвратит None, а оно интерпретируется как False. Так что, часто его не пишут.
#
# При необходимости, менеджеры контекстов можно вкладывать друг в друга. Например, при работе с файлами, можно выполнить такое вложение:
#
# try:
#     with open("myfile.txt") as fin:
#         with open("out.txt", "w") as fout:
#             for line in fin:
#                 fout.write(line)
# except Exception as e:
#     print(e)
#
# ==================================================================================================


# Подвиг 1. Выберите все верные утверждения, связанные с работой оператора with.
#
#
# перед началом выполнения операторов внутри менеджера контекста выполняется метод __exit__, а после завершения - метод __enter__
# менеджер контекста образует свою локальную область видимости (подобно функциям, тело которых находится внутри локальной области видимости)
# (YES) - перед началом выполнения операторов внутри менеджера контекста выполняется метод __enter__, а после завершения - метод __exit__
# после оператора with необходимо указывать объект класса, в котором обязательно должен быть реализован метод __enter__, а метод __exit__ можно не прописывать
# (YES) - после оператора with необходимо указывать объект класса, в котором обязательно должны быть реализованы методы __enter__ и __exit__


# ===================================================================================================================



# exc_type    -   тип возникшего исключения (None, если не произошло)
#
# exc_val     -   объект класса возникшего исключения (None, если не произошло)
#
# exc_tb      -   трассировка стека возникшего исключения (None, если не произошло)


# ========================================================================================================



# Подвиг 3. Объявите класс PrimaryKey, который должен работать совместно с менеджером контекста следующим образом:
# with PrimaryKey() as pk:
#     raise ValueError
# где pk - ссылка на объект класса PrimaryKey.Класс PrimaryKey должен в момент входа в менеджер контекста выводить на
# экран сообщение "вход", а при завершении работы менеджера контекста выводить тип возникшего исключения.
# Класс PrimaryKey следует реализовать так, чтобы менеджер контекста сам обрабатывал возникшее исключение.


# class PrimaryKey:
#     def __enter__(self):
#         print('вход')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(exc_type)
#         return True
#
#
# with PrimaryKey() as pk:
#     raise ValueError




# =======================================================================================================



# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/4SewG1p3f-s
# Подвиг 4. Вам поручено разработать класс DatabaseConnection для управления подключением к базе данных. Объекты этого класса создаются командой:
# conn = DatabaseConnection()
# В самом классе необходимо объявить метод:
# def connect(self, login, password): ...
# для подключения к БД. В данной реализации этот метод должен устанавливать локальный атрибут _fl_connection_open в значение True:
# _fl_connection_open = True
# и генерировать исключение с помощью собственного класса ConnectionError унаследованного от базового класса Exception.
# Также в классе DatabaseConnection должен быть метод:
# def close(self): ...
# для закрытия соединения. В этом методе нужно атрибут _fl_connection_open установить в значение False.
# Метод close() необходимо вызывать всякий раз после завершения работы с БД, вне зависимости от того, произошли какие-либо исключения или нет.
# Этот функционал (автоматическое закрытие соединения с БД) предполагается реализовывать посредством менеджера контекста
# с использованием класса DatabaseConnection следующим образом:
# with DatabaseConnection() as conn:
#     # операторы менеджера контекста
# Пропишите дополнительно в классе DatabaseConnection необходимые магические методы для такого его использования совместно с оператором with.
# P.S. В программе нужно объявить только класс. На экран ничего выводить не нужно.

# class ConnectionError(Exception):...



# class DatabaseConnection:
#     def __init__(self):
#         self._fl_connection_open = False
#
#     def connect(self, login=None, password=None):
#         # if not login or not password:
#
#         self._fl_connection_open = True
#         raise ConnectionError
#
#     def close(self):
#         self._fl_connection_open = False
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.close()
#         return False

# TESTS

# c = DatabaseConnection()
#
# try:
#     c.connect('aaa', 'bbb')
# except ConnectionError:
#     assert c._fl_connection_open
# else:
#     assert False, "не сгенерировалось исключение ConnectionError"

# try:
#     with DatabaseConnection() as conn:
#         conn.connect('aaa', 'bbb')
# except ConnectionError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ConnectionError"

# assert conn._fl_connection_open == False, "атрибут _fl_connection_open принимает значение True, а должно быть False"



# ==============================================================================================================



# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/YPppgpsCo3E
# Подвиг 5. Объявите класс Box (ящик), объекты которого создаются командой:
# box = Box(name, max_weight)
# где name - название ящика (строка); max_weight - максимальный суммарный вес вещей в ящике (любое положительное число). 
# В каждом объекте этого класса должны формироваться локальные атрибуты:
# _name - ссылка на параметр name;
# _max_weight - ссылка на параметр max_weight;
# _things - список из вещей, хранящиеся в ящике (изначально пустой список).
# В классе Box объявите метод:
# def add_thing(self, obj)
# для добавления новой вещи в ящик, где obj - кортеж из двух значений:
# (название_вещи, вес_вещи)
# Если в момент добавления новой вещи суммарный вес всех вещей в ящике становится больше величины _max_weight, то генерировать исключение командой:
# raise ValueError('превышен суммарный вес вещей')
# Затем, объявите еще один класс BoxDefender, который должен работать совместно с менеджером контекста следующим образом
# (эти строчки в программе не писать):
# box = Box("сундук", 1000)
# box.add_thing(("спички", 46.6))
# box.add_thing(("рубашка", 134))
# with BoxDefender(box) as b:
#     b.add_thing(("зонт", 346.6))
#     b.add_thing(("шина", 500))
#     ...
# Здесь b - это ссылка на объект класса Box. Если при добавлении вещей возникает исключение ValueError, то объект
# box должен оставаться без изменений (с теми вещами, что были до вызова менеджера контекста). Иначе, все добавленные вещи остаются в объекте box.
# P.S. В программе только объявить классы. Выводить что-либо на экран и использовать классы не нужно.


# class Box:
#     def __init__(self, name, max_weight):
#         self._name = name
#         self._max_weight = max_weight
#         self._things = []
#
#     @property
#     def things(self):
#         return self._things
#
#     @things.setter
#     def things(self, value):
#         self._things = value
#
#     @property
#     def total_weight(self):
#         return sum(x[1] for x in self._things)
#
#     def add_thing(self, obj):
#         name, weight = obj
#         if self.total_weight + weight > self._max_weight:
#             raise ValueError('превышен суммарный вес вещей')
#         self._things.append(obj)
#
#
#
# class BoxDefender:
#     def __init__(self, box):
#         self._box = box
#         self._things = box.things[:]
#
#     def __enter__(self):
#         return self._box
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type:
#             self._box.things = self._things
#         return False


# box = Box("сундук", 1000)
# box.add_thing(("спички", 46.6))
# box.add_thing(("рубашка", 134))
# # print(*list(box.__dict__.values()))
# with BoxDefender(box) as b:
#     b.add_thing(("зонт", 346.6))
#     b.add_thing(("шина", 500))
# print(box.__dict__)

# TESTS
# b = Box('name', 2000)
# assert b._name == 'name' and b._max_weight == 2000, "неверные значения атрибутов объекта класса Box"
#
# b.add_thing(("1", 100))
# b.add_thing(("2", 200))
#
# try:
#     with BoxDefender(b) as bb:
#         bb.add_thing(("3", 1000))
#         bb.add_thing(("4", 1900))
# except ValueError:
#     assert len(b._things) == 2
#
# else:
#     assert False, "не сгенерировалось исключение ValueError"

# try:
#     with BoxDefender(b) as bb:
#         bb.add_thing(("3", 100))
# except ValueError:
#     assert False, "возникло исключение ValueError, хотя, его не должно было быть"
# else:
#     assert len(b._things) == 3, "неверное число элементов в списке _things"





# ===============================================================================================


# Подвиг 6 (на повторение). Имеется следующий фрагмент программы:
# class PrinterError(Exception):
#     """Класс общих ошибок принтера"""
# class PrinterConnectionError(PrinterError):
#     """Ошибка соединения с принтером"""
# class PrinterPageError(PrinterError):
#     """Ошибка отсутствия бумаги в принтере"""
# try:
#     raise PrinterConnectionError('соединение с принтером отсутствует')
# except (PrinterConnectionError, PrinterPageError) as e:
#     print(e)
# except PrinterError as e:
#     print(e)
# Выберите все верные утверждения, связанные с этой программой.



# (NO) - последний блок except с классом PrinterError никогда выполнен не будет ни при каких типах исключений
# (YES) - при выполнении программы на экране будет отображена строка "соединение с принтером отсутствует"
# (NO) - блок except с двумя классами PrinterConnectionError и PrinterPageError записывать нельзя, возникнет ошибка
# (YES) - при возникновении исключений PrinterConnectionError или PrinterPageError выполнение программы перейдет в блок except с этими двумя классами


# ================================================================================================================



# Подвиг 7. Возможно ли в ООП обойтись без механизма обработки исключений и менеджеров контекста?
#
#
#
# (NO) - нет, написать большой проект без обработки исключений в принципе невозможно
# (YES) - вполне возможны ситуации, когда блоки try/except можно заменить операторами if/elif/else без потери качества программного кода
# (NO) - без менеджеров контекста невозможно обрабатывать ошибки при работе с файлами
# (YES) - да, но программа может получиться трудно понимаемой и трудно расширяемой



