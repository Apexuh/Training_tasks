# Распространение исключений (propagation exceptions)

# def func1():
#     return 1 / 0
# print('Я к вам пишу — чего же боле?')
# print('Что я могу еще сказать?')
# print('Теперь, я знаю, в вашей воле')
# func1() # error while calling function in line 8(but wrong code in line 4). we can see all stack of exceptions when we call the function
# print('Меня презреньем наказать.')
# print('Но вы, к моей несчастной доле')
# print('Хоть каплю жалости храня,')
# print('Вы не оставите меня.')


# def func1():
#     return 1 / 0
#
# def func2():
#     return func1()
# print('Я к вам пишу — чего же боле?')
# print('Что я могу еще сказать?')
# print('Теперь, я знаю, в вашей воле')
# func2() # error while calling function in line 23, 19, 16
# print('Меня презреньем наказать.')
# print('Но вы, к моей несчастной доле')
# print('Хоть каплю жалости храня,')
# print('Вы не оставите меня.')


# Выше исключения происходят на разных уровнях из-за деления на ноль. Обрабатывать исклюения можно на любом уровне.
# def func1():
#     return 1 / 0
#
# def func2():
#     return func1()
# print('Я к вам пишу — чего же боле?')
# print('Что я могу еще сказать?')
# print('Теперь, я знаю, в вашей воле')
# try:
#     func2()
# except ZeroDivisionError:
#     pass
# print('Меня презреньем наказать.')
# print('Но вы, к моей несчастной доле')
# print('Хоть каплю жалости храня,')
# print('Вы не оставите меня.')

# OR

# def func1():
#     return 1 / 0
#
# def func2():
#     try:
#         return func1()
#     except:
#         print('func2 error')
# print('Я к вам пишу — чего же боле?')
# print('Что я могу еще сказать?')
# print('Теперь, я знаю, в вашей воле')
# try:
#     func2()
# except ZeroDivisionError:
#     pass
# print('Меня презреньем наказать.')
# print('Но вы, к моей несчастной доле')
# print('Хоть каплю жалости храня,')
# print('Вы не оставите меня.')

# OR

# def func1():
#     try:
#         return 1 / 0
#     except:
#         print('func1 error')
#
# def func2():
#     try:
#         return func1()
#     except:
#         print('func2 error')
# print('Я к вам пишу — чего же боле?')
# print('Что я могу еще сказать?')
# print('Теперь, я знаю, в вашей воле')
# func2() #func1 error
# print('Меня презреньем наказать.')
# print('Но вы, к моей несчастной доле')
# print('Хоть каплю жалости храня,')
# print('Вы не оставите меня.')



# ====================================================================================

# Подвиг 1. В программе объявлены два класса следующим образом:
# class Geom:
#     def __init__(self, width, color):
#         if type(width) not in (int, float) or type(color) != str or width < 0:
#             raise ValueError('неверные параметры фигуры')
#
#         self._width = width
#         self._color = color
# class Ellipse(Geom):
#     def __init__(self, x1, y1, x2, y2, width=1, color='red'):
#         super().__init__(width, color)
#
#         if not self._is_valid(x1) or not self._is_valid(y1) or not self._is_valid(x2) or not self._is_valid(y2):
#             raise ValueError('неверные координаты фигуры')
#
#         self._x1 = x1
#         self._y1 = y1
#         self._x2 = x2
#         self._y2 = y2
#
#     def _is_valid(self, x):
#         return type(x) in (int, float)
# И создается объект класса Ellipse:
# try:
#     x1, y1, x2, y2, w = map(float, input().split())
#     el = Ellipse(x1, y1, x2, y2, w)
# except ValueError as e:
#     print(e)
# Выберите все верные утверждения, связанные с этой программой.


# при возникновении исключения в классе Geom, его можно обрабатывать только в классе Ellipse, иначе программа завершится с ошибкой
# (YES) - при вводе положительных числовых значений объект класса Ellipse будет создан успешно
# исключения, генерируемые в классе Ellipse можно обрабатывать в базовом классе Geom
# (YES) - все исключения, формируемые в классе Geom, можно обрабатывать внутри класса Ellipse
# (YES) - если бы переменная w ссылалась на строку, то в классе Geom было бы сгенерировано исключение, которое поднялось бы до класса Ellipse и обработано в основной программе в блоке try


# ==================================================================================================================



# Подвиг 2. Вы видите в консольном окне следующие строчки сообщения об ошибке:
#
# Traceback (most recent call last):
#   File "D:\Python\Projects\oop\ex1.py", line 26, in <module>
#     el = Ellipse(1, 2, 3, 4, '1')
#   File "D:\Python\Projects\oop\ex1.py", line 12, in __init__
#     super().__init__(width, color)
#   File "D:\Python\Projects\oop\ex1.py", line 4, in __init__
#     raise ValueError('неверные параметры фигуры')
# ValueError: неверные параметры фигуры
#
# Выберите все верные утверждения, которые можно сделать из этого вывода.

# (YES) - исключение ValueError стало следствием вызова метода __init__() в 12-й строчке программы
# (YES) - исключение ValueError сгенерировано в 4-й строчке программы в методе __init__()
# (YES) - исключение ValueError не было обработано в основном модуле программы в 26-й строчке
# (YES) - исключение ValueError сгенерировано в 4-й строчке программы и связано с работой команд, записанных в 12-й и 26-й строчках
# исключение ValueError сгенерировано в 26-й строчке программы и связано с работой команд, записанных в 12-й и 4-й строчках



# ================================================================================================================




# Подвиг 3. Объявите функцию с сигнатурой:
# def input_int_numbers(): ...
# которая бы считывала строку из введенных целых чисел, записанных через пробел, и возвращала кортеж из введенных чисел (в виде целых чисел, а не строк).
# Если хотя бы одно значение не является целым числом, то генерировать исключение, командой:
# raise TypeError('все числа должны быть целыми')
# Вызовите эту функцию в цикле до тех пор, пока пользователь не введет в строке все целочисленные значения
# (то есть, цикл завершается, когда функция отработает штатно, без генерации исключения).
# Выведите на экран прочитанные значения, записанные в виде строки через пробел.
# Sample Input:
# 1 abc 3 5
# 2.4 -5 4 3 2
# 0 -5 8 11
# 1 2 3 4
# Sample Output:
# 0 -5 8 11

# def input_int_numbers(string):
#     t = None
#     try:
#         t = tuple(map(int, string.split()))
#     except TypeError:
#         raise TypeError('все числа должны быть целыми')
#     finally:
#         if not t:
#             return input_int_numbers(input())
#         return ' '.join(t)
#
#
# print(input_int_numbers(input()))


# ANOTHER WAY

# def input_int_numbers():
#     try:
#         print(*map(int, input().split()))
#     except ValueError:
#         raise TypeError('все числа должны быть целыми')
        # return input_int_numbers()
# input_int_numbers()

# ===========================================================================================




# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/IexoPrHUSaA
# Подвиг 4. Объявите класс с именем ValidatorString, объекты которого создаются командой:
# vs = ValidatorString(min_length, max_length, chars)
# где min_length, max_length - минимально и максимально допустимая длина строки (целые числа, формируемые диапазон [min_length; max_length]);
# chars - строка из набора символов (хотя бы один из них должен присутствовать в проверяемой строке).
# Если chars - пустая строка, то проверку на вхождение символов не делать.
# В самом классе ValidatorString объявите метод:
# def is_valid(self, string): ...
# который проверяет строку string на соответствие критериям: string должна быть строкой, с длиной в диапазоне [min_length; max_length]
# и в string присутствует хотя бы один символ из chars. Если хотя бы один из этих критериев не выполняется, то генерируется исключение командой:
# raise ValueError('недопустимая строка')
# Затем, объявите класс с именем LoginForm, объекты которого создаются командой:
# lg = LoginForm(login_validator, password_validator)
# где login_validator - валидатор для логина (объект класса ValidatorString); password_validator - валидатор для пароля (объект класса ValidatorString).
# В самом классе LoginForm объявите следующий метод:
# def form(self, request): ...
# где request - объект запроса (словарь). В словаре request должен быть ключ 'login' со значением введенного логина (строки)
# и ключ 'password' со значением введенного пароля (строка). Если хотя бы одного ключа нет, то генерировать исключение командой:
# raise TypeError('в запросе отсутствует логин или пароль')
# В противном случае (если проверка для request прошла), проверять корректность полученного формой логина и пароля с помощью валидаторов,
# указанных в параметрах login_validator и password_validator, при создании объекта формы.
# Если логин/пароль введены верно, то в объекте класса LoginForm локальным атрибутам _login и _password присвоить соответствующие значения.
''''''
# Пример использования классов (эти строчки должны быть в программе):
# login_v = ValidatorString(4, 50, "")
# password_v = ValidatorString(10, 50, "!$#@%&?")
# lg = LoginForm(login_v, password_v)
# login, password = input().split()
# try:
#     lg.form({'login': login, 'password': password})
# except (TypeError, ValueError) as e:
#     print(e)
# else:
#     print(lg._login)
# Sample Input:
# sergey balakirev!
# Sample Output:
# # sergey


# class ValidatorString:
#     def __init__(self, min_length, max_length, chars):
#         self._min_length = min_length
#         self._max_length = max_length
#         self._chars = chars
#
#
#     def _check_chars(self, string):
#         s = any(list(map(lambda x: x in string, self._chars)))
#         return s
#
#     def is_valid(self, string):
#         if type(string) != str or len(string) < self._min_length or len(string) > self._max_length:
#             raise ValueError('недопустимая строка')
#         if len(self._chars) > 0 and not self._check_chars(string):
#             raise ValueError('недопустимая строка')
#         return string
#
#
# class LoginForm:
#     def __init__(self, login_validator, password_validator):
#         self._login_validator = login_validator
#         self._password_validator = password_validator
#
#     def form(self, request):
#         if not 'login' in request or not 'password' in request:
#             raise TypeError('в запросе отсутствует логин или пароль')
#         self._login = self._login_validator.is_valid(request['login'])
#         self._password = self._password_validator.is_valid(request['password'])
#
#
#
#
# login_v = ValidatorString(4, 50, "")
# password_v = ValidatorString(10, 50, "!$#@%&?")
# lg = LoginForm(login_v, password_v)
# # login, password = input().split()
# login, password = 'sergey balakirev!'.split()
# try:
#     lg.form({'login': login, 'password': password})
# except (TypeError, ValueError) as e:
#     print(e)
# else:
#     print(lg._login)

# ===============================================================================




# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/AVh6hs06oCU
# Подвиг 5. Вы начинаете разрабатывать свой сервис по тестированию. Для этого вам поручается разработать базовый класс Test для всех видов тестов,
# объекты которого создаются командой:
# test = Test(descr)
# где descr - формулировка теста (строка). Если длина строки descr меньше 10 или больше 10 000 символов, то генерировать исключение командой:
# raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
# В самом классе Test должен быть объявлен абстрактный метод:
# def run(self): ...
# который должен быть переопределен в дочернем классе. Если это не так, то должно генерироваться исключение командой:
# raise NotImplementedError
# Далее, объявите дочерний класс с именем TestAnsDigit для тестирования правильного введенного числового ответа на вопрос теста.
# Объекты класса TestAnsDigit должны создаваться командой:
# test_d = TestAnsDigit(descr, ans_digit, max_error_digit)
# где ans_digit - верный числовой ответ на тест; max_error_digit - максимальная погрешность в указании числового ответа
# (необходимо для проверки корректности вещественных чисел, по умолчанию принимает значение 0.01).
# Если аргумент ans_digit или max_error_digit не число (также проверить, что max_error_digit больше или равно нулю), то генерировать исключение командой:
# raise ValueError('недопустимые значения аргументов теста')
# В классе TestAnsDigit переопределите метод:
# def run(self): ...
# который должен читать строку из входного потока (ответ пользователя) командой:
# ans = float(input()) # именно такой командой, ее прописывайте в методе run()
# и возвращать булево значение True, если введенный числовой ответ ans принадлежит диапазону [ans_digit-max_error_digit;
# ans_digit+max_error_digit]. Иначе возвращается булево значение False.
# Теперь нужно воспользоваться классом TestAnsDigit. Для этого в программе вначале читается сам тест с помощью команд:
# descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при вычислении 2+2? | 4
# ans = float(ans) # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может
# Далее, вам необходимо создать объект класса TestAnsDigit с аргументами descr, ans, а аргумент max_error_digit должен
# принимать значение по умолчанию 0.01.
# Запустите тест командой run() и выведите на экран результат его работы (значение True или False). Если в процессе создания
# объекта класса TestAnsDigit или в процессе работы метода run() возникли исключения, то они должны быть обработаны и на
# экран выведено сообщение, содержащееся в исключении.
# Sample Input:
# Какое значение получим, при выполнении команды int(5.7)? | 5
# 6
# Sample Output:
# False
# from abc import ABC, abstractmethod
# class Test:
#     def __init__(self, descr):
#         if len(descr) > 10000 or len(descr) < 10:
#             raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
#         self.descr = descr
#
#
#     def run(self):
#         raise NotImplementedError
#
# class TestAnsDigit(Test):
#     def __init__(self, descr, ans_digit, max_error_digit=0.01):
#         super().__init__(descr)
#         try:
#             if int(ans_digit) < 0:
#                 raise ValueError('недопустимые значения аргументов теста')
#         except ValueError:
#             raise ValueError('недопустимые значения аргументов теста')
#         else:
#             self.ans_digit = int(ans_digit)
#         try:
#             if float(max_error_digit) < 0:
#                 raise ValueError('недопустимые значения аргументов теста')
#         except ValueError:
#             raise ValueError('недопустимые значения аргументов теста')
#         else:
#             self.max_error_digit = float(max_error_digit)
#
#
#
#     def run(self):
#         ans = float(input())
#         return self.ans_digit - self.max_error_digit <= ans <= self.ans_digit + self.max_error_digit
#
#
# descr, ans = map(str.strip, input().split('|'))
# descr, ans = map(str.strip, 'Какое значение получим, при выполнении команды int(5.7)? | 5'.split('|'))
# try:
#     tst = TestAnsDigit(descr, ans)
# except ValueError as e:
#     print(e)
# else:
#     print(tst.run())
#
# try:
#     test = Test('descr')
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError при вызове инициализатора класса Test с неверным набором аргументов"
#
# try:
#     test = Test('descr ghgfhgjg ghjghjg')
#     test.run()
# except NotImplementedError:
#     assert True
# else:
#     assert False
#
# assert issubclass(TestAnsDigit, Test)
#
# t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1)
# t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, 0.5)
#
# try:
#     t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, -0.5)
# except ValueError:
#     assert True
# else:
#     assert False


# =====================================================================================



# Подвиг 7. В программе выполняется считывание числовых данных из входного потока, командой:
# digits = list(map(float, input().split()))
# Эти данные следует представить в виде объекта класса TupleLimit. Сам класс должен наследоваться от класса tuple, а его объекты создаваться командой:
# tl = TupleLimit(lst, max_length)
# где lst - коллекция (список или кортеж) из данных; max_length - максимально допустимая длина коллекции TupleLimit.
# Если длина lst превышает значение max_length, то должно генерироваться исключение командой:
# raise ValueError('число элементов коллекции превышает заданный предел')
# В самом классе TupleLimit переопределить магические методы __str__() и __repr__() для отображения объекта класса
# TupleLimit в виде строки из набора данных lst, записанных через пробел. Например:
# "1.0 2.5 -5.0 11.2"
# Создайте в программе объект класса TupleLimit для прочитанных данных digits и параметром max_length = 5.
# Выведите на экран объект в случае его успешного создания. Иначе, выведите сообщение обработанного исключения.
# Sample Input:
# 1 2 3 4 5
# Sample Output:
# 1.0 2.0 3.0 4.0 5.0

# digits = list(map(float, '1 2 3 4 5'.split()))

# class TupleLimit(tuple):
#     def __new__(cls, lst, max_length):
#         # if len(lst) > max_length:
#         #     raise ValueError('число элементов коллекции превышает заданный предел')
#         instance = super().__new__(cls, lst)
#         instance.max_length = max_length
#         return instance
#     def __init__(self, lst, max_length):
#         if len(lst) > max_length:
#             raise ValueError('число элементов коллекции превышает заданный предел')
#         self.lst = lst
#         self.max_length = max_length
#
#     def __str__(self):
#         return ' '.join(list(map(str, self.lst)))
#
#     def __repr__(self):
#         return ' '.join(list(map(str, self.lst)))
#
# digits = list(map(float, input().split()))
# try:
#     tp = TupleLimit(digits, max_length=5)
# except ValueError as e:
#     print(e)
# else:
#     print(tp)
