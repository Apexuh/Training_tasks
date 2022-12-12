# __eq__ - для равенства ==
# __ne__ - для равенства !=
# __lt__ - для оператора меньше <
# __le__ - для оператора меньше или равно <=
# __gt__ - для оператора больше >
# __ge__ - для оператора больше или равно >=


# class Clock:
#     __DAY = 86400 # count of seconds
#
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError('Seconds must be "int" type')
#         self.seconds = seconds % self.__DAY
#
#     @classmethod
#     def __verify_data(cls, other):
#         if not isinstance(other, (Clock, int)):
#             raise TypeError('Ooops')
#         return other if isinstance(other, int) else other.seconds
#
#     def __eq__(self, other): # == and !=
#         sc = self.__verify_data(other)
#         return self.seconds == sc
#
#     def __lt__(self, other): # c1 < c2 and c1 > c2 (because c1 > c2 == c2 < c1 for interpretator)
#         sc = self.__verify_data(other)
#         return self.seconds < sc
#
#     def __le__(self, other): # <=
#         sc = self.__verify_data(other)
#         return self.seconds <= sc
#
# c1 = Clock(1000)
# c2 = Clock(1000)
# print(c1 == c2)
# c2 = 2000
# print(c1 == c2)
# print(c1 != c2) # true, то есть работает без метода __ne__ , тк интерпретатор читает оператор != как 'not =='
# print(c1 < c2)


# ==================================================================================================


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/cHV-yuNFavg
# Подвиг 3. Объявите класс Track (маршрут), объекты которого создаются командой:
# track = Track(start_x, start_y)
# где start_x, start_y - координаты начала маршрута (целые или вещественные числа).
# Каждый линейный сегмент маршрута определяется классом TrackLine, объекты которого создаются командой:
# line = TrackLine(to_x, to_y, max_speed)
# где to_x, to_y - координаты следующей точки маршрута (целые или вещественные числа); max_speed - максимальная скорость на данном участке (целое число).
# Для формирования и работы с маршрутом в классе Track должны быть объявлены следующие методы:
# add_track(self, tr) - добавление линейного сегмента маршрута (следующей точки);
# get_tracks(self) - получение кортежа из объектов класса TrackLine.
# Также для объектов класса Track должны быть реализованные следующие операции сравнения:
# track1 == track2  # маршруты равны, если равны их длины
# track1 != track2  # маршруты не равны, если не равны их длины
# track1 > track2  # True, если длина пути для track1 больше, чем для track2
# track1 < track2  # True, если длина пути для track1 меньше, чем для track2
# И функция:
# n = len(track) # возвращает целочисленную длину маршрута (привести к типу int) для объекта track
# Создайте два маршрута track1 и track2 с координатами:
# 1-й маршрут: (0; 0), (2; 4), (5; -4) и max_speed = 100
# 2-й маршрут: (0; 1), (3; 2), (10; 8) и max_speed = 90
# Сравните их между собой на равенство. Результат сравнения сохраните в переменной res_eq.
# P.S. На экран в программе ничего выводить не нужно.


# class Track:
#     def __init__(self, start_x, start_y):
#         self._start_x = start_x if isinstance(start_x, (int, float)) else 0
#         self._start_y = start_y if isinstance(start_y, (int, float)) else 0
#         self._tracks = []
#
#     def add_track(self, tr):
#         '''- добавление линейного сегмента маршрута (следующей точки);'''
#         self._tracks.append(tr)
#     def get_tracks(self):
#         '''- получение кортежа из объектов класса TrackLine.'''
#         return tuple(self._tracks)
#
#     def __len__(self):
#         len_1 = ((self._start_x - self._tracks[0].x) ** 2 + (self._start_y - self._tracks[0].y)**2) ** 0.5
#         return int(len_1 + sum(self._get_length(i) for i in range(1, len(self._tracks))))
#
#     def _get_length(self, i):
#         return ((self._tracks[i - 1].x - self._tracks[i].x) ** 2 + (self._tracks[i - 1].y - self._tracks[i].y) ** 2) ** 0.5
#
#     def __eq__(self, other):
#         return len(self) == len(other)
#
#     def __lt__(self, other):
#         return len(self) < len(other)
#
# class TrackLine:
#     def __init__(self, to_x, to_y, max_speed):
#         self._to_x = to_x if isinstance(to_x, (int, float)) else 0
#         self._to_y = to_y if isinstance(to_y, (int, float)) else 0
#         self._max_speed = max_speed if isinstance(max_speed, int) else 0
#
#     @property
#     def x(self):
#         return self._to_x
#
#     @property
#     def y(self):
#         return self._to_y
#
#     @property
#     def max_speed(self):
#         return self._max_speed
#
#
#
# track1 = Track(0,0)
# track1.add_track(TrackLine(2, 4, 100))
# track1.add_track(TrackLine(5, -4, 100))
# track2 = Track(0,1)
# track2.add_track(TrackLine(3,2,90))
# track2.add_track(TrackLine(10,8,90))
#
# res_eq = track1 == track2


# ===============================================================================================


# Подвиг 4. Объявите класс Dimensions (габариты) с атрибутами:
# MIN_DIMENSION = 10
# MAX_DIMENSION = 10000
# Каждый объект класса Dimensions должен создаваться командой:
# d3 = Dimensions(a, b, c)   # a, b, c - габаритные размеры
# Значения a, b, c должны сохраняться в локальных приватных атрибутах __a, __b, __c объектах этого класса.
# Для изменения и доступа к приватным атрибутам в классе Dimensions должны быть объявлены объекты-свойства (property)
# с именами: a, b, c. Причем, в момент присваивания нового значения должна выполняться проверка попадания числа в диапазон
# [MIN_DIMENSION; MAX_DIMENSION]. Если число не попадает, то оно игнорируется и существующее значение не меняется.
# С объектами класса Dimensions должны выполняться следующие операторы сравнения:
# dim1 >= dim2   # True, если объем dim1 больше или равен объему dim2
# dim1 > dim2    # True, если объем dim1 больше объема dim2
# dim1 <= dim2   # True, если объем dim1 меньше или равен объему dim2
# dim1 < dim2    # True, если объем dim1 меньше объема dim2
# Объявите в программе еще один класс с именем ShopItem (товар), объекты которого создаются командой:
# item = ShopItem(name, price, dim)
# где name - название товара (строка); price - цена товара (целое или вещественное число); dim - габариты товара (объект класса Dimensions).
# В каждом объекте класса ShopItem должны создаваться локальные атрибуты:
# name - название товара;
# price - цена товара;
# dim - габариты товара (объект класса Dimensions).
# Создайте список с именем lst_shop из четырех товаров со следующими данными:
# - кеды; 1024; (40, 30, 120)
# - зонт; 500.24; (10, 20, 50)
# - холодильник; 40000; (2000, 600, 500)
# - табуретка; 2000.99; (500, 200, 200)
# Сформируйте новый список lst_shop_sorted с упорядоченными по возрастанию объема (габаритов) товаров списка lst_shop, используя стандартную функцию sorted() языка Python и ее параметр key для настройки сортировки. Прежний список lst_shop должен оставаться без изменений.
# P.S. На экран в программе ничего выводить не нужно.

# class ShopItem:
#     def __init__(self, name, price, dim):
#         self.name = name
#         self.price = price
#         self.dim = dim
#
# class Dimensions:
#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 10000
#
#     def __init__(self, a, b, c):
#         self.__a = a
#         self.__b = b
#         self.__c = c
#
#     def __lt__(self, other):
#         return self.volume() < other.volume()
#
#     def __le__(self, other):
#         return self.volume() <= other.volume()
#
#     def volume(self):
#         return self.__a * self.__b * self.__c
#
#     @property
#     def a(self):
#         return self.__a
#
#     @a.setter
#     def a(self, a):
#         if self.__check_value(a):
#             self.__a = a
#
#     @property
#     def b(self):
#         return self.__b
#
#     @b.setter
#     def b(self, b):
#         if self.__check_value(b):
#             self.__b = b
#
#     @property
#     def c(self):
#         return self.__c
#
#     @c.setter
#     def c(self, c):
#         if self.__check_value(c):
#             self.__c = c
#
#     @classmethod
#     def __check_value(cls, x):
#         return cls.MIN_DIMENSION <= x <= cls.MAX_DIMENSION
#
#
# # Создайте список с именем lst_shop из четырех товаров со следующими данными:
# # - кеды; 1024; (40, 30, 120)
# # - зонт; 500.24; (10, 20, 50)
# # - холодильник; 40000; (2000, 600, 500)
# # - табуретка; 2000.99; (500, 200, 200)
#
#
# trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
# umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
# fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
# chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
# lst_shop = (trainers, umbrella, fridge, chair)
# lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.volume())
# print(list(map(lambda x: x.dim.volume(),lst_shop_sorted)))


# =======================================================================================================


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/k7PSxUf0w6g
# Подвиг 5. Имеется стихотворение, представленное следующим списком строк:
# stich = ["Я к вам пишу – чего же боле?",
#         "Что я могу еще сказать?",
#         "Теперь, я знаю, в вашей воле",
#         "Меня презреньем наказать.",
#         "Но вы, к моей несчастной доле",
#         "Хоть каплю жалости храня,",
#         "Вы не оставите меня."]
# Необходимо в каждой строчке этого стиха убрать символы "–?!,.;" в начале и в конце каждого слова и разбить строку по словам
# (слова разделяются одним или несколькими пробелами). На основе полученного списка слов, создать объект класса StringText командой:
# st = StringText(lst_words)
# где lst_words - список из слов одной строчки стихотворения. 
# С объектами класса StringText должны быть реализованы операторы сравнения:
# st1 > st2   # True, если число слов в st1 больше, чем в st2
# st1 >= st2  # True, если число слов в st1 больше или равно st2
# st1 < st2   # True, если число слов в st1 меньше, чем в st2
# st1 <= st2  # True, если число слов в st1 меньше или равно st2
# Все объекты класса StringText (для каждой строчки стихотворения) сохранить в списке lst_text. Затем, сформировать
# новый список lst_text_sorted из отсортированных объектов класса StringText по убыванию числа слов.
# Для сортировки использовать стандартную функцию sorted() языка Python. После этого преобразовать данный список
# (lst_text_sorted) в список из строк (объекты заменяются на соответствующие строки, между словами ставится пробел).
# P.S. На экран в программе ничего выводить не нужно.

# stich = ["Я к вам пишу – чего же боле?",
#         "Что я могу еще сказать?",
#         "Теперь, я знаю, в вашей воле",
#         "Меня презреньем наказать.",
#         "Но вы, к моей несчастной доле",
#         "Хоть каплю жалости храня,",
#         "Вы не оставите меня."]

# def string_to_list(i):
#     symbols = "–?!,.;"
#     for sym in symbols:
#         i = i.replace(sym, '')
#     return i.split()
#
# stich_lst = [string_to_list(i) for i in stich]
#
# class StringText:
#     def __init__(self, lst):
#         self.__lst = lst
#
#     def __len__(self):
#         return len(self.__lst)
#
#     def __lt__(self, other):
#         return len(self.__lst) < len(other.__lst)
#
#     def __le__(self, other):
#         return len(self.__lst) <= len(other.__lst)
#
#     def __call__(self, *args, **kwargs):
#         return self.__lst
#
# lst_text = [StringText(i) for i in stich_lst]
# lst_text_sorted = sorted(lst_text, key=lambda x: len(x), reverse=True)
# # print(lst_text_sorted)
# lst_text_sorted = list(map(lambda a: ' '.join(a),[i() for i in lst_text_sorted]))
# print(lst_text_sorted)


# ===================================================================================


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/PJsJOIxZOdM
# Подвиг 6. Ваша задача написать программу поиска слова в строке. Задача усложняется тем, что слово должно определяться
# в разных его формах. Например, слово:
# программирование
# может иметь следующие формы:
# программирование, программированию, программированием, программировании, программирования, программированиям,
# программированиями, программированиях
# Для решения этой задачи необходимо объявить класс Morph (морфология), объекты которого создаются командой:
# mw = Morph(word1, word2, ..., wordN)
# где word1, word2, ..., wordN - возможные формы слова.
# В классе Morph реализовать методы:
# add_word(self, word) - добавление нового слова (если его нет в списке слов объекта класса Morph);
# get_words(self) - получение кортежа форм слов.
# Также с объектами класса Morph должны выполняться следующие операторы сравнения:
# mw1 == "word"  # True, если объект mv1 содержит слово "word" (без учета регистра)
# mw1 != "word"  # True, если объект mv1 не содержит слово "word" (без учета регистра)
# И аналогичная пара сравнений:
# "word" == mw1
# "word" != mw1
# После создания класса Morph, формируется список dict_words из объектов этого класса, для следующих слов с их словоформами:
# - связь, связи, связью, связей, связям, связями, связях
# - формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
# - вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
# - эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
# - день, дня, дню, днем, дне, дни, дням, днями, днях
# Затем, прочитайте строку из входного потока командой:
# text = input()
# Найдите все вхождения слов из списка dict_words (используя операторы сравнения) в строке text (без учета регистра, знаков пунктуаций и их словоформы). Выведите на экран полученное число.
# Sample Input:
# Мы будем устанавливать связь завтра днем.
# Sample Output:
# 2
#

# text = input()

# class Morph:
#     def __init__(self, *args):
#         self.__lst = list(map(lambda x: x.strip(' .,!?;:').lower(), args))
#
#     def add_word(self, word):
#         w = word.lower()
#         if w not in self.__lst:
#             self.__lst.append(w)
#
#     def get_words(self):
#         return tuple(self.__lst)
#
#     def __eq__(self, other):
#         if isinstance(self, Morph):
#             return other.lower() in self.__lst
#         else:
#             return self.lower() in other.__lst
#
#
# dict_words = [Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
#                   Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
#                         'формулах'),
#                   Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
#                         'векторами', 'векторах'
#                         ),
#                   Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
#                         'эффектами', 'эффектах'
#                         ), Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях'
#                                  )]
# # text = 'Мы будем устанавливать связь завтра днем.'
# # text = 'daf'
# res = len(list(filter(lambda x: x in dict_words, list(set([i.strip(' .,;:!?') for i in text.lower().split()])))))
# print(res)


# ==========================================================================================================


# Подвиг 7 (на повторение). Перед вами стоит задача выделения файлов с определенными расширениями из списка файлов, например:
# filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
# Для этого необходимо объявить класс FileAcceptor, объекты которого создаются командой:
# acceptor = FileAcceptor(ext1, ..., extN)
# где ext1, ..., extN - строки с допустимыми расширениями файлов, например: 'jpg', 'bmp', 'jpeg'.
# После этого предполагается использовать объект acceptor в стандартной функции filter языка Python следующим образом:
# filenames = list(filter(acceptor, filenames))
# То есть, объект acceptor должен вызываться как функция:
# acceptor(filename) 
# и возвращать True, если файл с именем filename содержит расширения, указанные при создании acceptor, и False -
# в противном случае. Кроме того, с объектами класса FileAcceptor должен выполняться оператор:
# acceptor12 = acceptor1 + acceptor2
# Здесь формируется новый объект acceptor12 с уникальными расширениями первого и второго объектов. Например:
# acceptor1 = FileAcceptor("jpg", "jpeg", "png")
# acceptor2 = FileAcceptor("png", "bmp")
# acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")
# Пример использования класса (эти строчки в программе писать не нужно):
# acceptor_images = FileAcceptor("jpg", "jpeg", "png")
# acceptor_docs = FileAcceptor("txt", "doc", "xls")
# filenames = list(filter(acceptor_images + acceptor_docs, filenames))
# P.S. На экран в программе ничего выводить не нужно.

# filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls", 'yff.jg']
#
# class FileAcceptor:
#     def __init__(self, *args):
#         self._acceptor_list = list(args)
#
#     def __add__(self, other):
#         lst = self._acceptor_list[:]
#         for i in other._acceptor_list:
#             if i not in lst:
#                 lst.append(i)
#         return FileAcceptor(*lst)
#
#     def __call__(self, acceptor):
#         for i in self._acceptor_list:
#             search = f'.{i}'
#             if search == acceptor[-len(search):]:
#                 return True
#         return False
#
#
#     @property
#     def acceptor_list(self):
#         return self._acceptor_list

# acceptor1 = FileAcceptor("jpg", "jpeg", "png")
# print(acceptor1.acceptor_list)
# acceptor2 = FileAcceptor("png", "bmp")
# acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")
# print(acceptor12.acceptor_list)
# filenames = list(filter(acceptor, filenames))

# acceptor_images = FileAcceptor("jpg", "jpeg", "png")
# acceptor_docs = FileAcceptor("txt", "doc", "xls")
# filenames = list(filter(acceptor_images + acceptor_docs, filenames))
# print(filenames)


# ============================================================================================


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/qKTQLo-plpc
# Подвиг 8. В программе необходимо объявить классы для работы с кошельками в разных валютах:
# MoneyR - для рублевых кошельков
# MoneyD - для долларовых кошельков
# MoneyE - для евро-кошельков
# https://ucarecdn.com/c892d3ab-647c-4827-b0d0-61d2f7135bef/
# Объекты этих классов могут создаваться командами:
# rub = MoneyR()   # с нулевым балансом
# dl = MoneyD(1501.25) # с балансом в 1501.25 долларов
# euro = MoneyE(100)  # с балансом в 100 евро
# В каждом объекте этих классов должны формироваться локальные атрибуты:
# __cb - ссылка на класс CentralBank (центральный банк, изначально None);
# __volume - объем денежных средств в кошельке (если не указано, то 0).
# Также в классах MoneyR, MoneyD и MoneyE должны быть объекты-свойства (property) для работы с локальными атрибутами:
# cb - для изменения и считывания данных из переменной __cb;
# volume - для изменения и считывания данных из переменной __volume.
# Объекты классов должны поддерживать следующие операторы сравнения:
# rub < dl
# dl >= euro
# rub == euro  # значения сравниваются по текущему курсу центрального банка с погрешностью 0.1 (плюс-минус)
# euro > rub
# При реализации операторов сравнения считываются соответствующие значения __volume из сравниваемых объектов
# и приводятся к рублевому эквиваленту в соответствии с курсом валют центрального банка.
# Чтобы каждый объект классов MoneyR, MoneyD и MoneyE "знал" текущие котировки, необходимо
# в программе объявить еще один класс CentralBank. Объекты класса CentralBank создаваться не должны (запретить), при выполнении команды:
# cb = CentralBank()
# должно просто возвращаться значение None. А в самом классе должен присутствовать атрибут:
# rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
# Здесь числа (в значениях словаря) - курс валюты по отношению к доллару. 
# Также в CentralBank должен быть метод уровня класса:
# register(cls, money) - для регистрации объектов классов MoneyR, MoneyD и MoneyE.
# При регистрации значение __cb объекта money должно ссылаться на класс CentralBank. Через эту переменную объект
# имеет возможность обращаться к атрибуту rates класса CentralBank и брать нужные котировки.
# Если кошелек не зарегистрирован, то при операциях сравнения должно генерироваться исключение:
# raise ValueError("Неизвестен курс валют.")
# Пример использования классов (эти строчки в программе писать не нужно):
# CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
# r = MoneyR(45000)
# d = MoneyD(500)
# CentralBank.register(r)
# CentralBank.register(d)
# if r > d:
#     print("неплохо")
# else:
#     print("нужно поднажать")
# P.S. В программе на экран ничего выводить не нужно, только объявить классы.

# class CentralBank:
#     rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
#
#     def __new__(cls, *args, **kwargs):
#         return
#
#     @classmethod
#     def register(cls, money):
#         money.cb = cls
#
#
# class Money:
#     type_money = None
#     EPS = 0.1
#
#     def __init__(self, volume=0):
#         self.__volume = volume
#         self.__cb = None
#
#     @property
#     def volume(self):
#         return self.__volume
#
#     @volume.setter
#     def volume(self, volume):
#         self.__volume = volume
#
#     @property
#     def cb(self):
#         return self.__cb
#
#     @cb.setter
#     def cb(self, cb):
#         self.__cb = cb
#
#     def get_volumes(self, other):
#         if self.cb is None:
#             raise ValueError("Неизвестен курс валют.")
#         if self.type_money is None:
#             raise ValueError("Type data is None")
#         a = self.volume / self.cb.rates[self.type_money]
#         b = other.volume / other.cb.rates[self.type_money]
#         return a, b
#
#     def __lt__(self, other):
#         a, b = self.get_volumes(other)
#         return a < b
#
#     def __le__(self, other):
#         a, b = self.get_volumes(other)
#         return a <= b
#
#     def __eq__(self, other):
#         a, b = self.get_volumes(other)
#         return abs(a - b) < self.EPS
#
#
# class MoneyR(Money):
#     type_money = 'rub'
#
#
# class MoneyD(Money):
#     type_money = 'dollar'
#
#
# class MoneyE(Money):
#     type_money = 'euro'


# CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
# r = MoneyR(45000)
# d = MoneyD(500)
# e = MoneyE(450)
# CentralBank.register(r)
# CentralBank.register(d)
# CentralBank.register(e)
# print()
# print(r < e)



# ANOTHER WAY



# class CentralBank:
#     rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
#
#     def __new__(cls):
#         return None
#
#     @classmethod
#     def register(cls, money):
#         if isinstance(money, Money):
#             money.cb = cls
#
#
# class Money:
#     def __init__(self, volume=0):
#         self.__cb = None
#         self.__volume = volume
#
#     def __eq__(self, other):
#         if isinstance(other, Money):
#             return self.valuate() == other.valuate()
#
#     def __lt__(self, other):
#         if isinstance(other, Money):
#             return self.valuate() < other.valuate()
#
#     def __le__(self, other):
#         if isinstance(other, Money):
#             return self.valuate() <= other.valuate()
#
#     @property
#     def cb(self):
#         return self.__cb
#
#     @cb.setter
#     def cb(self, value):
#         if value is CentralBank:
#             self.__cb = value
#
#     @property
#     def volume(self):
#         return self.__volume
#
#     @volume.setter
#     def volume(self, value):
#         if type(value) in (int, float):
#             self.__volume = value
#
#     def valuate(self):
#         if self.cb:
#             return round(self.volume / self.cb.rates[self.currency_name], 1)
#         raise ValueError("Неизвестен курс валют.")
#
#
# class MoneyR(Money):
#     currency_name = 'rub'
#
#
# class MoneyD(Money):
#     currency_name = 'dollar'
#
#
# class MoneyE(Money):
#     currency_name = 'euro'




# ====================================================================================================




# Подвиг 9 (релакс). Необходимо объявить класс Body (тело), объекты которого создаются командой:
# body = Body(name, ro, volume)
# где name - название тела (строка); ro - плотность тела (число: вещественное или целочисленное);
# volume - объем тела  (число: вещественное или целочисленное).
# Для объектов класса Body должны быть реализованы операторы сравнения:
# body1 > body2  # True, если масса тела body1 больше массы тела body2
# body1 == body2 # True, если масса тела body1 равна массе тела body2
# body1 < 10     # True, если масса тела body1 меньше 10
# body2 == 5     # True, если масса тела body2 равна 5
# Масса тела вычисляется по формуле:
# m = ro * volume
# P.S. В программе только объявить класс, выводить на экран ничего не нужно.


# class Body:
#     def __init__(self, name, ro, volume):
#         self.name = name
#         self.ro = ro
#         self.volume = volume
#
#     @property
#     def mass(self):
#         return self.ro * self.volume
#
#     def __eq__(self, other):
#         mass = other
#         if isinstance(other, Body):
#             mass = other.mass
#         return self.mass == mass
#
#     def __lt__(self, other):
#         mass = other
#         if isinstance(other, Body):
#             mass = other.mass
#         return self.mass < mass
#
#     def __gt__(self, other):
#         mass = other
#         if isinstance(other, Body):
#             mass = other.mass
#         return self.mass > mass
#
#
# r = Body('dfsdf', 3, 5)
# print(r < 20)



# =======================================================================================================

# Подвиг 10. Объявите в программе класс с именем Box (ящик), объекты которого должны создаваться командой:
# box = Box()
# А сам класс иметь следующие методы:
# add_thing(self, obj) - добавление предмета obj (объект другого класса Thing) в ящик;
# get_things(self) - получение списка объектов ящика.
# Для описания предметов необходимо объявить еще один класс Thing. Объекты этого класса должны создаваться командой:
# obj = Thing(name, mass)
# где name - название предмета (строка); mass - масса предмета (число: целое или вещественное).
# Объекты класса Thing должны поддерживать операторы сравнения:
# obj1 == obj2
# obj1 != obj2
# Предметы считаются равными, если у них одинаковые названия name (без учета регистра) и массы mass.
# Также объекты класса Box должны поддерживать аналогичные операторы сравнения:
# box1 == box2
# box1 != box2
# Ящики считаются равными, если одинаковы их содержимое (для каждого объекта класса Thing одного ящика и
# можно найти ровно один равный объект из второго ящика).
# Пример использования классов:
# b1 = Box()
# b2 = Box()
# b1.add_thing(Thing('мел', 100))
# b1.add_thing(Thing('тряпка', 200))
# b1.add_thing(Thing('доска', 2000))
# b2.add_thing(Thing('тряпка', 200))
# b2.add_thing(Thing('мел', 100))
# b2.add_thing(Thing('доска', 2000))
# res = b1 == b2 # True
# P.S. В программе только объявить классы, выводить на экран ничего не нужно.

# class Box:
#     def __init__(self):
#         self.__list_box = []
#
#     def add_thing(self, obj):
#         self.__list_box.append(obj)
#
#     def get_things(self):
#         return self.__list_box
#
#     def __eq__(self, other):
#         return all(list(map(lambda x: x in other.__list_box, self.__list_box)))
#
# class Thing:
#     def __init__(self, name, mass):
#         self.__name = name.lower()
#         self.__mass = mass
#
#     def __eq__(self, other):
#         return self.__mass == other.__mass and self.__name == other.__name

# b1 = Box()
# b2 = Box()
# b1.add_thing(Thing('мел', 100))
# b1.add_thing(Thing('тряпка', 200))
# b1.add_thing(Thing('доска', 2000))
# b2.add_thing(Thing('тряпка', 200))
# b2.add_thing(Thing('мел', 100))
# b2.add_thing(Thing('доска', 2000))
# res = b1 == b2 # True
# print(res)