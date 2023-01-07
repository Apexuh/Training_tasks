# print("Куда ты скачешь, гордый конь,")
# print("И где опустишь ты копыта?")
# print("О мощный властелин судьбы!")
# 1/0
# print("Не так ли ты над самой бездной")
# print("На высоте, уздой железной")
# print("Россию поднял на дыбы?")
#
# Но как эта операция деления формирует само исключение? Для этого в языке Python имеется конструкция (оператор)
# raise
# которая и порождает указанные типы исключений. В самом простом варианте, мы можем вместо деления на ноль записать
# этот оператор и указать тип исключения ZeroDivisionError:
# raise ZeroDivisionError("Деление на ноль")
# Результат выполнения программы будет тем же – она остановится на конструкции raise.
# Только сообщение об ошибке теперь будет на русском языке – та строка, что мы указали при формировании объекта класса ZeroDivisionError.
# То есть, после оператора raise мы можем прописывать нужный нам класс исключения с собственными параметрами.
# Также можно просто указывать класс, не прописывая каких-либо параметров:
# raise ZeroDivisionError
# Здесь у нас также создается экземпляр, но без параметров. Раз это так, значит, можно заранее создать экземпляр класса:
# e = ZeroDivisionError("Деление на ноль")
# а, затем, сгенерировать это исключение:
# raise e
#
#
# Если мы посмотрим на иерархию классов исключений языка Python, то здесь во главе стоит базовый класс BaseException
# Остальные классы наследуются от него и имеют строгую специализацию, кроме, разве что, класса Exception,
# который является общим для большого разнообразия типов исключений в момент выполнения программы.
#
# class PrintData:
#     def print(self, data):
#         self.send_data(data)
#         print(f"печать: {str(data)}")
#  
#     def send_data(self, data):
#         if not self.send_to_print(data):
#             raise Exception("принтер не отвечает")
#  
#     def send_to_print(self, data):
#         return False
#
# классы SystemExit, GeneratorExit и KeyboardInterrupt являются весьма специфичными и, обычно, они не используются при
# обработке собственных исключений. Поэтому, целесообразно выбирать именно класс Exception для формирования новых собственных классов исключений
#
# Итак, чтобы сформировать свой новый тип исключения, нужно прописать класс, который рекомендуется наследовать от класса Exception.
# В самом простом варианте достаточно просто описать иерархию:
# class ExceptionPrintSendData(Exception):
#     """Класс исключения при отправке данных принтеру"""
#
# И далее в программе использовать этот новый класс:
# def send_data(self, data):
#     if not self.send_to_print(data):
#         raise ExceptionPrintSendData("принтер не отвечает")
#
#
# Соответственно, ниже в программе, мы можем обработать этот тип ошибки, просто указав имя нашего нового класса:
# p = PrintData()
# try:
#     p.print("123")
# except ExceptionPrintSendData:
#     print("Ошибка печати")

# Кроме того, мы можем расширить функционал класса ExceptionPrintSendData. Давайте добавим в него конструктор. Он прописывается для произвольного числа аргументов:
#
# class ExceptionPrintSendData(Exception):
#     """Класс исключения при отправке данных принтеру"""
#     def __init__(self, *args):
#         self.message = args[0] if args else None
#
# А также магически метод__str__ для представления ошибки в консоли:
#
#     def __str__(self):
#         return f"Ошибка: {self.message}"
#
# Если теперь убрать блок try/except и вызвать метод print(), то увидим наш вариант отображения ошибки в консоли:
#
# p = PrintData()
# p.print("123")
#
# Наконец, пользовательские классы исключений дают возможность создавать свою иерархию исключений. В частности, в нашем примере, можно прописать общий класс исключений для принтера ExceptionPrint:
#
# class ExceptionPrint(Exception):
#     """Общий класс исключения принтера"""
#
# А, затем, остальные, более конкретные типы наследовать от него:
#
# class ExceptionPrintSendData(ExceptionPrint):
#     """Класс исключения при отправке данных принтеру"""
#
# В результате, в блоке except мы можем отлавливать как конкретные типы ошибок, так и общие, связанные с принтером:
#
# p = PrintData()
#  
# try:
#     p.print("123")
# except ExceptionPrintSendData as e:
#     print(e)
# except ExceptionPrint:
#     print("Ошибка печати")


# ======================================================================================================

# Подвиг 1. Выберите все верные утверждения, связанные с оператором raise.
#
# (NO) - оператор raise возвращает объект исключения (подобно оператору return)
# (YES) - после оператора raise следует указывать объект класса, унаследованного от BaseException
# (YES) - оператор raise позволяет генерировать различные исключения
# (YES) - после выполнения оператора raise программа останавливает свою работу, если исключение не обрабатывается
# (NO) - после оператора raise указывается строка с описанием возникшей ошибки


# ======================================================================================================


# Подвиг 2. Имеется следующий фрагмент программы:
#
# class LimitException(Exception):
#     """Превышение лимита"""
#
#
# error = LimitException('превышение лимита нагрузки')
# raise error
#
# Выберите все верные утверждения, относящиеся к этой программе.

# (NO) - при выполнении команды raise error на экран будет выведено сообщение "Превышение лимита"
# (YES) - команда raise error сгенерирует исключение типа LimitException
# (NO) - объект класса LimitException создан не будет, т.к. в классе LimitException отсутствует какой-либо инициализатор с параметром
# (YES) - при выполнении команды raise error на экран будет выведено сообщение "превышение лимита нагрузки"
# (NO) - команда raise error записана неверно, т.к. после оператора raise следует указывать имя класса исключения, а не его объект


# ==========================================================================================


# Подвиг 3. Имеется следующий фрагмент программы:
#
# class LimitException(Exception):
#     """Превышение лимита"""
#
#
# class ServerLimitException(LimitException):
#     """Превышение нагрузки на сервер"""
#
#
# try:
#     raise ServerLimitException('превышение серверной нагрузки')
# except LimitException:
#     print("LimitException")
# except ServerLimitException:
#     print("ServerLimitException")
#
# Выберите все верные утверждения, относящиеся к этой программе.


# (YES) - программа ни при каких типах исключений не перейдет во второй блок except
# (YES) - при выполнении этой программы на экране будет отображена строка "LimitException"
# при выполнении этой программы на экране будет отображена строка "ServerLimitException"
# (YES) - после выполнения оператора raise программа перейдет в первый блок except
# после выполнения оператора raise программа перейдет во второй блок except


# ========================================================================================================


# Подвиг 4. Объявите класс-исключение с именем StringException, унаследованным от базового класса Exception.
# После этого объявите еще два класса-исключения:
# NegativeLengthString - ошибка, если длина отрицательная;
# ExceedLengthString - ошибка, если длина превышает заданное значение;
# унаследованные от базового класса StringException.
# Затем, в блоке try (см. программу) пропишите команду генерации исключения для перехода в блок обработки исключения ExceedLengthString.


# class StringException(Exception): pass
#
# class NegativeLengthString(StringException):
#     '''len is negative'''
#
# class ExceedLengthString(StringException):
#     '''len is too musch...'''
#
# try:
#     raise ExceedLengthString
# except NegativeLengthString:
#     print("NegativeLengthString")
# except ExceedLengthString:
#     print("ExceedLengthString")
# except StringException:
#     print("StringException")


# ===========================================================================================================


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/6wnJd7OrNaI
# Подвиг 5. Объявите в программе класс-исключение с именем PrimaryKeyError, унаследованным от базового класса Exception.
# Объекты класса PrimaryKeyError должны создаваться командами:
# e1 = PrimaryKeyError()          # Первичный ключ должен быть целым неотрицательным числом
# e2 = PrimaryKeyError(id='abc')  # Значение первичного ключа id = abc недопустимо
# e3 = PrimaryKeyError(pk='123')  # Значение первичного ключа pk = 123 недопустимо
# В первом варианте команды должно формироваться сообщение об ошибке "Первичный ключ должен быть целым неотрицательным числом". При втором варианте:
# "Значение первичного ключа id = <id> недопустимо"
# И при третьем:
# "Значение первичного ключа pk = <pk> недопустимо"
# Эти сообщения должны формироваться при отображении объектов класса PrimaryKeyError, например:
# print(e2) # Значение первичного ключа id = abc недопустимо
# Затем, сгенерируйте это исключение с аргументом id = -10.5, обработайте его и отобразите на экране объект исключения.
# Sample Input:
#
# Sample Output:
# Значение первичного ключа id = -10.5 недопустимо

# class PrimaryKeyError(Exception):
#     def __init__(self, *args, **kwargs):
#         if len(args) == 0:
#             self.message = "Первичный ключ должен быть целым неотрицательным числом"
#         if kwargs:
#             self.message = f"Значение первичного ключа {''.join(list(kwargs.keys()))} = {kwargs[''.join(list(kwargs.keys()))]} недопустимо"
#     def __str__(self):
#         return self.message
#
# k = PrimaryKeyError(id = -10.5)
# print(k)


# e1 = PrimaryKeyError()          # Первичный ключ должен быть целым неотрицательным числом
# e2 = PrimaryKeyError(id='abc')  # Значение первичного ключа id = abc недопустимо
# e3 = PrimaryKeyError(pk='123')  # Значение первичного ключа pk = 123 недопустимо
# print(e2)


# TESTS
# assert issubclass(PrimaryKeyError, Exception), "класс PrimaryKeyError должен наследоваться от класса Exception"
#
# e1 = PrimaryKeyError(id=1)
# e2 = PrimaryKeyError(pk=2)
# e3 = PrimaryKeyError()
#
# assert str(e1) == "Значение первичного ключа id = 1 недопустимо", "неверное сообщение для исключения объекта класса PrimaryKeyError"
# assert str(e2) == "Значение первичного ключа pk = 2 недопустимо", "неверное сообщение для исключения объекта класса PrimaryKeyError"
# assert str(e3) == "Первичный ключ должен быть целым неотрицательным числом", "неверное сообщение для исключения объекта класса PrimaryKeyError"


# Подвиг 6. Объявите класс DateString для представления дат, объекты которого создаются командой:
# date = DateString(date_string)
# где date_string - строка с датой в формате:
# "DD.MM.YYYY"
# здесь DD - день (целое число от 1 до 31); MM - месяц (целое число от 1 до 12); YYYY - год (целое число от 1 до 3000).
# Например:
# date = DateString("26.05.2022")
# или
# date = DateString("26.5.2022") # незначащий ноль может отсутствовать
# Если указанная дата в строке записана неверно (не по формату), то генерировать исключение с помощью собственного класса:
# DateError- класс-исключения, унаследованный от класса Exception.
# В самом классе DateString переопределить магический метод __str__() для формирования строки даты в формате:
# "DD.MM.YYYY"
# (здесь должны фигурировать незначащие нули, например, для аргумента "26.5.2022" должна формироваться строка "26.05.2022").
# Далее, в программе выполняется считывание строки из входного потока командой:
# date_string = input()
# Ваша задача создать объект класса DateString с аргументом date_string и вывести объект на экран командой:
# print(date) # date - объект класса DateString
# Если же произошло исключение, то вывести сообщение (без кавычек):
# "Неверный формат даты"
# Sample Input:
# 1.2.1812
# Sample Output:
# 01.02.1812


# class DateError(Exception):
#     def __str__(self):
#         return "Неверный формат даты"
#
#
# error = DateError("Неверный формат даты")
# class DateString:
#     def __init__(self, date_string):
#         try:
#             day, month, year = date_string.split('.')
#             day, month, year = int(day), int(month), int(year)
#         except:
#             raise DateError("Неверный формат даты")
#         else:
#             if day < 1 or day > 31 or month < 1 or month > 12 or year < 0 or year > 3000:
#                 raise DateError("Неверный формат даты")
#             self._day = day
#             self._month = month
#             self._year = year
#
#
#     @staticmethod
#     def append_zero(value):
#         if 1 <= value <= 9:
#             return f'0{value}'
#         return value
#
#
#     def __str__(self):
#         return f'{self.append_zero(self._day)}.{self.append_zero(self._month)}.{self.append_zero(self._year)}'
#
# # date_string = input()
# date_string = '1.2.1812'
# date_string = 'sd'
# try:
#     date = DateString(date_string)
# except DateError as e:
#     print(e)
# else:
#     print(date)


# ======================================================================================

# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/wLaOyNN8x7E
# Значимый подвиг 7. Вам поручается разработать класс TupleData, элементами которого могут являются только объекты классов:
# CellInteger, CellFloat и CellString.
# Вначале в программе нужно объявить класс CellInteger, CellFloat и CellString, объекты которых создаются командами:
# cell_1 = CellInteger(min_value, max_value)
# cell_2 = CellFloat(min_value, max_value)
# cell_3 = CellString(min_length, max_length)
# где min_value, max_value - минимальное и максимальное допустимое значение в ячейке; min_length, max_length - минимальная
# и максимальная допустимая длина строки в ячейке.
# В каждом объекте этих классов должны формироваться локальные атрибуты с именами _min_value, _max_value или _min_length,
# _max_length и соответствующими значениями.
# Запись и считывание текущего значения в ячейке должно выполняться через объект-свойство (property) с именем:
# value - для записи и считывания значения в ячейке (изначально возвращает значение None).
# Если в момент записи новое значение не соответствует диапазону [min_value; max_value] или [min_length; max_length],
# то генерируется исключения командами:
# raise CellIntegerException('значение выходит за допустимый диапазон')  # для объектов класса CellInteger
# raise CellFloatException('значение выходит за допустимый диапазон')    # для объектов класса CellFloat
# raise CellStringException('длина строки выходит за допустимый диапазон')  # для объектов класса CellString
# Все три класса исключений должны быть унаследованы от одного общего класса:
# CellException
# Далее, объявите класс TupleData, объекты которого создаются командой:
# ld = TupleData(cell_1, ..., cell_N)
# где cell_1, ..., cell_N - объекты классов CellInteger, CellFloat и CellString (в любом порядке и любом количестве).
# Обращение к отдельной ячейке должно выполняться с помощью оператора:
# value = ld[index] # считывание значения из ячейке с индексом index
# ld[index] = value # запись нового значения в ячейку с индексом index
# Индекс index отсчитывается с нуля (для первой ячейки) и является целым числом. Если значение index выходит за диапазон [0; число ячеек-1], то генерировать исключение IndexError.
# Также с объектами класса TupleData должны выполняться следующие функции и операторы:
# res = len(ld) # возвращает общее число элементов (ячеек) в объекте ld
# for d in ld:  # перебирает значения ячеек объекта ld (значения, а не объекты ячеек)
#     print(d)
# Все эти классы в программе можно использовать следующим образом:
# ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

# try:
#     ld[0] = 1
#     ld[1] = 20
#     ld[2] = -5.6
#     ld[3] = "Python ООП"
# except CellIntegerException as e:
#     print(e)
# except CellFloatException as e:
#     print(e)
# except CellStringException as e:
#     print(e)
# except CellException:
#     print("Ошибка при обращении к ячейке")
# except Exception:
#     print("Общая ошибка при работе с объектом TupleData")
#
# P.S. Данная программа должна быть выполнена штатно, без ошибок. На экран отображать ничего не нужно.

# class CellException(Exception): ...
#
#
# class CellIntegerException(CellException): ...
#
#
# class CellFloatException(CellException): ...
#
#
# class CellStringException(CellException): ...
#
#
# class Cell:
#     def __init__(self, min_value, max_value):
#         self._min_value = min_value
#         self._max_value = max_value
#         self._value = None
#
#     def _check_value(self, value):
#         return value
#
#     @property
#     def value(self):
#         return self._value
#
#     @value.setter
#     def value(self, value):
#         self._value = self._check_value(value)
#
#
# class CellInteger(Cell):
#     def _check_value(self, value):
#         if value < self._min_value or value > self._max_value:
#             raise CellIntegerException('значение выходит за допустимый диапазон')
#         return value
#
#
# class CellFloat(Cell):
#     def _check_value(self, value):
#         if value < self._min_value or value > self._max_value:
#             raise CellFloatException('значение выходит за допустимый диапазон')
#         return value
#
#
# class CellString(Cell):
#     def _check_value(self, value):
#         if len(value) < self._min_value or len(value) > self._max_value:
#             raise CellStringException('длина строки выходит за допустимый диапазон')
#         return value
#
#
# class TupleData(tuple):
#     def __new__(cls, *lst):
#         instance = super().__new__(cls, lst)
#         return instance
#
#     def __init__(self, *lst):
#         self.lst = lst
#
#     def __getitem__(self, item):
#         return self.lst[item].value
#
#     def __setitem__(self, key, value):
#         self.lst[key].value = value
#
#     def __next__(self):
#         self.cnt += 1
#         if self.cnt < len(self.lst):
#             return self.lst[self.cnt].value
#         else:
#             raise StopIteration
#
#     def __iter__(self):
#         self.cnt = -1
#         return self


# k = CellInteger(0, 10)
# print(k)
# ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))
# ld[0] = 1
# print(ld[0])
# try:
#     ld[0] = 1
#     ld[1] = 20
#     ld[2] = -5.6
#     ld[3] = "Python ООП"
# except CellIntegerException as e:
#     print(e)
# except CellFloatException as e:
#     print(e)
# except CellStringException as e:
#     print(e)
# except CellException:
#     print("Ошибка при обращении к ячейке")
# except Exception:
#     print("Общая ошибка при работе с объектом TupleData")

# TESTS
# t = TupleData(CellInteger(-10, 10), CellInteger(0, 2), CellString(5, 10))
#
# d = (1, 0, 'sergey')
# t[0] = d[0]
# t[1] = d[1]
# t[2] = d[2]
#
# for i, x in enumerate(t):
    # assert x == d[i], "объект класса TupleData хранит неверную информацию"
#
# assert len(t) == 3, "неверное число элементов в объекте класса TupleData"
#
# cell = CellFloat(-5, 5)
# try:
#     cell.value = -6.0
# except CellFloatException:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение CellFloatException"
#
# cell = CellInteger(-1, 7)
# try:
#     cell.value = 8
# except CellIntegerException:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение CellIntegerException"
#
# cell = CellString(5, 7)
# try:
#     cell.value = "hello world"
# except CellStringException:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение CellStringException"
#
# assert issubclass(CellIntegerException, CellException) and issubclass(CellFloatException, CellException) and issubclass(
#     CellStringException,
#     CellException), "классы CellIntegerException, CellFloatException, CellStringException должны наследоваться от класса CellException"
#