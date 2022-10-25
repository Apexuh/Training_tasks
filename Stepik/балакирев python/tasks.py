# # ввод целого числа
# d = int(input())
#
# # здесь продолжите программу
# # from math import abs
# print(abs(d))


# # ввод данных
# a, b = map(int, input().split())
#
# # здесь продолжите программу
# print(round((a ** 2 + b ** 2)**0.5,2))


# # ввод данных
# n, k = map(int, input().split())
#
# # здесь продолжите программу
# from math import factorial
# print(int(factorial(n)/(factorial(k)*factorial(n-k))))


# 2.3
# # ввод данных
# import math
#
# n, m = map(int, input().split())
#
# # здесь продолжите программу
# print(math.ceil((n+m)/20))


# a = 7
# b = -4
# c = 3
# print(a,b,c,sep="\n")


# 2.5
# 78.34
# n = round(float(input()))
# print(n % 3 == 0)


# import math
# n = float(input())
# m = math.floor(n)
# print(n - m >=0.50)


# put your python code here
# 8 11 12
# a, b, c = map(int, input().split())
# print(a + b > c and a+c>b and b+c>a)


# s1, s2 = input().split()
# print((s1 + ' ')*2, (s2 + ' ') * 3, sep='')


# hello python
# s1, s2 = input().split()
# print(s1 in s2, s1 == s2, s1 > s2, s1 < s2, sep=' ')

# a, b = input().split()
# print(f'Коды: {a} = {ord(a)}, {b} = {ord(b)}')


# n = 'dsfdsf'
# print(n.capitalize())


# 3.4
# n = r'C:\WINDOWS\System32\drivers\etc\hosts'
# print(n)


# marks = list(map(int, input().split()))
# print(round(sum(marks)/len(marks),1))


# put your python code here
# n = int(input())
# n = 8
# fib1 = 1
# fib2 = 1
# k = 0
# print(fib1, fib2, end=' ')
# while k < n -2:
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')
#     k += 1


# p = [0] * 10
# while p.count(1) < 5:
#     k = int(input)
#     if p[k] == 1:
#         continue
#     else:
#         p[k] = 1
# print(*p)


# st = input()
# yes = []
# for i in range(len(st)-1):
#
#     if st[i] + st[i+1] == 'ра':
#         yes.append(i)
# print(yes)


# n = input().replace(' ','')
# k = ''
# sum = 0
# c = 0
# d = ''
# for i,v in enumerate(n):
#     if c == 0:
#         if v in ['+', '-']:
#             c += 1
#             sum += int(k)
#             k = ''
#             d = v
#             continue
#         k += v
#         continue
#     if v in ['+', '-']:
#
#         if d == '+':
#             sum += int(k)
#             k = ''
#
#         elif d == '-':
#             sum -= int(k)
#             k = ''
#         d = v
#         continue
#     k += v
#     if i == len(n) - 1:
#         if d == '+':
#             sum += int(k)
#             k = ''
#
#         elif d == '-':
#             sum -= int(k)
#             k = ''
#
#
#
#
# print(sum)


# iter(True)
# iter(7)
# iter("")
# iter([])
# iter("python")
# iter([1, True, "abc", -5.6])


# lst_in = [[1, 0, 0, 1, 0],
#           [0, 0, 1, 0, 1],
#           [0, 0, 0, 0, 0],
#           [0, 1, 0, 1, 0],
#           [0, 0, 0, 0, 1]]
# print(lst_in)
# yes = True
# for i in range(len(lst_in)):
#     lst_in[i].insert(0, 0)
#     lst_in[i].append(0)
# lst_in.insert(0, [0] * len(lst_in[0]))
# lst_in.append([0] * len(lst_in[0]))
#
# for i1, v1 in enumerate(lst_in):
#     if 1 not in v1:
#         continue
#     for i2, v2 in enumerate(v1):
#         if v2 == 1:
#             if 1 in [lst_in[i1 - 1][i2 - 1:i2 + 1]]:
#                 yes = False
#                 break
#             if 1 in [lst_in[i1][i2 - 1], lst_in[i1][i2 - 1]]:
#                 yes = False
#                 break
#             if 1 in [lst_in[i1 + 1][i2 - 1], lst_in[i1 + 1][i2], lst_in[i1 + 1][i2 + 1]]:
#                 yes = False
#                 break
#     if yes == False:
#         break
# print('ДА' if yes else 'НЕТ')


# сортировка методом пузырька
# n = '4 5 2 0 6 3 -56 3 -1'
# a = list(map(int, n.split()))
#
# for i in range(len(a) - 1):
#     for j in range(len(a) - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
# print(*a)


# put your python code here
# n = int(input())
# k = []
# lst = [64, 32, 16, 8, 4, 2, 1]
# for i in lst:
#     if n // i > 0:
#         k.append([i] * (n//i))
#         n = n % i
#
# print(*k)


# треугольник паскаля
# N = 7
# P = []
#
# for i in range(N):
#     row = [1] * (i + 1)
#     for j in range(i + 1):
#         if j != 0 and j != i:
#             row[j] = P[i -1][j - 1] + P[i-1][j]
#     P.append(row)
# print(P)
# print(*P)
# [print(*i, end=' ') for i in P]


# put your python code here
# матрица из 0 с 1 по главной диагонали
# n = int(input())
# lst = [[1 if i == j else 0  for i in range(n)] for j in range(n)]
# [print(*i) for i in lst]

# lst = 'Москва 15000 Уфа 1200 Самара 1090 Казань 1300'.split()
# # lst = input().split()
# lst2 = [[lst[i], int(lst[i + 1])] for i in range(0,len(lst)-1,2)]
# print(lst2)


# lst = [
#     f'{i} * {j} = {i * j}'
#     for i in range(1,4)
#     for j in range(4) if j > 0
# ]
# print(*lst,sep='\n')

# матрица задом-наперед
# lst_in = [[1, 2, 3, 4],
#         [5, 6, 7, 8],
#         [9, 8, 7, 6],
#         [5, 4, 3, 2]]
#
# lst_out = [[print(j, end=' ') for j in reversed(lst_in[-i])] for i in range(1,len(lst_in)+1)]


# сформировать квадратную матрицу из строки

# inp = '1 2 3 4 5 6 7 8 9'.split()
# len_inp = 0
# for i in range(1, 20):
#     if len(inp) // i == i:
#         len_inp = i
#
# lst_out = [[int(inp[i + j]) for i in range(len_inp)] for j in range(0,len(inp),len_inp)]
# print(lst_out)


# преобразовать список строк в список списков слов с исключением слов длиной больше 3 символов
# t = ["– Скажи-ка, дядя, ведь не даром",
#     "Я Python выучил с каналом",
#     "Балакирев что раздавал?",
#     "Ведь были ж заданья боевые,",
#     "Да, говорят, еще какие!",
#     "Недаром помнит вся Россия",
#     "Как мы рубили их тогда!"
#     ]
#
# lst = [[j for j in i.split() if len(j) > 3] for i in t]
# print(lst)


# транспонировать матрицу (поворот на 90 по часовой)
# lst_in = [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9],
#         [5, 4, 3]]
# # lst_another = []
# # row , col = len(lst_in), len(lst_in[0])
# # lst_next = [[lst_another.append(lst_in[j][i]) for i in range(len(lst_in[j]))] for j in range(len(lst_in))]
# # lst_out = [[lst_another[i + j] for i in range(0,len(lst_another),col)] for j in range(col)]
# # [print(*i) for i in lst_out]
#
# # another way
# a = [[row[i] for row in lst_in] for i in range(len(lst_in[0]))]
# for row in a:
#     print(*row)


# inp = 'one=1 two=2 three=3'.split()
# d = {}
# for i in inp:
#         k = i.split('=')
#         d[k[0]]= int(k[1])
# print(*sorted(d.items()))

# into dict
# lst_in = ['5=отлично', '4=хорошо', '3=удовлетворительно']
#
# d = dict([[int(i.split('=')[0]), i.split('=')[1]] for i in lst_in])
# print(d)


# test if values in dict

# inp='вологда=город house=дом True=1 5=отлично 9=божественно'
# inp= input()
# d = dict([[i.split('=')[0], i.split('=')[1]] for i in inp.split()])
# find_value = ['house', 'True', '5']
# yes_value = ['yes' if i in d else 'no' for i in find_value]
# print('НЕТ' if 'no' in yes_value else 'ДА')


# find keys and terminate))
# inp = 'лена=имя дон=река москва=город False=ложь 3=удовлетворительно True=истина'
# inp = input()
# erase_keys = ['False', '3']
# d = dict([[i.split('=')[0], i.split('=')[1]] for i in inp.split() if i.split('=')[0] not in erase_keys])
#
# print(*sorted(d.items()))


# numbers to dict
# inp = '+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890'
# inp = input()
# inp_list = inp.split()
# print(inp_list)
# d = {}
# for i in inp_list:
#         if i[0:2] in d:
#                     d[i[0:2]] += [i]
#         else:
#                 d[i[0:2]] = [i]
# print(*sorted(d.items()))


# address_book
# lst_in = ['+71234567890 Сергей', '+71234567810 Сергей', '+51234567890 Михаил', '+72134567890 Николай']
# d = {}
# for i in lst_in:
#         k = i.split()
#         if k[1] in d:
#                 d[k[1]] += [k[0]]
#         else:
#                 d[k[1]] = [k[0]]
# print(*sorted(d.items()))


# square with dict
# d = {}
# while True:
#         inp = int(input())
#         if inp == 0:
#                 break
#         else:
#                 out = round(inp**0.5,2)
#                 if inp not in d:
#                         d[inp] = out
#                         print(out)
#                 else:
#                         print('значение из кэша:', out)


# sum of numbers which multiples 5 and 3
# print(sum([i for i in range(1,int(input())) if (i % 3 == 0 and i % 5 == 0)]))


# "HTML-страница для адреса <URL-адрес>"
# lst_in = ['ustanovka-i-zapusk-yazyka', 'ustanovka-i-poryadok-raboty-pycharm',
#           'peremennyye-operator-prisvaivaniya-tipy-dannykh', 'arifmeticheskiye-operatsii',
#           'ustanovka-i-poryadok-raboty-pycharm']
# d = []
# for inp in lst_in:
#     if inp not in d:
#         d.append(inp)
#         print(f'HTML-страница для адреса {inp}')
#     else:
#         print(f'Взято из кэша: HTML-страница для адреса {inp}')


# morze
# d = {
#         "А": ".-", "Б": "-...", "В": ".--","Г": "--.", "Д": "-..", "Е": ".", "Ж": "...-", "З": "--..",
#         "И": "..", "Й": ".---", "К": "-.-", "Л": ".-..", "М": "--", "Н": "-.", "О": "---", "П": ".--.",
#         "Р": ".-.", "С": "...", "Т": "-", "У": "..-", "Ф": "..-.", "Х": "....", "Ц": "-.-.", "Ч": "---.",
#         "Ш": "----", "Щ": "--.-", "Ъ": "--.--", "Ы": "-.--", "Ь": "-..-", "Э": "..-..", "Ю": "..--", "Я": ".-.-", " ": "-...-"
#      }
# for key in input().upper():
#         print(d[key], end=' ')


# morze to text
# d = {
#     "А": ".-", "Б": "-...", "В": ".--", "Г": "--.", "Д": "-..", "Е": ".", "Ж": "...-", "З": "--..",
#     "И": "..", "Й": ".---", "К": "-.-", "Л": ".-..", "М": "--", "Н": "-.", "О": "---", "П": ".--.",
#     "Р": ".-.", "С": "...", "Т": "-", "У": "..-", "Ф": "..-.", "Х": "....", "Ц": "-.-.", "Ч": "---.",
#     "Ш": "----", "Щ": "--.-", "Ъ": "--.--", "Ы": "-.--", "Ь": "-..-", "Э": "..-..", "Ю": "..--", "Я": ".-.-",
#     " ": "-...-"
# }
# d1 = {}
# for i, v in d.items():
#     d1[v] = i
#
# # inp = '.-- ... . -...- .-- . .-. -. ---'
# inp = input()
# lst_out = [d1[i].lower() for i in inp.split()]
# print(*lst_out, sep = '')


# individual numbers without set
# inp = list(map(int, '8 11 -4 5 2 11 4 8'.split()))
# inp = list(map(int, input().split()))
#
# d = {}
# for i in inp:
#         if i not in d:
#                 d.setdefault(i)
# print(*d.keys())


# lst in dict
# lst_in = ['3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана']
# d = {}
# for i in lst_in:
#         key, value = int(i.split()[0]), i.split()[1]
#         if key not in d:
#                 d[key] = [value]
#         else:
#                 d[key] += [value]
# print(d)


# weight in Sergey's bag
# things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
#           'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
#           'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
# things = dict(sorted(things.items(), key=lambda i: i[1],reverse=True))
# inp = int(input())*1000
# # inp = 10000
# out = []
# for key, value in things.items():
#         if inp >= value:
#                 inp -= value
#                 out.append(key)
#
# print(*out)


# Воронеж Самара Тольятти Ульяновск Пермь
# inp = tuple(input().split())
# t = inp if "Ульяновск" not in inp else inp[0:inp.index("Ульяновск")] + inp[inp.index("Ульяновск")+1:]
# print(*t)


# t = ((1, 0, 0, 0, 0),
#      (0, 1, 0, 0, 0),
#      (0, 0, 1, 0, 0),
#      (0, 0, 0, 1, 0),
#      (0, 0, 0, 0, 1))
# # size = int(input())
# size = 3
# # t2 = tuple((t[i] for i in range(size)) for j in range(size))
# t2 = tuple()
# for i in range(size):
#         k = tuple()
#         for j in range(size):
#                 k += (t[i][j],)
#         print(*k)


# lst_in = ['Главная home', 'Python learn-python', 'Java learn-java', 'PHP learn-php']
# t = tuple(tuple(i.split()) for i in lst_in)
# print(t)


# unique numbers in str, if no number print NO
# inp = 'Python  - best language!'
# # inp = input()
# s = set(filter(lambda x: x.isdigit(), inp))
# print(*sorted(s) if len(s) > 0 else ['НЕТ'])


# unique commentators

# lst_in = ['EvgeniyK: спасибо большое!', 'LinaTroshka: лайк и подписка!', 'Sergey Karandeev: крутое видео!', 'Евгений Соснин: обожаю', 'EvgeniyK: это повтор?', 'Sergey Karandeev: нет, это новое видео']
# s = set(map(lambda x: x.split(':')[0],lst_in))
# print(len(s))


# in set 1 or set 2
# setA, setB = set(map(int, input().split())),set(map(int, input().split()))
# print(*sorted(setA ^ setB))

# dict of scores . first number = second value
# inp = '1 ужасно неудовлетворительно удовлетворительно прилично отлично'
# inp = input()
# i1, l = int(inp.split()[0]), inp.split()[1:]
# l1 = [i for i in range(i1, len(l)+i1)]
# d = dict(zip(l1, l))
# print(d)

# another way
# n, *st = input().split()
# d = {key: value for key, value in enumerate(st, start=int(n))}
# print(d[4])


# unique words with len > 2 symbols
# input_data = 'Хижина изба машина и снова хижина машина'
# input_data = input()
# inp = {i.lower() for i in input_data.split() if len(i.lower()) > 2}
#
# print(len(inp))


# how many times we got 'и' i our phrase
# inp = 'И что сказать и что сказать и нечего и точка'
# inp = input()
# l = list(map(lambda x: x.lower(), inp.split()))
# d = {key: l.count(key) for key in l}
# print(d['и'] if 'и' in d else 0)


# lst_in = ['Пушкин: Сказака о рыбаке и рыбке', 'Есенин: Письмо к женщине', 'Тургенев: Муму', 'Пушкин: Евгений Онегин', 'Есенин: Русь']
# d = dict()
# for item in lst_in:
#     name, novel = item.split(': ')
#     if name not in d:
#         d[name] = {novel}
#     else:
#         d[name] |= {novel}
# print(d)


# def power_2(mini, maxi):
#     return mini * maxi
#
# lst = list(map(int, input().split()))
# print(power_2(min(lst), max(lst)))


# from time import time
#
# def get_nod(a, b):
#     """
#     вычисляется НОД (наибольший общий делитель) для двух чисел по медленному методу евклида
#     :param a: целое число 1
#     :param b: целое число 2
#     :return: возвращает НОД
#     """
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a
#
#
# def get_nod_fast(a, b):
#     """
#     вычисляется НОД (наибольший общий делитель) для двух чисел по быстрому методу евклида
#     :param a: целое число 1
#     :param b: целое число 2
#     :return: возвращает НОД
#     """
#     if a < b:
#         a, b = b, a
#
#     while b > 0:
#         a ,b = b, a % b
#     return a
#
# def test_nod(func):
#     # ---test n1
#     a = 28
#     b = 35
#     if func(a, b) == 7:
#         print('#test 1 - ok')
#     else:
#         print('#test 1 - fail')
#
#
#     # ---test n2
#     a = 1
#     b = 1000
#     if func(a, b) == 1:
#         print('#test 2 - ok')
#     else:
#         print('#test 2 - fail')
#
#
#     # ---test n3
#     st = time()
#     a = 2
#     b = 100000000
#     f = func(a, b)
#     et = time() - st
#     if f == 2 and et < 1:
#         print('#test 3 - ok')
#     else:
#         print('#test 3 - fail')
#
#
# test_nod(get_nod)
# test_nod(get_nod_fast)
# # help(get_nod)


# Проверка равенства строк через фактические и формальные параметры
# def cmp_str(s1, s2, reg=False, trim=True):
#     if reg:
#         s1 = s1.lower()
#         s2 = s2.lower()
#     if trim:
#         s1 = s1.strip()
#         s2 = s2.strip()
#     return s1 == s2
#
#
# print(cmp_str('Python', 'PYTHON', reg=True))

# пример работы с формальным параметров в виде списка(так делать нельзя)
# def add_value(value, lst=[]):
#     lst.append(value)
#     return lst
#
# l = add_value(1)
# l = add_value(2)
# print(l) #будет [1, 2], тк ссылка на изменяемый обьект, лучше кортеж


# def add_value(value, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(value)
#     return lst
#
#
# l = add_value(1)
# l = add_value(2)
# print(l)
# l = add_value(5, l)
# print(l)


# Объявите функцию с именем get_rect_value, которая принимает два аргумента (два числа) и
# еще один формальный параметр type с начальным значением 0.
# Если параметр type равен нулю, то функция должна возвращать периметр прямоугольника, а иначе - его площадь.

# def get_rect_value(a, b, type=0):
#     return (a + b) * 2 if type == 0 else a * b


# Объявите функцию с именем check_password, которая принимает аргумент - строку (пароль) и имеет один формальный параметр
# chars с начальным значением в виде строки "$%!?@#".
# Функция должна проверять: есть ли в пароле хотя бы один символ из chars и что длина пароля не менее 8 символов.
# Если проверка проходит, то функция возвращает True, иначе - False.

# P. S. Вызывать функцию не нужно, только объявить.

# def check_password(password, chars="$%!?@#"):
#     d = set(chars).intersection(set(password))
#     return True if len(d) > 0 and len(password) > 7 else False
#
#
# print(check_password('1234567ghjghj'))


# Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу,
# используя следующий словарь для замены русских букв на соответствующее латинское написание:
#
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# Функция должна возвращать преобразованную строку. Замены делать без учета регистра (исходную строку перевести в
# нижний регистр - малые буквы). У функции также определить формальный параметр sep с начальным значением в виде строки "-".
# Он будет определять символ для замены пробелов в строке.
#
# После объявления функции прочитайте (с помощью функции input) строку и дважды вызовите функцию (с выводом результата ее работы на экран):
#
# - первый раз только со строкой
# - второй раз со строкой и именованным аргументом sep со значением '+'.

# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# def replace_symbol(symbol):
#     return t[symbol]
#
# def rus_to_lat(str, sep='-'):
#     str = str.lower()
#     for i in str:
#         if i in t:
#             str = str.replace(i, t[i])
#         elif i == ' ':
#             str = str.replace(i, sep)
#     print(str)
#
# rus_to_lat('Лучший курс по Python!')
# rus_to_lat('Лучший курс по Python!', sep='+')


# здесь продолжайте программу
# def kir_lat(st, sep='-'):
#     lst = ''.join([t[i] if i in t else i for i in st ]).replace(' ', sep)
#     return lst
#
#
# st = input().lower()
# print(kir_lat(st))
# print(kir_lat(st, sep='+'))


# Объявите функцию, которая принимает строку и заключает ее в указанный тег. Тег определяется формальным параметров tag с начальным значением в виде строки "h1". Например, мы передаем строку "Hello Python" и заключаем в тег "h1". На выходе должны получить строку (без кавычек):
#
# "<h1>Hello Python</h1>"
#
# То есть, сначала открывается тег <h1>, а в конце строки - закрывается </h1>. И так для любых указанных тегов.
#
# После объявления функции прочитайте (с помощью функции input) строку и дважды вызовите функцию (с выводом результата ее работы на экран):
#
# - первый раз только со строкой
# - второй раз со строкой и именованным аргументом tag со значением 'div'.
#
# Sample Input:
#
# Работаем с функциями
#
# Sample Output:
#
# <h1>Работаем с функциями</h1>
# <div>Работаем с функциями</div>


# def html(str, tag ='h1'):
#     return f'<{tag}>{str}</{tag}>'
#
# # str = 'Работаем с функциями'
# str = input()
# print(html(str))
# print(html(str, tag='div'))


# дополнительно добавить тег up
# def html(str, tag ='h1', up=True):
#     if up:
#         tag = tag.upper()
#     return f'<{tag}>{str}</{tag}>'
#
# str = 'Работаем с функциями'
# # str = input()
# print(html(str))
# print(html(str, tag='div'))
# print(html(str,tag='div', up=False))


# Объявите функцию с именем get_even, которая принимает произвольное количество чисел в качестве аргументов и
# возвращает список, составленный только из четных переданных значений.
# Функцию выполнять не нужно, только определить.
# Sample Input:
#
# 45 4 8 11 12 0
#
# Sample Output:
#
# 4 8 12 0

# def get_even(*args):
#     return [i for i in args if i % 2 ==0]


# def get_biggest_city(*args):
#     lst = ' '.join(args).split()
#     return max(lst, key=len)
#
# print(get_biggest_city('Питер Москва Самара Воронеж'))


# Объявите функцию с именем get_data_fig для вычисления периметра произвольного N-угольника.
# На вход этой функции передаются N длин сторон через аргументы. Дополнительно могут быть указаны именованные аргументы:
#
# type - булево значение True/False
# color - целое числовое значение
# closed - булево значение True/False
# width - целое значение
#
# Функция должна возвращать в виде кортежа периметр многоугольника и указанные значения именованных параметров в
# порядке их перечисления в тексте задания (если они были переданы). Если какой-либо параметр отсутствует,
# его возвращать не нужно (пропустить).
# Функцию выполнять не нужно, только определить.

# def get_data_fig(*args, **kwargs):
#    s = (sum(args),)
#    k = ['type', 'color', 'closed', 'width']
#    for i in k:
#        if i in kwargs:
#            s += (kwargs[i],)
#    return print(s)


# another way
# def get_data_fig(*args, **kwargs):
#     kwargs = [kwargs[i] for i in ['type', 'color', 'closed', 'width'] if i in kwargs]
#     return (sum(args), *kwargs)
#
# get_data_fig(3, 4, 5)
# # (12,)
#
# get_data_fig(3, 4, 5, type=True, color=256, closed=False, width=5)
# # (12, True, 256, False, 5)
#
# get_data_fig(3, 4, 5, width=6, color=128)
# # (12, 6, 128)


# Большой подвиг 6. (Для закрепления предыдущего материала). Вводится таблица целых чисел (см. пример ниже) размером N x N
# элементов (N определяется по входным данным). Эта таблица содержит нули, но кое-где - единицы. С помощью функции с именем verify,
# на вход которой передается двумерный список чисел, необходимо проверить, являются ли единицы изолированными друг от друга,
# то есть, вокруг каждой единицы должны быть нули.
#
# Рекомендуется следующий алгоритм. В функции verify производить перебор двумерного списка. Для каждого элемента (списка)
# со значением 1 вызывать еще одну вспомогательную функцию is_isolate для проверки изолированности единицы.
# То есть, функция is_isolate должна возвращать True, если единица изолирована и False - в противном случае.
#
# Как только встречается не изолированная единица, функция verify должна возвращать False. Если успешно доходим
# (по элементам списка) до конца, то возвращается значение True.
#
# Функцию выполнять не нужно, только определить.
#
# P. S. При реализации функции is_isolate не следует прописывать восемь операторов if. Подумайте, как это можно сделать
# красивее (с точки зрения реализации алгоритма).
#
# Sample Input:
#
# 1 0 0 0 0
# 0 0 1 0 0
# 0 0 0 0 0
# 0 1 0 1 0
# 0 0 0 0 0

# def update_matrix(matrix):
#     for i in matrix:
#         i.insert(0, 0)
#         i.append(0)
#     matrix.insert(0, [0] * len(matrix[0]))
#     matrix.append([0] * len(matrix[0]))
#     return matrix
#
# def is_not_isolate(lst, i, j):
#     pos = lst[i - 1][j - 1: j+1] + [lst[i][j-1]]+[lst[i][j+1]] + lst[i + 1][j - 1: j + 1]
#     if 1 in pos:
#         return True
#     return False
#
#
#
# def verify(args):
#     update_matrix(args)
#     for i in range(1, len(args) - 1):
#         for j in range(1, len(args) -1):
#             if args[i][j] == 1:
#                 if is_not_isolate(args,i,j):
#                     return False
#     return True
#
#
#
# d = [[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
# [print(*i) for i in d]
# print(verify(d))
#

# another way
# def is_isolate(*args):
#     return sum(*args) < 2
#
#
# def verify(lst):
#     size = len(lst)
#     return False not in [is_isolate(lst[i][j:j+2] + lst[i+1][j:j+2])
#                          for j in range(size - 1)
#                          for i in range(size - 1)]


# (Для закрепления предыдущего материала). Объявите функцию с именем str_min,
# которая сравнивает две переданные строки и возвращает минимальную из них (то есть, выполняется лексикографическое сравнение строк).
# Затем, используя функциональный подход к программированию (то есть, более сложные функции реализуются путем вызова более простых),
# реализовать еще две аналогичные функции:
#
# - с именем str_min3 для поиска минимальной строки из трех переданных строк;
# - с именем str_min4 для поиска минимальной строки из четырех переданных строк.
#
# Выполнять функции не нужно, только записать.


# def str_min(*args):
#     return min(args)
#
# def str_min3(*args):
#     return min(args)
#
# def str_min4(*args):
#     return min(args)
#
# print(str_min('dssfas','dsfsafsdfas'))
# print(str_min3('dssfas','dsfsafsdfas','ewdqwdqwadawda'))
# print(str_min4('dssfas','dsfsafsdfas','ewdqwdqwadawda','edasdasdasdadasd'))


# запаковка и распаковка
# d = -5, 5
# f = range(*d)
# print(f)    #range(-5, 5)
# print(*f)   #-5 -4 -3 -2 -1 0 1 2 3 4
#
# d1 = {0: 'damn', 1: 'very bad', 2: 'bad', 3: 'good', 4: 'excellent', 5: 'brilliant'}
# d2 = {6: 'fantastic', 7: 'awesome'}
# d3 = {**d1, **d2}
# print(d1, d2, d3, sep='\n')
# #{0: 'damn', 1: 'very bad', 2: 'bad', 3: 'good', 4: 'excellent', 5: 'brilliant', 6: 'fantastic', 7: 'awesome'}


# str --> list --> tuple
# lst = 'Москва Уфа Тверь Самара'.split()
# lst_c = (*lst,)
#
# print(lst_c)    #('Москва', 'Уфа', 'Тверь', 'Самара')


# Вводятся два целых значения a и b (a < b) в одну строчку через пробел.
# Необходимо сформировать список из целых чисел от a до b (включительно) с шагом изменения 1, используя функцию range,
# оператор [] и оператор распаковки *. Вывести полученный список на экран командой:
#
# print(*lst)
#
# Sample Input:
#
# 3 11
#
# Sample Output:
#
# 3 4 5 6 7 8 9 10 11

# a, b = list(map(int,input().split()))
# # a, b = list(map(int, '3 11'.split()))
# r = range(a, b+1)
# print(*r)


# *распаковка -запаковка
# st1 = list(map(float, '5.8 11.0 4.3'.split()))
# st2 = 'Уфа Омск Тверь Самара'.split()
# # st1 = list(map(int, input().split()))
# # st2 = input().split()
# st3 = [*st1, *st2]
# print(*st3)


# Имеется словарь, содержащий пункты меню:
#
# menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
#
# Дополнительно вводятся еще пункты меню в виде строк в формате:
#
# название_1=url_1
# ...
# название_N=url_N
#
# Необходимо эту введенную информацию преобразовать в словарь и добавить к словарю menu, используя
# оператор распаковки для словарей. На результирующий словарь должна вести переменная menu.
# Выводить словарь не нужно, только сформировать.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
#
# Города=about-cities
# Машины=read-of-cars
# Самолеты=airplanes
#
# Sample Output:
#
# Архив Главная Города Машины Новости Самолеты
# about-cities airplanes archive home news read-of-cars

# menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# lst_in = ['Города=about-cities', 'Машины=read-of-cars', 'Самолеты=airplanes']
#
# menu = {**menu, **dict([i.split("=") for i in lst_in])}
# print(menu)


# def recursive(value):
#
#     if value < 4:
#         recursive(value + 1)
#     print(value)

# recursive(1) #вывод 1 2 3 4 4 3 2 1 обусловлен тем,что сначала прошел поток запусков функции до значения 4
# а затем уже функции заканчивали действие начиная с конечной


# факториал рекурсия
# def fact(n):
#     if n <= 0:
#         return 1
#     else:
#         return n * fact(n - 1)
#
# print(fact(6))


# распечатка цифр от 1 до N через рекурсию
# def get_rec_N(n):
#     if n > 1:
#         get_rec_N(n - 1)
#     print(n)


# N = 8
# N = int(input())
# get_rec_N(N)


# summ of elements of list
# lst_in = [int(i) for i in '8 11 -5 4 3'.split()]
# def get_rec_sum(lst):
#     return sum(lst)
#
#
#
# get_rec_sum(lst_in)


# fibonnachi
# def fib_rec(N, f=[1, 1]):
#     if N > 2:
#         N -= 1
#         f.append(f[-1] + f[-2])
#         fib_rec(N, f)
#     return f
#
#
# N = 10
# print(fib_rec(N))  #1 1 2 3 5 8 13


# Вводится целое неотрицательное число n. Необходимо с помощью рекурсивной функции fact_rec вычислить факториал числа n.
# Напомню, что факториал числа, равен: n! = 1 * 2 * 3 *...* n. Функция должна возвращать вычисленное значение.
# Вызывать функцию не нужно, только объявить со следующей сигнатурой:
#
# def fact_rec(n): ...
# Sample Input:
# 6
# Sample Output:
# 720
import math

# n = 6

# def fact_rec(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * fact_rec(n - 1)
#
#
# print(fact_rec(n))


# С помощью рекурсивной функции get_line_list создать на его основе одномерный список из значений элементов списка d.
# Функция должна возвращать новый созданный одномерный список.  (Только возвращать, выводить на экран ничего не нужно.)
# Вызывать функцию не нужно, только объявить со следующей сигнатурой:
#
# def get_line_list(d,a=[]): ...
# где d - исходный список; a - новый формируемый.\


# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
# def get_line_list(d,a=[]):
#     for i in d:
#         if type(i) == list:
#             get_line_list(i)
#         else:
#             a.append(i)
#     return a
#
#
# get_line_list(d)


# Лягушка прыгает вперед и может скакнуть либо на одно деление, либо сразу на два. Наша задача определить количество
# вариантов маршрутов, которыми лягушка может достичь риски под номером N (натуральное число N вводится с клавиатуры).
# Решать задачу следует с применением рекурсивной функции. Назовем ее get_path. Алгоритм решения будет следующий.
# Рассмотрим, например, риску под номером 4. Очевидно, в нее лягушка может скакнуть либо с риски номер 2,
# либо с риски номер 3. Значит, общее число вариантов перемещений лягушки можно определить как:
# get_path(4) = get_path(3) + get_path(2)
# Аналогично будет справедливо и для любой риски N:
# get_path(N) = get_path(N-1) + get_path(N-2)
# А начальные условия задачи, следующие:
# get_path(1) = 1
# get_path(2) = 2
# Реализуйте такую рекурсивную функцию, которая должна возвращать количество вариантов перемещений лягушки для риски под номером N.
# Вызовите эту функцию для введенного числа N и отобразите результат на экране.
# Sample Input:
# 7
# Sample Output:
# 21

# def get_path(n):
#     if n in [1, 2]:
#         return n
#     else:
#         return get_path(n - 1) + get_path(n - 2)
#
#
#
# print(get_path(7))

# просто сортировка
# lst = [int(i) for i in input().split()]
# print(*sorted(lst))
#
# # сортировка слиянием с использованием рекурсивной функции
# l = [int(i) for i in input().split()]
#
#
# def merge_two_lists(a, b):
#     res = []
#     while a and b:
#         res += [a.pop(0) if a[0] < b[0] else b.pop(0)]
#     return res + a + b
#
#
# def merge_sort(l):
#     if len(l) == 1:
#         return l
#     mid = len(l) // 2
#     a, b = l[:mid], l[mid:]
#     return merge_two_lists(merge_sort(a), merge_sort(b))
#
#
# print(*merge_sort(l))

# lambda
# l = [1, 2, lambda: print('lambda'), 5, 6]
# # print(l)
# # print(l[2])
# print(l[2]())


# Объявите анонимную (лямбда) функцию с двумя параметрами для деления одного целого числа на другое.
# Если происходит деление на ноль, то функция должна возвращать значение None, иначе - результат деления.

# get_div = lambda a, b: a/b if b != 0 else None


#  модуль через лямбду
# x = float(input())
# print(x if x > -1 else -x)  #свое решение без лямбды

# another way
# x = float(input())
# n = lambda x: abs(x)
# print(n(x))

# Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "ra".
# То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае.
# Вызовите эту функцию для введенной строки s:
# s = input()
# Отобразите результат работы функции на экране.
# Sample Input:
# abrakadabra
# Sample Output:
# True


# s = input()
# k = lambda a,b: a+b == 'ra'
# q = 'NO'
# for i in range(1,len(s)):
#     if k(s[i-1], s[i]):
#         q = 'YES'
#         break
# print(q)

# another way
# print((lambda x: 'ra' in x)(input()))


# В программе задана функция filter_lst (см. программу ниже), которая отбирает элементы, переданного ей
# итерируемого объекта и возвращает сформированный кортеж значений.
# На вход программы поступает список целых чисел, записанных в одну строчку через пробел. Вызовите функцию filter_lst для формирования:
#
# - кортежа из всех значений входного списка (передается в параметр it);
# - кортежа только из отрицательных чисел;
# - кортежа только из неотрицательных чисел (то есть, включая и 0);
# - кортежа из чисел в диапазоне [3; 5]
#
# Каждый результат работы функции следует отображать с новой строки командой:
#
# print(*lst)
#
# где lst - список на возвращенный функцией filter_lst. Для отбора нужных значений формальному параметру key следует
# передавать соответствующие определения анонимной функции.
# Sample Input:
#
# 5 4 -3 4 5 -24 -6 9 0
#
# Sample Output:
#
# 5 4 -3 4 5 -24 -6 9 0
# -3 -24 -6
# 5 4 4 5 9 0
# 5 4 4 5


# def filter_lst(it, key=None):
#     if key is None:
#         return tuple(it)
#
#     res = ()
#     for x in it:
#         if key(x):
#             res += (x,)
#
#     return res
#
# # здесь продолжайте программу
# s = [int(i) for i in '5 4 -3 4 5 -24 -6 9 0'.split()]
# s = [int(i) for i in input().split()]
#
# print(*filter_lst(s))
# print(*filter_lst(s, key=lambda x: x < 0))
# print(*filter_lst(s, key=lambda x: x >= 0))
# print(*filter_lst(s, key=lambda x: x in range(3,6)))


# Замыкание в Python
# def say_name(name):
#     def say_goobye():
#         print(f'Don`t say me goodbye, {name}!')
#     return say_goobye
#
# f1 = say_name('Alex')
# f1()
# f2 = say_name('Python')
# f2()


# def counter(start= 0):
#     def step():
#         nonlocal start
#         start += 1
#         return start
#     return step
#
# c1 = counter(10)
# c2 = counter()
# print(c1(), c2())
# print(c1(), c2())
# print(c1(), c2())


#
# def strip_string(string_chars = ' '):
#     def do_strip(string):
#         return string.strip(string_chars)
#     return do_strip
# s1 = strip_string()
# s2 = strip_string(' !?/,.;=')
#
# print(s1(' python '))
# print(s2(' python   !?. '))


# Используя замыкания функций, определите вложенную функцию, которая бы увеличивала значение переданного параметра на 5
# и возвращала бы вычисленный результат. При этом внешняя функция должна иметь следующую сигнатуру:
#
# def counter_add(): ...
# Вызовите функцию counter_add и результат ее работы присвойте переменной с именем cnt.
# Вызовите внутреннюю функцию через переменную cnt со значением k, введенным с клавиатуры:
# k = int(input())
# Выведите результат на экран.
# Sample Input:
# 7
# Sample Output:
# 12

# def counter_add():
#     def upper_count(count):
#         return count + 5
#     return upper_count
#
# k = int(input())
# cnt = counter_add()
# print(cnt(k))


# Используя замыкания функций, объявите внутреннюю функцию, которая увеличивает значение своего аргумента на некоторую величину
# n - параметр внешней функции с сигнатурой:
# def counter_add(n): ...
# Вызовите внешнюю функцию counter_add со значением аргумента 2 и результат присвойте переменной cnt.
# Вызовите внутреннюю функцию через переменную cnt со значением k, введенным с клавиатуры:
# k = int(input())
# Выведите результат на экран.
# Sample Input:
# 5
# Sample Output:
# 7


# def counter_add(n):
#     def counter_in(k):
#         return k + n
#     return counter_in
#
# k = int(input())
#
# cnt = counter_add(2)
#
# print(cnt(k))


# Используя замыкания функций, объявите внутреннюю функцию, которая заключает в тег h1 строку s
# (s - строка, параметр внутренней функции). Далее, на вход программы поступает строка и ее нужно поместить в тег h1
# с помощью реализованного замыкания. Результат выведите на экран.
# P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>
# Sample Input:
# Balakirev
# Sample Output:
# <h1>Balakirev</h1>

# def add_tag(tag_str):
#     def tag(s):
#         return f'<{tag_str}>{s}</{tag_str}>'
#     return tag
#
# s1 = add_tag('h1')
# print(s1(input()))

# Используя замыкания функций, объявите внутреннюю функцию, которая заключает строку s (s - строка, параметр
# внутренней функции) в произвольный тег, содержащийся в переменной tag - параметре внешней функции.
# Далее, на вход программы поступают две строки: первая с тегом, вторая с некоторым содержимым.
# Вторую строку нужно поместить в тег из первой строки с помощью реализованного замыкания. Результат выведите на экран.
# P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>
# Sample Input:
# div
# Сергей Балакирев
# Sample Output:
#
# <div>Сергей Балакирев</div>

# def add_tag(tag_str):
#     def tag(s):
#         return f'<{tag_str}>{s}</{tag_str}>'
#     return tag
#
# s1 = add_tag(input())
# print(s1(input()))


# Используя замыкания функций, объявите внутреннюю функцию, которая преобразует строку из списка целых чисел,
# записанных через пробел, либо в список, либо в кортеж. Тип коллекции определяется параметром tp внешней функции.
# Если tp = 'list', то используется список, иначе (при другом значении) - кортеж.
# Далее, на вход программы поступают две строки: первая - это значение для параметра tp; вторая - список целых чисел,
# записанных через пробел. С помощью реализованного замыкания преобразовать эти данные в соответствующую коллекцию.
# Результат вывести на экран командой (lst - ссылка на коллекцию):
# print(lst)
# Sample Input:
# list
# -5 6 8 11 0 111 -456 3
# Sample Output:
# [-5, 6, 8, 11, 0, 111, -456, 3]

# def add_to_collection(tp):
#
#     def add_to_list(lst):
#         return list(lst)
#
#     def add_to_tuple(lst):
#         return tuple(lst)
#
#     if tp == 'list':
#         return add_to_list
#     else:
#         return add_to_tuple
#
#
# type_of_collection = input()
# lst = [int(i) for i in input().split()]
# # type_of_collection = 'list'
# # lst = [int(i) for i in '-5 6 8 11 0 111 -456 3'.split()]
#
# closure = add_to_collection(type_of_collection)
# print(closure(lst))


# Подвиг 1. Объявите функцию с именем get_sq, которая вычисляет площадь прямоугольника по двум параметрам: width и height
# - ширина и высота прямоугольника. И возвращает результат (сама ничего на экран не выводит). То есть, функция имеет сигнатуру:
# def get_sq(width, height): ...
# Определите декоратор func_show для этой функции, который отображает результат на экране в виде строки (без кавычек):
# "Площадь прямоугольника: <значение>"
# Вызывать функцию и декоратор не нужно, только объявить. Применять декоратор к функции также не нужно.
# Sample Input:
# 8 11
# Sample Output:
# Площадь прямоугольника: 88

# def func_show(func):
#     def wrapper(*args, **kwargs):
#         return print(f'Площадь прямоугольника: {func(*args, **kwargs)}')
#     return wrapper
#
#
# def get_sq(width, height):
#     return width * height


# На вход программы поступает строка с названиями пунктов меню, записанные в одну строчку через пробел. Необходимо
# задать функцию с именем get_menu, которая преобразует эту строку в список из слов и возвращает этот список. Сигнатура функции следующая:
# def get_menu(s): ...
# Определите декоратор для этой функции с именем show_menu, который отображает список на экран в формате:
# 1. Пункт_1
# 2. Пункт_1
# ...
# N. Пункт_N
# Примените декоратор show_menu к функции get_menu, используя оператор @. Более ничего в программе делать не нужно. Сами функции не вызывать.
# Sample Input:
# Главная Добавить Удалить Выйти
# Sample Output:
# 1. Главная
# 2. Добавить
# 3. Удалить
# 4. Выйти

# def show_menu(func):
#     def wrapper(*args,**kwargs):
#         s = func(*args, **kwargs)
#         s1 = [f'{i + 1}. {s[i]}' for i in range(len(s))]
#         s2 = print(*s1, sep='\n')
#         return s2
#     return wrapper
#
# @show_menu
# def get_menu(s):
#     return s.split()
#
# get_menu(input())
# get_menu('Главная Добавить Удалить Выйти')


# На вход программы поступает строка из целых чисел, записанных через пробел. Напишите функцию get_list,
# которая преобразовывает эту строку в список из целых чисел и возвращает его. Определите декоратор для этой функции,
# который сортирует список чисел по возрастанию. Результат сортировки должен возвращаться при вызове декоратора.
# Вызовите декорированную функцию get_list и отобразите полученный отсортированный список lst командой:
# print(*lst)
# Sample Input:
# 8 11 -5 4 3 10
# Sample Output:
# -5 3 4 8 10 11

# def sort_list(func):
#     def wrapper(*args, **kwargs):
#         return sorted(func(*args, **kwargs))
#     return wrapper
#
# @sort_list
# def get_list(s):
#     return [int(i) for i in s.split()]
#
# lst = get_list('8 11 -5 4 3 10')
# # lst = get_list(input())
# print(lst)


# Вводятся две строки из слов (слова записаны через пробел). Объявите функцию, которая преобразовывает эти две строки в
# два списка слов и возвращает эти списки.
# Определите декоратор для этой функции, который из двух списков формирует словарь, в котором ключами являются слова из
# первого списка, а значениями - соответствующие элементы из второго списка. Полученный словарь должен возвращаться при вызове декоратора.
# Примените декоратор к первой функции и вызовите ее для введенных строк. Результат (словарь d) отобразите на экране командой:
# print(*sorted(d.items()))
# Sample Input:
# house river tree car
# дом река дерево машина
# Sample Output:
# ('car', 'машина') ('house', 'дом') ('river', 'река') ('tree', 'дерево')

# def list_to_dict(func):
#     def wrapper(*args):
#         lst1 = func(args[0])
#         lst2 = func(args[1])
#         global d
#         d = dict(zip(lst1, lst2))
#         return d
#     return wrapper
#
# @list_to_dict
# def str_to_list(st1):
#     return st1.split()
#
#
# str_to_list('house river tree car', 'дом река дерево машина')
# # str_to_list(input(), input())
# print(*sorted(d.items()))


# Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу,
# используя следующий словарь для замены русских букв на соответствующее латинское написание:
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# Функция должна возвращать преобразованную строку. Замены делать без учета регистра (исходную строку
# перевести в нижний регистр - малые буквы). Все небуквенные символы ": ;.,_" превращать в символ '-' (дефиса).
# Определите декоратор для этой функции, который несколько подряд идущих дефисов, превращает в один дефис.
# Полученная строка должна возвращаться при вызове декоратора. (Сам декоратор на экран ничего выводить не должен).
# Примените декоратор к первой функции и вызовите ее для введенной строки s на кириллице:
# s = input()
# Результат работы декорированной функции отобразите на экране.
# Sample Input:
# Python - это круто!
# Sample Output:
# python-eto-kruto!


# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# def no_more(func):
#     def wrapper(s):
#         k = func(s)
#         for i in k:
#             if i in ': ;.,_':
#                 k = k.replace(i, '-')
#         while '--' in k:
#             k = k.replace('--','-')
#         return k
#     return wrapper
#
# @no_more
# def cyr_to_lat(s):
#     s = s.lower()
#     for i in s:
#         if i in t:
#             s = s.replace(i, t[i])
#     return s
#
# # print(cyr_to_lat('Python - это круто!'))
# cyr_to_lat(input())


# import math
# from functools import wraps
#
# # декоратор с параметрами
# def df_decorator(dx=0.0001):
#     def func_decorator(func):
#         @wraps(func)
#         def wrapper(x, *args, **kwargs):
#             res = func(x + dx, *args,**kwargs) - func(x,*args, **kwargs)/dx
#             return res
#         # wrapper.__name__= func.__name__
#         # wrapper.__doc__ = func.__doc__        #тк используем декоратор из functools, то эти строчки не нужны
#         return wrapper
#     return func_decorator
#
#
# @df_decorator(dx=0.01)
# def sin_df(x):
#     """Функция для вычисления производной синуса"""
#     return math.sin(x)
#
# df = math.sin(math.pi/3)
# print(df)


#  Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает эту строку в список чисел и возвращает их сумму.
# Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
# Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для введенной строки s:
# s = input()
# Результат отобразите на экране.
# Sample Input:
# 5 6 3 6 -4 6 -1
# Sample Output:
# 26


# def start_decorator(start=5):
#     def decor_func(func):
#         def wrapper(x, *args, **kwargs):
#             res = start + func(x, *args, **kwargs)
#             return res
#
#         return wrapper
#
#     return decor_func
#
#
# @start_decorator(start=5)
# def sum_lst(s):
#     return sum([int(i) for i in s.split()])
#
#
# lst = input()
# print(sum_lst(lst))


# Объявите функцию, которая возвращает переданную ей строку в нижнем регистре (с малыми буквами).
# Определите декоратор для этой функции, который имеет один параметр tag, определяющий строку с названием тега и
# начальным значением "h1". Этот декоратор должен заключать возвращенную функцией строку в тег tag и возвращать результат.
# Пример заключения строки "python" в тег h1: <h1>python</h1>
# Примените декоратор со значением tag="div" к функции и вызовите декорированную функцию для введенной строки s:
# s = input()
# Результат отобразите на экране.
# Sample Input:
# Декораторы - это классно!
# Sample Output:
# <div>декораторы - это классно!</div>

# def decorator_tag(tag='h1'):
#     def dec_func(func):
#         def wrapper(st, *args,**kwargs):
#             return f'<{tag}>{func(st)}</{tag}>'
#         return wrapper
#     return dec_func
#
#
# @decorator_tag(tag='div')
# def minimize_st(st):
#     return st.lower()
# s = input()
# print(minimize_st(s))


# Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу, используя следующий словарь
# для замены русских букв на соответствующее латинское написание:
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# Функция должна возвращать преобразованную строку. Замены делать без учета регистра (исходную строку перевести в нижний
# регистр - малые буквы).
# Определите декоратор с параметром chars и начальным значением " !?", который данные символы преобразует в символ "-" и,
# кроме того, все подряд идущие дефисы (например, "--" или "---") приводит к одному дефису. Полученный результат должен
# возвращаться в виде строки.
# Примените декоратор с аргументом chars="?!:;,. " к функции и вызовите декорированную функцию для введенной строки s:
# s = input()
# Результат отобразите на экране.
# Sample Input:
# Декораторы - это круто!
# Sample Output:
# dekoratory-eto-kruto-

# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# def decorator_del_symbols(chars="?!:;,. "):
#     def decor_func(func):
#         def wrapper(s, *args, **kwargs):
#             k = ''
#             for i in func(s):
#                 k += t[i] if i in t else i
#             for symbol in k:
#                 k = k.replace(symbol, '-') if symbol in chars else k
#             while '--' in k:
#                 k = k.replace('--','-')
#             return k
#         return wrapper
#     return decor_func
#
# @decorator_del_symbols(chars="?!:;,. ")
# def cyr_to_lat(s):
#     return s.lower()
#
# print(cyr_to_lat(input()))


# Объявите функцию с именем get_list и следующим описанием в теле функции:
# '''Функция для формирования списка целых значений'''
# Сама функция должна формировать и возвращать список целых чисел, который поступает на ее вход в виде строки из целых чисел,
# записанных через пробел.
# Определите декоратор, который выполняет суммирование значений из списка этой функции и возвращает результат.
# Внутри декоратора декорируйте переданную функцию get_list с помощью команды @wraps (не забудьте сделать импорт:
# from functools import wraps). Такое декорирование необходимо, чтобы исходная функция get_list сохраняла свои локальные свойства:
# __name__ и __doc__.
# Примените декоратор к функции get_list, но не вызывайте ее.

# from functools import wraps
#
# def decorator_sum(func):
#     @wraps(func)
#     def wrapper(lst, *args, **kwargs):
#         return sum(func(lst))
#     return wrapper
#
# @decorator_sum
# def get_list(s):
#     '''Функция для формирования списка целых значений'''
#     return [int(i) for i in s.split()]
#
# print(get_list(input()))


# import modules
# cmd + left mouse --> going to the module text
# from pprint import pprint
# import math
# import time
#
# pprint(locals())


# from random import seed
# from random import random as rnd
#
# seed(10)
# print(round(rnd(), 2))


# pip freeze > requirements.txt   #создает текстовый файл со списком установленных модулей и номерами их версий


#  В пакете panda_pack имеются два модуля: panda1.py и panda2.py. В файле __init__.py прописаны следующие команды:
# from . import panda2
# from . import panda1
# __all__ = ['panda1']
# Как при этом будут работать импорты пакетов, если в основной программе импорт пакета выполняется с помощью команды:
# from panda_pack import *

# ANSWER: импортируется только модуль panda1


# try-except-finally

# try:
#     with open('my_file', encoding='UTF-8') as file:
#         s = file.readlines()
#         print(s)
# аналог этого ниже
# file = open('my_file', encoding='UTF-8')
# try:
#     s = file.readlines()
#     int(s)  #сработает except ошибка при работе с файлом
#     print(s)
# finally:
#     file.close()    #выполняется в любом случае
# except FileNotFoundError:
#     print('Файл не найден') #сработает если файл не найден
# except:
#     print('Ошибка при работе с файлом')


# file = open('out.txt', 'w')
# file.write('Hello World!')
# file.close()


# try:
#     with open('out.txt','w') as file:
#         file.write('Hello World!_1\n')
#         file.write('Hello World!_2\n')
#         file.write('Hello World!_3\n')
#
# except:
#     print('Ошибка при работе с файлом')


# try:
#     with open('out.txt','w') as file:
#         file.seek(0)    #в режиме а+ позиция считывания становится в конце,поэтому перемещаем курсор на 0 позицию
#         file.write('hello4')    #все равно запишется в конец
#         file.writelines(['hello5\n','hello6\n'])
#         s = file.readlines()
#         print(s)
# except:
#     print('Ошибка при работе с файлом')

# r = (i for i in range(0,5))
# try:
#     print(next(r))
# except StopIteration:
#     print('stop')

# генераторы не хранят значения как списки в памяти , а генерируют по мере необходимости
# lst = list(range(100000000000000000))   #MemoryError
# lst = (i for i in range(100000000000000000))
# for i in lst:
#     if i > 50:
#         break
#     print(i, end=' ')


# Подвиг 3. На вход программы поступают два целых числа a и b (a < b), записанные в одну строчку через пробел.
# Определите генератор, который бы выдавал модули целых чисел из диапазона [a; b]. В цикле выведите первые пять значений этого генератора.
# Каждое значение с новой строки. (Гарантируется, что пять значений имеются).
# Sample Input:
# -3 3
# Sample Output:
# 3
# 2
# 1
# 0
# 1
# a, b = [3,30]
# gen = (abs(i) for i in range(a,b))
# for i in range(5):
#     print(next(gen))


# Вводится целое положительное число a. Необходимо определить генератор, который бы возвращал модули чисел в диапазоне
# [-a; a], а затем еще один, который бы вычислял кубы чисел (возведение в степень 3), возвращаемых первым генератором.
# Вывести в одну строчку через пробел первые четыре значения. (Полагается, что генератор выдает, как минимум четыре значения).
# Sample Input:
# 3
# Sample Output:
# 27 8 1 0
# a = 3
# gen_1 = (abs(i) for i in range(-a,a))
# gen_2 = (i ** 3 for i in gen_1)
# print(*list(gen_2)[0:4])


# Подвиг 7. Используя символы малых букв латинского алфавита (строка ascii_lowercase):
# from string import ascii_lowercase
# запишите генератор, который бы возвращал все сочетания из двух букв латинского алфавита.
# Выведите первые 50 сочетаний на экран в строку через пробел.
# Например, первые семь начальных сочетаний имеют вид:
# aa ab ac ad ae af ag

# from string import ascii_lowercase
#
# alf = (i + j for i in ascii_lowercase for j in ascii_lowercase)
#
# print(*list(alf)[0:50])     # else [print(next(gen), end= ' ') for _ in range(50)]


# Имеется список из названий городов:
# cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
# Необходимо записать генератор, который бы используя этот список, выдавал 1 000 000 наименований городов по циклу.
# То есть, дойдя до конца списка, возвращался в начало и повторял перебор. И так, для выдачи миллиона названий.
# Вывести на экран первые 20 наименований городов с помощью генератора в одну строчку через пробел.

# cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
# gen=(j for i in range(1000000) for j in cities)
# print(*list(gen)[0:20])


# Подвиг 9. Имеется график функции f(x) = 0.5x^2 - 2. Необходимо записать генератор, который бы выдавал значения этой функции
# для аргумента x в диапазоне [a; b] с шагом 0.01. Величины a, b вводятся с клавиатуры в одну строчку через пробел как целые
# числа (a< b). Вывести на экран первые 20 значений функции с точностью до сотых, взятых из генератора.
# P.S. Значения функции вычислять командой:
# f(x) = 0.5 * pow(x, 2) - 2.0
# Sample Input:
# 0 10
# Sample Output:
# -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -1.99 -1.99 -1.99 -1.99 -1.99 -1.99 -1.99 -1.98 -1.98
# from numpy import arange
# # a, b = 0, 10
# a, b = map(int, input().split())
# func = (round(0.5 * pow(x, 2) - 2.0, 2) for x in arange(a, b, 0.01))
# print(*list(func)[:20])
# print(range(0.0, 1.0, 0.1))


# yield превращает любую функцию в генератор

# def gen():
#     for x in [1, 2, 3, 4, 5]:
#         yield x
#
# a = gen()
# for i in a:
#     print(i)


# def gen_2():
#     for i in range(1, 10):
#         a = range(i, 11)
#         yield sum(a)/len(a)
#
# f = gen_2()
# print(*list(f))


# def find_word(f, word):
#     g_index = 0
#     for line in f:
#         indx = 0
#         while indx != -1:
#             indx = line.find(word,indx)
#             if indx > -1:
#                 yield g_index + indx
#                 indx += 1
#         g_index += len(line)
#
# try:
#     with open('lesson_54.txt', encoding='UTF-8') as file:
#         a = find_word(file, 'генератор')
#         print(list(a))
# except FileNotFoundError:
#     print('The is no file with such name')
# except:
#     print('Houston, we have some problems')


# Подвиг 1. Вводится натуральное число N. Необходимо определить функцию-генератор с именем get_sum,
# которая бы возвращала текущую сумму чисел последовательности длины N в диапазоне целых чисел [1; N]. Например:
# - для первого числа 1 сумма равна 1;
# - для второго числа 2 сумма равна 1+2 = 3
# ....
# - для N-го числа сумма равна 1+2+...+(N-1)+N
# Реализовать функцию-генератор get_sum без использования коллекций. Вызывать ее не нужно, только определить.
# Sample Input:
# 5
# Sample Output:
# 1 3 6 10 15


# def get_sum(N):
#     summa = 0
#     for i in range(1, N + 1):
#         summa += i
#         yield summa
# N = int(input())
# # print(*list(get_sum(int(input()))))
# print(*tuple(get_sum(N)))


# Подвиг 2. Мы с вами в заданиях несколько раз генерировали последовательность чисел Фибоначчи, которая строится по правилу:
# каждое последующее число равно сумме двух предыдущих. Для разнообразия давайте будем генерировать каждое последующее
# как сумму трех предыдущих чисел. При этом первые три числа равны 1 и имеем такую последовательность:
# 1, 1, 1, 3, 5, 9, 17, 31, 57, ...
# Не знаю, есть ли у нее название, поэтому, в рамках уроков, я скромно назову ее последовательностью Балакирева.
# Итак, на вход программы поступает натуральное число N (N > 5) и необходимо определить функцию-генератор, которая бы
# возвращала N первых чисел последовательности Балакирева (включая первые три единицы).
# Реализуйте эту функцию без использования коллекций (списков, кортежей, словарей и т.п.). Вызовите ее N раз для получения
# N чисел и выведите полученные числа на экран в одну строчку через пробел.
# Sample Input:
# 7
# Sample Output:
# 1 1 1 3 5 9 17

# def balakirev(N):
#     s = (1,1,1)
#     while len(s) < N:
#         s += (sum(s[-3:]),)
#     return s
#
# print(*balakirev(7))

# another way
# N = int(input())
#
#
# def get_sum(N):
#     a = b = c = 1
#     for _ in range(N):
#         yield a
#         a, b, c = b, c, a + b + c
#
#
# print(*get_sum(N))


# Подвиг 3. Вводится натуральное число N (N > 8). Необходимо определить функцию-генератор, которая бы выдавала пароль длиной
# N символов из случайных букв, цифр и некоторых других знаков. Для получения последовательности допустимых символов для
# генерации паролей в программе импортированы две строки: ascii_lowercase, ascii_uppercase (см. листинг ниже),
# на основе которых формируется общий список:
# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
# Функция-генератор должна при каждом вызове возвращать новый пароль из случайно выбранных символов chars длиной N и
# делать это бесконечно, то есть, вызывать ее можно бесконечное число раз. Сгенерировать случайный индекс indx в диапазоне
# [a; b] для символа можно с помощью функции randint модуля random:
# import random
# random.seed(1)
# indx = random.randint(a, b)
# Сгенерируйте с помощью этой функции первые пять паролей и выведите их в столбик (каждый с новой строки).
# Sample Input:
# 10
# Sample Output:
# riGp?58WAm
# !dX3a5IDnO
# dcdbWB2d*C
# 4?DSDC6Lc1
# mxLpQ@2@yM

# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
#
# import random
#
# random.seed(1)
# indx = random.randint(0, len(chars))
# print(indx)


# Подвиг 3. Вводится таблица целых чисел. Используя функцию map и генератор списков, преобразуйте список строк lst_in
# (см. листинг) в двумерный список с именем lst2D, содержащий целые числа.
# Выводить на экран ничего не нужно, только сформировать список lst2D на основе введенных данных.
# Sample Input:
# 8 11 -5
# 3 4 10
# -1 -2 3
# 4 5 6
# Sample Output:
# True
#
# lst_in = ['8 11 -5', '3 4 10', '-1 -2 3', '-4 5 6']
# lst2D = list(map(lambda x: list(map(int,x.split())), lst_in))
# print(lst2D)


# Подвиг 4. На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
# Выводить на экран ничего не нужно, только преобразовать строку в кортеж с именем tp.
# Sample Input:
# house=дом car=машина men=человек tree=дерево
# Sample Output:
# True

# ввод строки (переменную s не менять)
# s = input()
# s = 'house=дом car=машина men=человек tree=дерево'
# s_lst = s.split()
#
# tp = tuple(map(lambda x: tuple(x.split('=')), s_lst))
# print(tp)


# Подвиг 5. (Для учебных целей). Вводится строка. Необходимо в ней заменить кириллические символы на соответствующие
# латинские обозначения (без учета регистра букв), а все остальные символы - на символ дефиса (-).
# Для этого в программе определен словарь (см. листинг). Используя его, запишите функцию map,
# которая бы выдавала преобразованные фрагменты для входной строки. На основе этой функции сформируйте строку,
# состоящую из преобразованных фрагментов (фрагменты в строке должны идти друг за другом без пробелов). Отобразите результат на экране.
# Sample Input:
# Привет Питон
# Sample Output:
# privet-piton

# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

# здесь продолжайте программу
# s = '-'.join(list(map(lambda x: ''.join(list(map(lambda y: t[y.lower()], list(x)))), input().split())))
# print(s)


# another way
# print(*map(lambda x: t.get(x, '-'), input().lower()), sep='')


# Подвиг 6. Вводятся названия городов в одну строчку через пробел. Необходимо определить функцию map,
# которая бы возвращала названия городов только длиной более 5 символов. Вместо остальных названий - строку с дефисом ("-").
# Сформировать список из полученных значений и отобразить его на экране в одну строчку через пробел.
# Sample Input:
# Москва Уфа Вологда Тула Владивосток Хабаровск
# Sample Output:
# Москва - Вологда - Владивосток Хабаровск

# st = 'Москва Уфа Вологда Тула Владивосток Хабаровск'
# lst = list(map(lambda x: x if len(x) > 5 else '-', st.split()))
# lst = list(map(lambda x: x if len(x) > 5 else '-', input().split()))
# print(lst)


# Подвиг 2. Вводится список предметов в виде списка:
# название_1: вес_1
# ...
# название_N: вес_N
# С помощью функции map, необходимо сначала преобразовать этот список строк в кортеж, элементами которого также являются кортежи:
# (('название_1', 'вес_1'), ..., ('название_N', 'вес_N'))
# А, затем, отфильтровать (исключить) все предметы с весом менее 500, используя функцию filter. Вывести на экран список оставшихся предметов (только их названия) в одну строчку через пробел.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# зонт=1000
# палатка=10000
# спички=22
# котелок=543
# Sample Output:
# зонт палатка котелок


# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список lst_in)
# #['зонт=1000', 'палатка=10000', 'спички=22', 'котелок=543']
#
# m = filter(lambda x: int(x[1]) > 500, map(lambda x: tuple(x.split('=')), lst_in))
# for i in m:
#     print(i[0], end= ' ')


# Подвиг 3. Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности оставшихся
# чисел в одну строчку через пробел.
# Sample Input:
# 8 11 0 -23 140 1
# Sample Output:
# 11 -23

# s = '8 11 0 -23 140 1'
# s = input()
# st = filter(lambda x: -100 < x < -9  or 9<x<100,map(int, s.split()))
# print(*st)


# Подвиг 4. Саша и Галя коллекционируют монетки. Каждый из них решил записать номиналы монеток из своей коллекции.
# Получилось два списка. Эти списки поступают на вход программы в виде двух строк из целых чисел, записанных через пробел.
# Необходимо выделить значения, присутствующие в обоих списках и оставить среди них только четные.
# Результат вывести на экран в виде строки полученных чисел в порядке их возрастания через пробел.
# При реализации программы используйте функцию filter и кое-что еще (для упрощения программы), подумайте что.
# Sample Input:
# 1 5 2 7 10 25 50 100
# 5 2 3 7 10 25 55
# Sample Output:
# 2 10
# s1 = '1 5 2 7 10 25 50 100'
# s2 = '5 2 3 7 10 25 55'
# s1 = input()
# s2 = input()
# set_cross = filter(lambda x: x%2 ==0, set(map(int, s1.split())) & set(map(int, s2.split())))
# print(*sorted(set_cross))


# Подвиг 5. Вводится список email-адресов в одну строчку через пробел. Среди них нужно оставить только корректно записанные адреса.
# Будем полагать, что к таким относятся те, что используют латинские буквы, цифры и символ подчеркивания.
# А также в адресе должен быть символ "@", а после него символ точки "." (между ними, конечно же, могут быть и другие символы).
# Результат отобразить в виде строки email-адресов, записанных через пробел.
# Sample Input:
# abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com
# Sample Output:
# abc@it.ru biba123@list.ru sc_lib@list.ru

# from string import ascii_lowercase
#
# def email_true(email):
#     lst = list(email)
#     another_digits = '0123456789_-'
#     if '@' in lst and '.' in lst:
#         if lst.index('@') < lst.index('.'):
#             del lst[lst.index('@')]
#             del lst[lst.index('.')]
#         else:
#             return False
#     else:
#         return False
#     if not all(map(lambda x: x in ascii_lowercase or x in another_digits, lst)):
#         return False
#     return True
#
#
#
# s = 'abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com'
# # s = input()
# l = filter(lambda x: email_true(x), s.split())
# print(*l)


# another way
# from string import ascii_letters, digits
# chars = ascii_letters + digits + "_@."
#
# lst = input().split()
#
# fil = filter(lambda adress:
#              '@' in adress and
#              '.' in adress and
#              all(i in chars for i in adress) and
#              adress.find('@') < adress.find('.'), lst)
#
# print(*fil)


# Подвиг 1. Вводятся два списка целых чисел. Необходимо попарно перебрать их элементы и перемножить между собой.
# При реализации программы используйте функции zip и map. Выведите на экран первые три значения, используя функцию next.
# Значения выводятся в строчку через пробел. (Полагается, что три выходных значения всегда будут присутствовать).
# Sample Input:
# -7 8 11 -1 3
# 1 2 3 4 5 6 7 8 9 10
# Sample Output:
# -7 16 33

# s1, s2 = '-7 8 11 -1 3', '1 2 3 4 5 6 7 8 9 10'
# s1, s2 = input(), input()
# z = map(lambda x: x[0] * x[1],zip(map(int, s1.split()), map(int, s2.split())))
# for i in range(3):
#     print(next(z), end = ' ')


# Подвиг 2. Вводится неравномерная таблица целых чисел. С помощью функции zip выровнить эту таблицу,
# приведя ее к прямоугольному виду, отбросив выходящие элементы. Вывести результат на экран в виде такой же таблицы чисел.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# 1 2 3 4 5 6
# 3 4 5 6
# 7 8 9
# 9 7 5 3 2
# Sample Output:
# 1 2 3
# 3 4 5
# 7 8 9
# 9 7 5

# lst_in = ['1 2 3 4 5 6', '3 4 5 6', '7 8 9', '9 7 5 3 2']
# lst_sec = list(map(lambda x: list(map(int, x.split())), lst_in))
# lst_end = zip(*zip(*lst_sec))
# for i in lst_end:
#     print(*i)


# Подвиг 3. Вводится таблица целых чисел. Необходимо сначала эту таблицу представить двумерным списком чисел, а затем,
# с помощью функции zip выполнить транспонирование этой таблицы (то есть, строки заменить на соответствующие столбцы).
# Результат вывести на экран в виде таблицы чисел (числа в строках следуют через пробел).
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# 1 2 3 4
# 5 6 7 8
# 9 8 7 6
# Sample Output:
# 1 5 9
# 2 6 8
# 3 7 7
# 4 8 6


# import sys
# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# здесь продолжайте программу (используйте список строк lst_in)

# lst_in = ['1 2 3 4', '5 6 7 8', '9 8 7 6']
# lst_sec = map(lambda x: map(int, x.split()), lst_in)
# lst_end = zip(*lst_sec)
# [print(*i) for i in lst_end]


# Подвиг 4. Вводится строка из слов, записанных через пробел. Необходимо на их основе составить прямоугольную таблицу из
# трех столбцов и N строк (число строк столько, сколько получится). Лишнее (выходящее) слово - отбросить.
# Реализовать эту программу с использованием функции zip. Результат отобразить на экране в виде прямоугольной таблицы из слов,
# записанных через пробел (в каждой строчке).
# Sample Input:
# Москва Уфа Тула Самара Омск Воронеж Владивосток Лондон Калининград Севастополь
# Sample Output:
# Москва Уфа Тула
# Самара Омск Воронеж
# Владивосток Лондон Калининград
# l = 'Москва Уфа Тула Самара Омск Воронеж Владивосток Лондон Калининград Севастополь'
# # lst = [[l.split()[t] for t in range(i, i+3)] for i in range(0,len(l.split()),3) if len(l.split()[i]) == 3]
# # lst1 = l.split()
# lst1 = input().split()
# z = zip(*[iter(lst1)]*3)
# [print(*l) for l in z]


# Подвиг 5. Вводится строка. Требуется, используя введенную строку, сформировать N=10 пар кортежей в формате:
# (символ, порядковый индекс)
# Первый индекс имеет значение 0. Строка может быть короче 10 символов, а может быть и длиннее.
# То есть, число пар может быть 10 и менее. Используя функцию zip сформируйте указанные кортежи и сохраните в список с именем lst.
# Программа ничего не должна отображать на экране, только формировать список из кортежей.
# Sample Input:
# Python дай мне силы пройти этот курс до конца!
# Sample Output:
# True

# s = 'Python дай мне силы пройти этот курс до конца!'
# l = range(10)
# f = list(zip(s,l))
# print(f)
# [('P', 0) ('y', 1) ('t', 2) ('h', 3) ('o', 4) ('n', 5) (' ', 6) ('д', 7) ('а', 8) ('й', 9)]


# Подвиг 2. На вход поступает список целых чисел, записанных в одну строчку через пробел.
# Преобразуйте сначала эту строку в список из целых чисел, а затем список в кортеж из целых чисел.
# То есть, в программе будет две разные коллекции: список и кортеж. Отсортируйте по возрастанию значений эти коллекции
# методом sort, если это возможно, а иначе - примените функцию sorted.
# На экран ничего выводить не нужно, только сформировать две отсортированные коллекции: lst (список) - результат
# сортировки списка; tp_lst (кортеж) - результат сортировки кортежа.
# P. S. На результаты сортировок обязательно должны ссылаться переменные с именами lst и tp_lst!
# Sample Input:
# -2 -1 8 11 4 5
# Sample Output:
# True


# s = input()
# s = '-2 -1 8 11 4 5'
# lst = [int(i) for i in s.split()]
# tp_lst = tuple(sorted(lst))
# lst.sort()
#
# print(lst)
# print(tp_lst)


#

# Подвиг 3. На вход функции с именем get_sort поступает словарь, например, такой:
# d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
# Необходимо отсортировать словарь d по убыванию ключей (лексикографическая сортировка строк) и возвратить список из
# соответствующих значений ключей словаря. Например, для указанного словаря d, результатом должен быть список:
# ['дерево', 'лошадь', 'собака', 'кот', 'книга']
# Сигнатура функции get_sort должна быть следующей:
# def get_sort(d): ...
# В программе только определить функцию, вызывать ее не нужно и что-либо выводить на экран тоже не нужно.
# P. S. Подсказка: список в функции get_sort лучше всего формировать с помощью генератора списков.
# Sample Input:
# Sample Output:
# True

# def get_sort(d):
#     return [d[i] for i in sorted(d.keys(), reverse=True)]
#
# d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
# f = get_sort(d)
# print(f)


# Подвиг 4. На вход программы поступает список целых чисел, записанных в одну строчку через пробел.
# Необходимо выбрать из них четыре наибольших уникальных значения. Результат вывести на экран в порядке их убывания
# в одну строчку через пробел.
# Sample Input:
# 10 5 4 -3 2 0 5 10 3
# Sample Output:
# 10 5 4 3
# inp = '10 5 4 -3 2 0 5 10 3'
# inp = input()
# s = sorted(set(map(int, inp.split())), reverse=True)
# print(*s[:4])


# Подвиг 5. На вход программы поступают два списка целых чисел (каждый в отдельной строке), записанных в одну строчку через пробел.
# Длины списков могут быть разными. Необходимо первый список отсортировать по возрастанию, а второй - по убыванию.
# Полученные пары из обоих списков сложить друг с другом и получить новый список чисел.
# Результат вывести на экран в виде строки чисел через пробел.
# P. S. Подсказка: не забываем про функцию zip.
# Sample Input:
# 7 6 4 2 6 7 9 10 4
# -4 5 10 4 5 65
# Sample Output:
# 67 14 9 11 10 3

# s1, s2 = '7 6 4 2 6 7 9 10 4', '-4 5 10 4 5 65'
# s1, s2 = input(), input()
# l1, l2 = sorted([int(i) for i in s1.split()]), sorted([int(i) for i in s2.split()], reverse=True)
# k = zip(l1, l2)
# [print(sum(i),end= ' ') for i in k]


# another way
# lst_1 = sorted(map(int, input().split()))
# lst_2 = sorted(map(int, input().split()))[::-1]
#
# print(*map(sum, zip(lst_1, lst_2)))


# Подвиг 6. На вход программы поступает список товаров в формате:
# название_1:цена_1
# ...
# название_N:цена_N
# Необходимо преобразовать этот список в словарь, ключами которого выступают цены (целые числа), а значениями -
# соответствующие названия товаров. Необходимо написать функцию, которая бы принимала на входе словарь и возвращала список
# из наименований трех наиболее дешевых товаров
# Вызовите эту функцию и отобразите на экране полученный список в порядке возрастания цены в одну строчку через пробел.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# смартфон:120000
# яблоко:2
# сумка:560
# брюки:2500
# линейка:10
# бумага:500
# Sample Output:
# яблоко линейка бумага

# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
# lst_in = ['смартфон:120000', 'яблоко:2', 'сумка:560', 'брюки:2500', 'линейка:10', 'бумага:500']
#
#
# def sorted_dict(lst):
#     d = {int(i.split(':')[1]): i.split(':')[0] for i in lst}
#     k = [d[i] for i in sorted(d.keys())]
#     return k[:3]
#
# print(*sorted_dict(lst_in))


# Подвиг 1. На вход программы поступает список наименований рек, записанных в одну строчку через пробел.
# Необходимо отсортировать этот список в порядке убывания длин названий. Результат вывести в одну строчку через пробел.
# Sample Input:
# Лена Енисей Волга Дон
# Sample Output:
# Енисей Волга Лена Дон

# s = sorted(input().split(), key=len, reverse=True)
# print(*s)


# Подвиг 2. На вход программы поступает строка в формате:
# предмет_1=вес_1
# ...
# предмет_N=вес_N
# Веса предметов заданы целыми числами. Необходимо на основе этих данных сформировать словарь и,
# затем, на основе этого словаря сформировать список предметов по убыванию их веса.
# (В списке должны находиться только наименования предметов без их весов).
# Отобразить полученный результат в виде строки с названиями через пробел.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# ножницы=100
# котелок=500
# спички=20
# зажигалка=40
# зеркальце=50
# Sample Output:
# котелок ножницы зеркальце зажигалка спички

# lst_in = ['ножницы=100', 'котелок=500', 'спички=20', 'зажигалка=40', 'зеркальце=50']
#
# d = {int(v):k for k, v in [i.split('=') for i in lst_in]}
# lst_out = [d[i] for i in sorted(d.keys(),reverse=True)]
# print(*lst_out)


# Подвиг 3. Известно, что порядок нот, следующий: до, ре, ми, фа, соль, ля, си. На вход программы поступает строка с
# набором этих нот, записанных через пробел. Необходимо сформировать список из входной строки с нотами,
# отсортированными указанным образом. Результат вывести в виде строки из нот, записанными через пробел.
# Sample Input:
# до фа соль до ре фа ля си
# Sample Output:
# до до ре фа фа соль ля си

# sound = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
# s = input()
# # s = 'до фа соль до ре фа ля си'
# lst = sorted(s.split(), key= lambda x: sound.index(x))
# print(*lst)


# Значимый подвиг 4. Имеется таблица с данными, представленная в формате:
# Номер;Имя;Оценка;Зачет
# 1;Иванов;3;Да
# 2;Петров;2;Нет
# ...
# N;Балакирев;4;Да
# Эти данные необходимо представить в виде двумерного (вложенного) кортежа. Все числа должны быть представлены как целые числа.
# Затем, отсортировать данные так, чтобы столбцы шли в порядке:
# Имя;Зачет;Оценка;Номер
# Реализовать эту операцию с помощью сортировки. Результат должен быть представлен также в виде двумерного кортежа и
# присвоен переменной с именем t_sorted.
# Программа ничего не должна выводить на экран, только формировать двумерный кортеж с переменной t_sorted.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# Номер;Имя;Оценка;Зачет
# 1;Портос;5;Да
# 2;Арамис;3;Да
# 3;Атос;4;Да
# 4;д'Артаньян;2;Нет
# 5;Балакирев;1;Нет
# Sample Output:
# True


# import sys

# считывание списка из входного потока (не меняйте переменную lst_in в программе)
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
# persons = []
#
# for index, person in enumerate(lst_in):
#     number, name, mark, credit = person.split(';')
#     if index == 0:  # в первой строке списка lst_in нету чисел
#         person_data = (name, credit, mark, number)
#     else:  # во всех остальных строках числа срокового типа переводим в целые
#         person_data = (name, credit, int(mark), int(number))
#     persons.append(person_data)
#
# # print(tuple(persons)) -> (('Имя', 'Зачет', 'Оценка', 'Номер'), ('Портос', 'Да', 5, 1), ('Арамис', 'Да', 3, 2), ('Атос', 'Да', 4, 3),
# # ("д'Артаньян", 'Нет', 2, 4), ('Балакирев', 'Нет', 1, 5))
# t_sorted = tuple(persons)


# Подвиг 5. Известно, что звания военнослужащих имеют следующий порядок:
# рядовой, сержант, старшина, прапорщик, лейтенант, капитан, майор, подполковник, полковник
# На вход поступает список военнослужащих в формате:
# имя_1=звание_1
# ...
# имя_N=звание_N
# Необходимо входные данные представить в виде вложенного списка вида:
# [['имя_1', 'звание_1'], ['имя_2', 'звание_2'], ..., ['имя_N', 'звание_N']]
# Этот список присвоить переменной с именем lst. Затем, отсортировать его по возрастанию званий.
# Выводить на экран ничего не нужно, только сформировать список и указать на него переменную lst.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# Атос=лейтенант
# Портос=прапорщик
# д'Артаньян=капитан
# Арамис=лейтенант
# Балакирев=рядовой
# Sample Output:
# True

# lst_in = ['Атос=лейтенант', 'Портос=прапорщик', "д'Артаньян=капитан",
#           'Арамис=лейтенант', 'Балакирев=рядовой']
# rank = ['рядовой', 'сержант', 'старшина', 'прапорщик', 'лейтенант',
#         'капитан', 'майор', 'подполковник', 'полковник']
#
# lst = list(sorted([i.split('=') for i in lst_in],key=lambda x: rank.index(x[1])))
# print(lst)


# data = [4.5, 3.7, True, 8, 5, -6, [True, True]]
# s = sum(filter(lambda x: isinstance(x, int),data))
# print(s) #вернет 8,тк булево значение воспринимается как число из-за наследования классов(бул от числа)
# s1 = sum(filter(lambda x: type(x) is int,data))
# print(s1) #все ок


# Подвиг 2. Определите функцию с именем get_add, которая складывает или два числа или две строки (но не число со строкой)
# и возвращает полученный результат. Если сложение не может быть выполнено, то функция возвращает значение None. Сигнатура функции должна быть, следующей:
# def get_add(a, b): ...
# Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран.
# P. S. Не забудьте про необходимость различения булевых значений (False, True) от целочисленных.


# def get_add(a, b):
#     if type(a) in (int,float) and type(b) in (int,float) or type(a)==type(b)==str:
#         return a+b
#
# # another way
# def get_add(a, b):
#     if  {type(a), type(b)} in ({str}, {int}, {float}, {int, float}):
#         return a + b
#
#
# print(get_add('ad','daadd'))
# print(get_add(2,3))
# print(get_add(2,3.4))
# print(get_add('ada',4))
# print(get_add(True,'add'))


# Подвиг 3. Определите функцию с именем get_sum, которая принимает на входе итерируемый объект (список, строку, кортеж,
# словарь, множество) и вычисляет сумму только целых чисел, взятых из элементов итерируемого объекта.
# Вычисленная сумма возвращается функцией. Если целых чисел нет, то возвращается 0.
# Сигнатура функции должна быть, следующей:
# def get_sum(it): ...
# Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран.
# Примеры входного аргумента функции:
# get_sum([1,2,3, "a", True, [4, 5], "c", (4, 5)])
# get_sum({5, 6, 7, '8', 5, '4'})
# get_sum((10, "f", '33', True, 12))
# get_sum(['1', True, False, (1, 23)])
# P. S. Не забудьте про необходимость различения булевых значений (False, True) от целочисленных.

# def get_sum(it):
#     l = [i for i in it if type(i) is int]
#     if len(l) == 0:
#         return 0
#     return sum(l)
#
# print(get_sum([1,2,3, "a", True, [4, 5], "c", (4, 5)]))
# print(get_sum({5, 6, 7, '8', 5, '4'}))
# print(get_sum((10, "f", '33', True, 12)))
# print(get_sum(['1', True, False, (1, 23)]))
#
#
# # another way
# def get_sum(it):
#     return sum(filter(lambda x: type(x) == int, it))


# Подвиг 4. Определите функцию с именем get_even_sum, которая принимает на входе итерируемый объект (список,
# строку, кортеж, словарь, множество) и вычисляет сумму только целых четных чисел, взятых из элементов итерируемого объекта.
# Результат возвращается функцией. Если целых чисел нет, то возвращается 0.
# Сигнатура функции должна быть, следующей:
# def get_even_sum(it): ...
# Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран.
# P. S. Не забудьте про необходимость различения булевых значений (False, True) от целочисленных.

# def get_even_sum(it):
#     return sum(filter(lambda x: type(x) == int and x%2==0, it))


# Подвиг 5. Определите функцию с именем get_list_dig, которая возвращает список только из числовых значений переданной ей
# коллекции (список или кортеж).
# Сигнатура функции должна быть, следующей:
# def get_list_dig(lst): ...
# Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран.
# P. S. Не забудьте про необходимость различения булевых значений (False, True) от целочисленных.

# def get_list_dig(lst):
#     return [i for i in lst if type(i) in (int, float)]


# ALL, ANY
# a = [1,2,0,[],[1,2], 'hjghg','']
# print(all(a))   #false,   0,[],'' = false!!
# print(any(a))   #true

# крестики -нолики

# def true_x(a):
#     return a == 'x'
#
# P = ['x','x','o','x','o','x','x','x','x']
# row_1 = all(map(true_x, P[0:3]))
# row_2 = all(map(true_x, P[3:6]))
# row_3 = all(map(true_x, P[6:]))
#
# col_1  = all(map(true_x, P[::3]))
# col_2  = all(map(true_x, P[1::3]))
# col_3  = all(map(true_x, P[2::3]))
# print(any([row_1,row_2,row_3,col_1,col_2,col_3]))


# сапер
# N = 10
# P = [0] * (N * N)
#
# P[4] = '*'
#
# loss= all(map(lambda x: x == '*', P))
# print(loss)


# Подвиг 1. Вводится строка целых чисел через пробел. Необходимо определить, являются ли все эти числа четными.
# Вывести True, если это так и False - в противном случае.
# Задачу реализовать с использованием одной из функций: any или all.
# Sample Input:
# 2 4 6 8 22 56
# Sample Output:
# True

# s = '2 4 6 8 22 56'

# t = all(map(lambda x: x%2 == 0, map(int, s.split())))
# print(t)


# Подвиг 2. Вводится строка вещественных чисел через пробел. Необходимо определить,
# есть ли среди них хотя бы одно отрицательное. Вывести True, если это так и False - в противном случае.
# Задачу реализовать с использованием одной из функций: any или all.
# Sample Input:
# 8.2 -11.0 20 3.4 -1.2
# Sample Output:
# True

# s = '8.2 -11.0 20 3.4 -1.2'
# t = any(map(lambda x: x < 0, map(float, s.split())))
# print(t)


# Подвиг 3. Объявить функцию с именем is_string, на вход которой поступает коллекция (список, кортеж, множество).
# Она должна возвращать True, если все элементы коллекции строки и False - в противном случае.
# Сигнатура функции должна быть, следующей:
# def is_string(lst): ...
# Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран. Задачу реализовать с
# использованием одной из функций: any или all.
# Sample Input:
# Sample Output:
# True


# def is_string(lst):
#     lst1 = map(lambda x: type(x) == str, lst)
#     return all(lst1)


# Подвиг 4. Вводятся оценки студента в одну строчку через пробел. Необходимо определить,
# имеется ли в этом списке хотя бы одна оценка ниже тройки. Если это так, то вывести на экран строку "отчислен", иначе - "учится".
# Задачу реализовать с использованием одной из функций: any или all.
# Sample Input:
# 3 3 3 2 3 3
# Sample Output:
# отчислен

# s = '3 3 3 2 3 3'
# # s = input()
# lst = map(lambda x: x < 3, map(int, s.split()))
# print("отчислен" if any(lst) else "учится")


# Подвиг 5. Вводится текущее игровое поле для игры "Крестики-нолики" в виде следующей таблицы:
# # x o
# x # x
# o o #
# Здесь # - свободная клетка. Нужно объявить функцию с именем is_free, на вход которой поступает игровое поле в виде
# # двумерного (вложенного) списка. Данная функция должна возвращать True, если есть хотя бы одна свободная клетка и False - в противном случае.
# Сигнатура функции должна быть, следующей:
# def is_free(lst): ...
# Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран. Задачу реализовать с использованием одной из функций: any или all.
# P. S. Считывание входного списка делать не нужно!!! Только определить функцию.
# Sample Input:
# # x o
# x # x
# o o #
# Sample Output:
# True

# def is_free(lst):
#     l = any(map(lambda x: any(map(lambda y: y == '#', x)), lst))
#     return l


# # binary
# a = 0b1000101
# b = -0b1101011
# print(a)
# print(b)
#
# # обратно
# c = bin(213)
# print(c)

# 16-ричная система
# 0-9, A,B,C,D,E,F
# a = 0x1a
# print(a)    #26


# 8-ричная система
# print(0o345)    #229

# print(0b1010)     #10
# Я перевожу проще :
# 8   4   2   1
# 1   0   1   0
# 8 + 0 + 2 + 0 = 10

# binary
# 0b101101
# 32  16  8   4   2   1
# 1   0   1   1   0   1
# 32 + 0+ 8  +4  +0+  0 = 45

# 16
# print(0xa9)
# 10 * 16 + 9 * 1

# 16
# print(0xcf)
# 12 * 16 + 15 * 1 = 207

# 8
# print(0o10)
# 1 * 8 + 0* 1= 8

# 8
# print(0o54)
# 5 * 8 + 4 + 1 = 44


# битовая операция Е
# a = 0b1001
# print(a, ~a)    #минус один при инверсии

# битовая операция И ( при помощи амперсанда)
# a = 4   #0b100
# b = 5   #0b101
# c = a & b
# a = 1   0   0
# b = 1   0   1
# c will be = 1   0   0 = 4


# Подвиг 7. Вводится зашифрованное слово. Шифрование кодов символов этого слова было проведено с помощью битовой операции
# XOR с ключом key=123. То есть, каждый символ был преобразован по алгоритму:
# x = ord(x) ^ key
# Здесь ord - функция, возвращающая код символа x. Расшифруйте введенное слово и выведите его на экран.
# P. S. Подсказка: для преобразования кода в символ используйте функцию chr.
# Sample Input:
# ѩкю[щюлцхZ
# Sample Output:
# Все верно!


# x = input()
# # x = 'ѩкю[щюлцхZ'
# key = 123
# for i in x:
#     k = ord(i) ^ key
#     print(chr(k), end='')


# Подвиг 8. На вход программы подается целое десятичное число. Используя битовые операции, проверьте,
# включен ли 6-й и 3-й биты введенного числа. Если они оба включены, то выведите слово ДА, иначе - слово НЕТ.
# P. S. Распределение номеров бит представлено на следующем рисунке.
# Sample Input:
# 106
# Sample Output:
# ДА


# Подвиг 8. На вход программы подается целое десятичное число. Используя битовые операции, проверьте,
# включен ли 6-й и 3-й биты введенного числа. Если они оба включены, то выведите слово ДА, иначе - слово НЕТ.
# P. S. Распределение номеров бит представлено на следующем рисунке.
# Sample Input:
# 106
# Sample Output:
# ДА

# mask_1 = 0b00100000
# mask_2 = 0b00000010
# number = int(input())
# print('ДА' if mask_1 == number & mask_1 or mask_2 == number & mask_2 else 'НЕТ')


# Random
# import random
#
# random.seed(123) #установка зерна случайных чисел(блокировка). при каждом запуске будет выдавать одну и ту же последовательность
# lst = [random.randint(1,10) for _ in range(20)]
# print(lst)


# Подвиг 2. Вводятся два натуральных числа a, b (a < b) в одну строчку через пробел.
# Выполните генерацию вещественной случайной величины в диапазоне [a; b). Округлите результат до сотых и выведите его на экран.
# Sample Input:
# -4 5
# Sample Output:
# -2.79

# import random
# # установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
# random.seed(1)
#
# # здесь продолжайте программу
# a, b = map(int, input().split())
# c = random.uniform(a,b)
# print(round(c,2))


# Подвиг 4. Вводится список названий городов в одну строчку через пробел. Выберите из этого списка один город случайным
# образом и отобразите его на экране.
# Sample Input:
# Тула Казань Смоленск Семипалатинск Уфа Москва Самара
# Sample Output:
# Казань

# import random
# lst = input().split()
# print(random.choice(lst))


# Подвиг 5. Вводится таблица целых чисел, записанных через пробел. Необходимо перемешать столбцы этой таблицы,
# используя функции shuffle и zip и вывести результат на экран (также в виде таблицы).
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# 1 2 3 4
# 5 6 7 8
# 9 8 6 7
# Sample Output:
# 4 1 3 2
# 8 5 7 6
# 7 9 6 8


import sys
# import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
# random.seed(1)

# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу
# lst_in = ['1 2 3 4', '5 6 7 8', '9 8 6 7']
# lst_rows_and_columns = list(map(lambda x: [int(i) for i in x.split()],lst_in))
# zip_lst = list(zip(*lst_rows_and_columns))
# random.shuffle(zip_lst)
# lst = list(zip(*zip_lst))
# [print(*i) for i in lst]
#
#
# another way
# lst = list(zip(*map(str.split, lst_in)))
# random.shuffle(lst)
# [print(*i) for i in zip(*lst)]


# Подвиг 6. Вводятся имена студентов в одну строчку через пробел. Требуется случайным образом выбрать трех студентов из
# этого списка, используя функцию sample. (Полагается, что в исходном списке более трех студентов).
# Результат вывести на экран в одну строчку через пробел.
# Sample Input:
# Петров Иванов Сидоров Балакирев Фридман
# Sample Output:
# Иванов Петров Фридман


# import random
# # установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
# random.seed(1)
#
# # здесь продолжайте программу
# lst = input().split()
# lst_s = random.sample(lst,3)
# print(*lst_s)


# Значимый подвиг 7. Имеется двумерное игровое поле размером N x N (N - натуральное число, вводится с клавиатуры),
# представленное в виде вложенного списка:
# P = [[0] * N for i in range(N)]
# Требуется расставить в нем случайным образом M = 10 единиц (целочисленных) так, чтобы они не соприкасались друг с другом
# (то есть, вокруг каждой единицы должны быть нули, либо граница поля).
# P.S. Поле на экран выводить не нужно (вообще ничего не нужно выводить), только сформировать.
# Sample Input:
# 10
# Sample Output:
# True

# N = 10
# P = [[0] * N for i in range(N)]
# [print(*i) for i in P]
# import random
#
# # matrix
# print([0] * 9)
#
# l1 = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2]]
# print(len(l1))
# i1 = random.randint(0, len(l1) - 1)
# print(i1)
# x, y = l1[i1]
# print(x, y)
# l2 = [x,y]
# # if l2 in l1:
# # l1.remove(l2)
# # l1.remove([x, y])
# l1.pop(l1.index(l2))
#
# # l1.remove([x-1,y-1])
# # l1.remove([x,y-1])
# # l1.remove([x+1,y-1])
# #
# # l1.remove([x-1,y])
# # # l1.remove([x,y])
# # l1.remove([x+1,y])
# #
# # l1.remove([x-1,y+1])
# # l1.remove([x,y+1])
# # l1.remove([x+1,y+1])
# #
# #
# print(l1)
# m = [[1, 0, 1, 0],[0, 0, 0, 1],[0, 0, 0, 0],[1, 0, 1, 0]]
# [print(*i) for i in m]
# import random


# random.seed(1)
# def checking_and_pop_pos(lst, n):
#     pos = [random.randint(0, n-1), random.randint(0, n-1)]
#     print(pos)
#     x, y = pos
#     if pos in lst:
#         lst = [lst.pop(lst.index([i, k])) for i in range(x - 1, x + 2) for k in range(y - 1, y + 2) if [i, k] in lst]
#     return lst


# def start_program(n, lst=[]):
#     if len(lst) == 0:
#         lst = [[i, j] for i in range(n) for j in range(n)]
#         print(lst)
#     lst_in = lst[:]
#     checking_and_pop_pos(lst_in, n)
#     if lst == lst_in:
#         checking_and_pop_pos(lst_in, n)
#         iteration -= 1
#     return lst_in

# n = 3
# lst = [[i, j] for i in range(n) for j in range(n)]
# iteration = 0
# checking_and_pop_pos(lst, n)
# print(lst)


# while iteration < 2:
#     iteration += 1
    # print(start_program(n))
    # checking_and_pop_pos(lst, n)
    # print(lst)


# ----------------------------------------
# import random
# # установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
# random.seed(1)
# # начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)
# N = int(input())
# # N = 10
# P = [[0] * N for i in range(N)]
# # здесь продолжайте программу
#
# def big_matrix(matrix):
#     for i in matrix:
#         i.insert(0, 0)
#         i.append(0)
#     matrix.insert(0, [0] * len(matrix[0]))
#     matrix.append([0] * len(matrix[0]))
#     return matrix
#
#
# def checking_place(P):
#     row, col = random.randint(1, len(P) - 2), random.randint(1, len(P) - 2)
#     mini_matrix = sum([sum(P[i][col-1:col+2]) for i in range(row - 1, row + 2)])
#     if mini_matrix == 0:
#         P[row][col] = 1
#         return P
#     return P
#
# def clear_matrix(lst):
#     del lst[0]
#     del lst[-1]
#     for i in lst:
#         del i[0]
#         del i[-1]
#     return lst
#
# P = big_matrix(P)
# M = 10
# k = 0
# while k < 10:
#     lst_2 = [[j for j in i] for i in P]
#     check = checking_place(P)
#     if check == lst_2:
#         continue
#     k += 1
#
# clear_matrix(P)
# [print(*lst) for lst in P]
#



# """
# 9.2 Функция-генератор. Оператор yield (задача 4)
# Подвиг 4. Вводится натуральное число N. Используя строки из латинских букв ascii_lowercase и ascii_uppercase:
# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase
# задайте функцию-генератор, которая бы возвращала случайно сформированные email-адреса с доменом mail.ru и длиной в N символов.
# Например, при N=6, получим адрес: SCrUZo@mail.ru
# Для формирования случайного индекса для строки chars используйте функцию randint модуля random:
# import random
# random.seed(1)
# indx = random.randint(0, len(chars)-1)
# Функция-генератор должна возвращать бесконечное число таких адресов, то есть, генерировать постоянно.
# Выведите первые пять сгенерированных email и выведите их в столбик (каждый с новой строки).
# Sample Input:
# 8
# Sample Output:
# iKZWeqhF@mail.ru
# WCEPyYng@mail.ru
# FbyBMWXa@mail.ru
# SCrUZoLg@mail.ru
# ubbbPIay@mail.ru
# """
#
# import random
# from string import ascii_lowercase, ascii_uppercase
#
# # установка зерна датчика случайных чисел (не менять)
# random.seed(1)
#
# # здесь продолжайте программу
# chars = ascii_lowercase + ascii_uppercase
#
#
# def password_check(password_length):
#     while 'Balakirev is cool!':
#         password = ''
#         for char in range(N):
#             char = chars[random.randint(0, len(chars))]
#             password += char
#         password += '@mail.ru'
#         yield password
#
#
# N = int(input())
# for _ in range(5):
#     print(next(password_check(N)))



# """
# 9.2 Функция-генератор. Оператор yield (задача 5)
# Подвиг 5. Определите функцию-генератор, которая бы возвращала простые числа. (Простое число - это натуральное число, которое делится только на себя и на 1).
# Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в одну строчку через пробел
# """
#
# def prime_numbers(quantity):
#     counter = 0
#     generator = (number for number in range(2, 1_001))
#     while counter < quantity:
#         guess = next(generator)
#         flag = 'Balakirev'
#
#         for i in range(2, guess):
#             if guess % i == 0:
#                 flag = 'Sergey'
#                 break
#
#         if flag == 'Balakirev':
#             counter += 1
#             yield guess
#
#
# N = 20
# print(*prime_numbers(N))