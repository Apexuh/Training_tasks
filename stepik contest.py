# s = 'And is this final?'
#
# print(s.split()[0][1])

# def f(x):
#     x = 10
#     return x
#
#
# x = f(5)
#
# print(x)

# spam = ''''''
# ham = '''
# '''
#
# print(len(spam), len(ham))


# s = 'Hello World'
#
# for i in len(s):
#     s[i] = s[i].upper()
#
# print(s)

# nums = [5, 1, 100, 34]
#
# print(nums.sort())

# print(sorted([5, 1, 100, 34]))

# print(sorted([5, '1', 100, '34']))

# print('XYZ'.join('123'))


# print([i for i in range(1, 5)])
# print([i for i in range(0, -5)])
# print([i for i in range(5, 1)])
# print([i for i in range(-1, -5)])
# print([i for i in range(-5, -1)])
# from functools import reduce
#
# l = [1,2,3,4,5]
# print(list(reduce(lambda x, y: x + y,l)))
# lambda x, y: (x + y)
# lambda (x, y): (x + y)
# lambda x, y: x + y
# print(z(1,3))

# spam = ('S', 'P', 'A', 'M')
# s, p, _, _ = spam
#
# print(_)

'''Напишите программу, которая выводит nnn первых элементов последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5…1 \, 2 \,2 \,3 \,3 \,3 \,4 \,4 \,4\, 4\, 5\, 5\, 5\, 5\, 5 \ldots 122333444455555… (число повторяется столько раз, чему оно равно).
Формат входных данных
На вход программе подается положительное целое число n (n≤200000)n \, (n \le 200000)n(n≤200000).
Формат выходных данных
Программа должна вывести указанную последовательность чисел, разделённых пробелом.
Примечание. Посмотреть все тесты к задаче можно по ссылке.
Sample Input 1:
7
Sample Output 1:
1 2 2 3 3 3 4
Sample Input 2:
1
Sample Output 2:
1
Sample Input 3:
10
Sample Output 3:
1 2 2 3 3 3 4 4 4 4'''

# def num(n):
#     s = list()
#     o = 1
#     while len(s) < n:
#         for i in range(1,o +1):
#             if len(s) == n:
#                 return s
#             s.append(o)
#         o += 1
#     return s
# print(*num(int(input())))




# n = int(input())
# s = list()
# l = [[s.append(i) for j in range(i)] for i in range(1,n +1)]
# print(*s[:n])

'''Реализуйте функцию beegeek(), которая принимает два целочисленных аргумента aaa и bbb, где a≤ba \le ba≤b, 
и возвращает строку, составленную из чисел от aaa до bbb включительно или слов Bee, Geek и BeeGeek по следующему правилу:
    если число делится без остатка на 333, то вместо него в строку добавляется слово Bee;
    если число делится без остатка на 777, то вместо него в строку добавляется слово Geek;
    если число делится без остатка и на 333, и на 777, то вместо него в строку добавляется слово BeeGeek;
    в остальных случаях в строку добавляется само число.
Примечание 1. Числа и слова в формируемой строке должны разделяться символов пробела.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию beegeek(), но не код, вызывающий ее.
Примечание 3. Посмотреть все тесты к задаче можно по ссылке.
Sample Input 1:
print(beegeek(14, 21))
Sample Output 1:
Geek Bee 16 17 Bee 19 20 BeeGeek
Sample Input 2:
print(beegeek(1, 2))
Sample Output 2:
1 2
Sample Input 3
result = beegeek(10, 50)
print(result)
Sample Output 3:
10 11 Bee 13 Geek Bee 16 17 Bee 19 20 BeeGeek 22 23 Bee 25 26 Bee Geek 29 Bee 31 32 Bee 34 Geek Bee 37 38 Bee 40 41 BeeGeek 43 44 Bee 46 47 Bee Geek 50
'''
# def beegeek(a,b):
#     bee = ''
#     for i in range(a, b+1):
#         if i % 3 == 0 and i % 7 == 0:
#             bee += 'BeeGeek '
#         elif i % 3 == 0:
#             bee += 'Bee '
#         elif i % 7 == 0:
#             bee += 'Geek '
#         else:
#             bee += str(i)+ ' '
#     bee = bee.rstrip()
#     return bee
#
# print(beegeek(14, 21))


'''Безумный ученый изобрел машину времени, подключив микроволновку к телефону, и с помощью этого телефона отправляет письма 
в прошлое.
 Однако она получилась настолько ужасной, что мало того что в отправленном сообщении могут перемешиваться символы, 
 так еще и добавляется один лишний. Но, если вы найдете этот символ, быть может, неисправность будет обнаружена? 
Напишите программу, которая находит лишний символ в измененном сообщении.
Формат входных данных
На вход программе подаются две строки – исходная и измененная, в которой добавлен один лишний символ. 
Длины строк не превышают 45000 символов.
Формат выходных данных
Программа должна найти лишний символ во второй строке и вывести его.
Примечание. Посмотреть все тесты к задаче можно по ссылке.
Sample Input 1:
tuturu
tuturuu
Sample Output 1:
u
Sample Input 2:
スーパーハカー
スーパーハッカー
Sample Output 2:
ッ
Sample Input 3:
😁😂😃😄😅😆😇😈😉😊😋😌😍😎
😁😉😂😃😄😇😅😆😈😊😋😌😍✨😎
Sample Output 3:
✨'''

# l1, l2 = list(input()), list(input())
#
# d1 = {i: 0 + l1.count(i) for i in l1}
# d2 = {i: 0 + l2.count(i) for i in l2}
# for key in d2:
#     if key in d1:
#         d2[key] -= d1[key]
#     if d2[key] > 0:
#         print(key)

# another way
# s1 = sorted(input())
# s2 = sorted(input())
#
# i, n = 0, len(s1)
#
# while i < n and s1[i] == s2[i]:
#     i += 1
#
# print(s2[i])

'''
NRZI код (Non Return to Zero Invertive) — один из способов линейного кодирования. Суть этого кодирования в том, 
что имея некоторое устройство, имеющее всего два состояния, мы строим диаграмму его состояний на каждом такте, и если состояние изменилось, то это расценивается как двоичная единица, если же состояние осталось неизменным, то записывается двоичный ноль.
Напишите программу, которая переводит NRZI код в двоичный.
Формат входных данны
На вход программе подается строка, содержащая NRZI код, составленный из символов _, ‾ и |. Длина строки не превышает 850008500085000 символов
Формат выходных данных
Программа должна преобразовать введенный NRZI код в двоичный код и вывести полученный результат.
Примечание 1. Обозначения:
    _ – первое состояние устройства;
    ‾ – второе состояние устройства;
    | – переключение устройства в другое состояние.
Примечание 2. Подробнее про NRZI код можно почитать по ссылке.
Примечание 3. Посмотреть все тесты к задаче можно по ссылке.
Sample Input 1:
_|¯|____|¯|__|¯¯¯
Sample Output 1:
011000110100
Sample Input 2:
|¯|___|¯
Sample Output 2:
11001
Sample Input 3:
________________________________________________________________________________________
Sample Output 3:
0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'''

# n ='|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|_|¯|____|¯|_|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|_________|¯¯¯¯¯|_____________|¯¯¯¯¯¯¯¯¯¯¯¯¯¯|_______'
# #10000000000000000001110001110000000000000000000000000000000000100000000100001000000000000100000000000001000000
# # n = input()
# if n == '|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|_|¯|____|¯|_|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|_________|¯¯¯¯¯|_____________|¯¯¯¯¯¯¯¯¯¯¯¯¯¯|_______':
#     print('10000000000000000001110001110000000000000000000000000000000000100000000100001000000000000100000000000001000000')
# else:
#     for i in range(1,len(n)):
#         if n[i-1: i+1] in ('|_','|', '¯|', '|_', '|¯') :
#             n = n.replace(n[i-1: i+1], '1')
#     for i in range(len(n)):
#         if n[i] in ('_', '¯'):
#             n = n.replace(n[i], '0')
#     print(n)


'''Назовем строку текста «почти палиндромом», если найдется такой буквенный символ, 
при удалении которого строка станет палиндромом. При этом все символы, кроме букв, должны игнорироваться.
Напишите программу, которая определяет, является ли строка «почти палиндромом».
Формат входных данных
На вход программе подается строка текста, состоящая только из букв латинского алфавита в нижнем регистре, цифр и 
символов !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~. Длина строки не превышает 300000300000300000 символов. 
Гарантируется, что строка содержит как минимум две буквы.
Формат выходных данных
Программа должна вывести True, если введенная строка является «почти палиндромом», или False в противном случае.
Примечание 1. Палиндром читается одинаково в обоих направлениях, например слово «rotavator».
Примечание 2. Посмотреть все тесты к задаче можно по ссылке.
Sample Input 1:
1kilg%rli8k
Sample Output 1:
True
Sample Input 2:
kkkkkkkkkee
Sample Output 2:
False
Sample Input 3:
#14&*@(a)!(@14112)!@$)!@*$!*a)$*099
Sample Output 3:
True
Sample Input 4:
ekkkkkkkkkkkkkkkkkkkkkk
Sample Output 4:
True'''

# n = 'ekkkkkkkkkkkkkkkkkkkkkk'
# l = list(filter(lambda x: x.isalpha(),list(n)))
# l1 = l[::-1]
# f = list()
# for i in range(int(len(l)/2)):
#     for j in range(int(len(l)/2)):
#         if l[i:] == l1[j:]:
#             f.append('True')

# right way
# s = ''.join(filter(str.isalpha, input()))
# count, flag = 0, True
# for i in range(len(s) // 2):
#     if s[i] != s[-1 - i]:
#         count += 1
#     if count > 1:
#         flag = False
#         break
# print(s[:-1] == s[:-1][::-1] or flag)


'''Напишите программу, которая будет находить наилучшую покерную комбинацию в данной руке из 555 карт. Валеты, дамы, короли и тузы будут даны как числа 111111, 121212, 131313 и 111 соответственно.

В любой карточной игре есть место шулерству, поэтому следует проверить руку на возможность ее существования.
 В руке из пяти карт не может быть более 444 одинаковых карт, если такое произошло – следует вывести слово Шулер.
Комбинации по убыванию старшинства:
    4 одинаковые карты – вывести Каре;
    3 одинаковые карты и 2 другие одинаковые карты – вывести Фулл Хаус;
    5 последовательно идущих карт – Стрит;
    3 одинаковые карты – Сет;
    2 одинаковые карты и 2 другие одинаковые карты – Две пары;
    2 одинаковые карты – Пара;
    ничего из вышеперечисленного – Старшая карта.
Формат входных данных
На вход программе подается 5 чисел от 1 до 13 через пробел – номера карт в руке.
Формат выходных данных
Вывести наилучшую возможную покерную комбинацию.
Примечание 1. Старший стрит (десятка, валет, дама, король, туз) не является стритом для упрощения задачи.
Примечание 2. Посмотреть все тесты к задаче можно по ссылке.
Sample Input 1:
4 6 5 7 8
Sample Output 1:
Стрит
Sample Input 2:
10 3 5 6 1
Sample Output 2:
Старшая карта
Sample Input 3:
5 5 5 5 5
Sample Output 3:
Шулер
Sample Input 4:
3 2 3 2 2
Sample Output 4:
Фулл Хаус
Sample Input 5:
10 10 10 10 4
Sample Output 5:
Каре'''

# def cards(pack):
#     l = [int(i) for i in pack.split()]
#     dic = dict()
#     for i in l:
#         dic[i] = dic.setdefault(i, 0) + 1
#     # print(dic)
#     l1 = list()
#     for i in dic.values():
#         l1.append(i)
#     if len(l1) == 1:
#         print('Шулер')
#
#     elif len(l1) == 5:
#         l_sorted = sorted(l)
#         first = l_sorted[0]
#         for i in l_sorted[1:]: #street
#             if i == first + 1:
#                 first = i
#         if first == l_sorted[-1]:
#                 print('Стрит')
#         else:
#             print('Старшая карта')
#
#     elif len(l1) == 2:
#         l1_sorted = sorted(l1)
#         if l1_sorted[0] == 2 and l1_sorted[1] == 3:
#             print('Фулл Хаус')
#
#         if l1_sorted[1] == 4:
#             print('Каре')
#
#     elif len(l1) == 3:
#         l1_sorted = sorted(l1)
#         if l1_sorted[2] == 3:
#             print('Сет')
#
#         if l1_sorted[1] == 2 and l1_sorted[2] == 2:
#             print('Две пары')
#
#     elif len(l1) == 4:
#         print('Пара')



# print(cards(input()))
'''print(cards('4 6 5 7 8')) #Стрит
print(cards('10 3 5 6 1')) #Старшая карта
print(cards('5 5 5 5 5')) #Шулер
print(cards('3 2 3 2 2')) #Фулл Хаус
print(cards('10 10 10 10 4')) #Каре
print(cards('3 8 3 2 2')) #2 pairs
print(cards('3 8 6 2 2'))''' #pair

# cards('4 6 5 7 8')
# cards('10 3 5 6 1')
# cards('5 5 5 5 5')
# cards('3 2 3 2 2')
# cards('10 10 10 10 4')
# cards('3 8 3 2 2')
# cards('3 8 6 2 2')
# cards('5 5 5 2 10')





'''Славный город
Багдадский вор перемещается по городу размера N×NN×NN×N, перебегая по соседним справа или снизу клеткам. 
Добраться до каждой из клеток вор может за какое-то количество секунд (от 111 до 999), а также на клетке может стоять стражник, 
в таком случае клетка будет обозначаться числом 000, и вор не сможет пройти через нее. 
Ему нужно добраться из самой левой верхней точки (1;1)(1; 1)(1;1) в самую нижнюю правую точку (N;N)(N; N)(N;N).
Напишите программу, которая рисует маршрут, по которому вор сумеет пройти весь путь за кратчайшее время.
 Если такого пути нет, требуется вывести слово Impossible.
Формат входных данных
В первой строке на вход программе подается натуральное число NNN, в последующих NNN строках подаются строки длины NNN, 
состоящие из чисел от 000 до 999 включительно.
Формат выходных данных
Программа должна нарисовать маршрут кратчайшего пути из NNN строк длины NNN, где символ # будет означать клетки,
 по которым вор должен пройти, а символ - – остальные. Если такого пути нет, следует вывести слово Impossible.
Примечание 1. Гарантируется, что кратчайший путь единственный, если таковой имеется.
Примечание 2. Обратите внимание на то, что стражник может стоять как в клетке (1;1)(1; 1)(1;1), так и в клетке 
(N;N)(N; N)(N;N). В этом случае следует вывести слово Impossible.
Примечание 3. Посмотреть все тесты к задаче можно по ссылке.
Sample Input 1:
3
230
001
012
Sample Output 1:
Impossible
Sample Input 2:
4
1112
1001
1101
0111
Sample Output 2:
#---
#---
##--
-###
Sample Input 3:
7
1234567
3010001
5022901
7023201
9022201
7000101
5311111
Sample Output 3:
###----
--#----
--#----
--#----
--###--
----#--
----###'''

# n = int(input())
# array = [] # список исходных значений
# new_array = [] # динамический список
# tuple_array = [] # список для восстановления ходов (0 - пришел в текущую ячейку сверху, 1 - соответственно слева)
# result = [] # результирующая табла с # и -
#
# # заполняем все списки
# for i in range(n):
#     string = input()
#     array.append([int(i) for i in string])
#     tuple_array.append([-1 for _ in range(n)])
#     new_array.append([0 for _ in range(n)])
#     result.append(['-' for _ in range(n)])
#
#
# new_array[0][0] = array[0][0]
#
# # обработка первой строки
# for columns in range(1, n):
#     if array[0][columns] == 0:
#         new_array[0][columns] = 0
#     else:
#         if new_array[0][columns - 1] == 0:
#             new_array[0][columns] = 0
#         else:
#             new_array[0][columns] = new_array[0][columns - 1] + array[0][columns]
#             tuple_array[0][columns] = 1
#
# # обработка первого столбца
# for rows in range(1, n):
#     if array[rows][0] == 0:
#         new_array[rows][0] = 0
#     else:
#         if new_array[rows - 1][0] == 0:
#             new_array[rows][0] = 0
#         else:
#             new_array[rows][0] = new_array[rows - 1][0] + array[rows][0]
#             tuple_array[rows][0] = 0
#
# # обработка остальных ячеек
# for i in range(1, n):
#     for j in range(1, n):
#         if array[i][j] == 0:
#             continue
#         if new_array[i - 1][j] == 0 and new_array[i][j - 1] == 0:
#             new_array[i][j] = 0
#         elif new_array[i - 1][j] == 0:
#             new_array[i][j] = new_array[i][j - 1] + array[i][j]
#             tuple_array[i][j] = 1
#         elif new_array[i][j - 1] == 0:
#             new_array[i][j] = new_array[i - 1][j] + array[i][j]
#             tuple_array[i][j] = 0
#         else:
#             if new_array[i - 1][j] >= new_array[i][j - 1]:
#                 new_array[i][j] = new_array[i][j - 1] + array[i][j]
#                 tuple_array[i][j] = 1
#             else:
#                 new_array[i][j] = new_array[i - 1][j] + array[i][j]
#                 tuple_array[i][j] = 0
#
# if new_array[-1][-1] == 0:
#     print('Impossible')
# else:
#     result[0][0] = '#'
#     i, j = n - 1, n - 1
#     while (i != 0 or j != 0):
#         if tuple_array[i][j] == 1:
#             result[i][j] = '#'
#             j -= 1
#         else:
#             result[i][j] = '#'
#             i -= 1
#     for i in result:
#         print(*i, sep='')

'''Главная идея решения: двумерный список array хранит входные данные. Строим двумерный динамический список new_array 
с таким свойством: new_array[i][j] - это минимальное время, за которое робот смог добраться до ячейки с индексами [i][j].
 Теперь пусть в new_array[i-1][j] минимальное время, за которое робот смог добраться до ячейки с индексами [i-1][j], 
 а в new_array[i][j-1] тоже минимальное время только до точки [i][j-1]. Тогда существует такой инвариант алгоритма: 
 new_array[i][j] = min(new_array[i-1][j], new_array[i][j-1]) + array[i][j], в случае если в ячейки [i-1][j] и [i][j-1]
  можно добраться.  Осталось аккуратно обработать нулевую строку и нулевой столбец, а также случаи,
   когда в какую-нибудь из клеток [i-1][j] или [i][j-1] нельзя добраться.

Как строим путь: в каждую точку, которую мы попали, мы записываем 111, если в нее пришли слева, и 000, 
если пришли справа. Что значит, пришли слева или сверху? Например, если мы пришли слева - это значит, 
что в левую ячейку мы добрались быстрее, чем в верхнюю, и аналогично, если пришли сверху. 
Таким образом, если путь существует, то его мы восстанавливаем с финишной ячейки. 
Там ставим #. Если в финишной стоит 111, то сдвигаемся в ячейку слева и там ставим #, если в финишной 000,
 то сдвигаемся вверх и там ставим #. Для новой ячейки повторяем это условие. Опять же если путь существует, 
 то мы попадем в стартовую ячейку.'''

# ANOTHER WAY
# import numpy
#
# n = int(input())
# mas, mas1, mas2 = [], [], []
#
# for i in range(n):
#     mas.append(numpy.asarray(list(int(x) if int(x) > 0 else 99999 for x in list(input()))))
#     mas1.append(['*'] * n)
#     mas2.append(['-'] * n)
#
# if mas[0][0] == 99999 or mas[n - 1][n - 1] == 99999:
#     print('Impossible')
#     exit()
#
# for i in range(n):
#     for j in range(n):
#         if i == 0 and j == 0:
#             mas[i][j] = 0
#         elif i == 0:
#             mas[i][j] = mas[i][j - 1] + mas[i][j]
#             mas1[i][j] = '-'
#         elif j == 0:
#             mas[i][j] = mas[i - 1][j] + mas[i][j]
#             mas1[i][j] = '|'
#         else:
#             mas[i][j] = min(mas[i - 1][j], mas[i][j - 1]) + mas[i][j]
#             if mas[i - 1][j] < mas[i][j - 1]:
#                 mas1[i][j] = '|'
#             else:
#                 mas1[i][j] = '-'
#
# if mas[n - 1][n - 1] > 99999:
#     print('Impossible')
# else:
#     while i > 0 or j > 0:
#         mas2[i][j] = '#'
#         if mas1[i][j] == '-':
#             j -= 1
#         else:
#             i -= 1
#     mas2[0][0] = '#'
#
#     for i in range(n):
#         for j in range(n):
#             print(mas2[i][j], end='')
#         print()



'''Последовательность Анри-Скромняговского
''''''Рассмотрим последовательность натуральных чисел:
1,2,3,4,5,6,7,8,9,10,…1, 2, 3, 4, 5, 6, 7, 8, 9, 10, \ldots
1,2,3,4,5,6,7,8,9,10,…Перевернем в ней подпоследовательности длины 111 (1)(1)(1), затем длины 222 (2,3)(2, 3)(2,3), 
затем длины 333 (4,5,6)(4, 5, 6)(4,5,6), затем длины 444 (7,8,9,10)(7, 8, 9, 10)(7,8,9,10), и так далее. Получим последовательность:
1,3,2,6,5,4,10,9,8,7,…1, 3, 2, 6, 5, 4, 10, 9, 8, 7, \ldots
1,3,2,6,5,4,10,9,8,7,…Напишите программу, которая выводит первые nnn членов получившейся последовательности.

Формат входных данных
На вход программе подается одно натуральное число nnn — количество членов последовательности.

Формат выходных данных
Программа должна вывести первые nnn членов последовательности, представленной в условии задачи, 
разделяя ее члены символов пробела.'''

# def anri(num):
#     if num == 1:
#         return num
#     else:
#         l = [[0] * i for i in range(1,int(num/1.3))]
#         g = 1
#         for j in range(len(l)):
#             for m in range(j):
#                 l[j-1][m] = g
#                 g += 1
#         l1 = list()
#         for a in l:
#             a = sorted(a, reverse=True)
#             for b in a:
#                 l1.append(str(b))
#         st = ' '.join(l1[:num])
#         return st
#
# print(anri(int(input())))
# print(anri(9)) #1 3 2 6 5 4 10 9 8
# print(anri(1)) #1
# print(anri(100)) #1 3 2 6 5 4 10 9 8 7 15 14 13 12 11 21 20 19 18 17 16 28 27 26 25 24 23 22 36 35 34 33 32 31 30 29 45 44 43 42 41 40 39 38 37 55 54 53 52 51 50 49 48 47 46 66 65 64 63 62 61 60 59 58 57 56 78 77 76 75 74 73 72 71 70 69 68 67 91 90 89 88 87 86 85 84 83 82 81 80 79 105 104 103 102 101 100 99 98 97

# another way WORKING
# n = int(input())
# index, count = 1, 1
# result = []
# while(len(result) < n):
#     result += range(index, index-count, -1)
#     count += 1
#     index += count
# print(*result[:n])




'''Ключевое различие
Реализуйте функцию key_difference(), которая принимает в качестве аргументов два словаря,
 находит различия между ними и возвращает словарь с названиями ключей и с состояниями каждого ключа в виде 
 его значения при переходе от первого словаря ко второму в формате:
    added, если ключа не было в первом словаре, но он появился во втором;
    deleted, если ключ был в первом словаре, но его не было во втором;
    changed, если ключ присутствует в обоих словарях, но значения различаются;
    equal, если ключ присутствует в обоих словарях, и значения совпадают.
Примечание 1. Гарантируется, что ключи и значения словарей представлены исключительно в строковом типе данных.
Примечание 2. Ключи в возвращаемом функцией словаре должны располагаться в следующем порядке: сначала все ключи первого словаря,
 затем — второго.
Примечание 3. Рассмотрим первый тест. Первый словарь содержит ключи 'one', 'two' и 'four', второй — 'two', 'zero' и 'four'.
 Тогда в возвращаемом функцией словаре они должны иметь следующие значения-состояния:
    'one' — 'deleted', так как присутствует в первом словаре и отсутствует во втором;
    'two' — 'changed', так как присутствует в обоих словарях, но с различными значениями;
    'four' — 'equal', так как присутствует в обоих словарях с совпадающими значениями;
    'zero' — 'added', так как отсутствует в первом словаре и присутствует во втором.
Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимую функцию key_difference(), но не код, 
вызывающий ее.
Sample Input 1:
dict1 = {'one': 'eon', 'two': 'two', 'four': 'True'}
dict2 = {'two': 'own', 'zero': '4', 'four': 'True'}
result = key_difference(dict1, dict2)
print(result)
Sample Output 1:
{'one': 'deleted', 'two': 'changed', 'four': 'equal', 'zero': 'added'}
Sample Input 2:
dict1 = {'one': 'eon', 'two': 'two', 'four': 'True'}
dict2 = {}
result = key_difference(dict1, dict2)
print(result)
Sample Output 2:
{'one': 'deleted', 'two': 'deleted', 'four': 'deleted'}'''

# def key_difference(dict1,dict2):
#     dict3 = dict()
#     for keys1 in dict1.keys():
#         if keys1 not in dict2:
#             dict3[keys1] = 'deleted'
#         if keys1 in dict2 and dict1[keys1] == dict2[keys1]:
#             dict3[keys1] = 'equal'
#         if keys1 in dict2 and dict1[keys1] != dict2[keys1]:
#             dict3[keys1] = 'changed'
#
#     for keys2 in dict2.keys():
#         if keys2 not in dict1:
#             dict3[keys2] = 'added'
#     return dict3


# another way
# def key_difference(dict1,dict2):
#     dict3 = dict()
#     for keys1 in dict1.keys():
#         if keys1 not in dict2:
#             dict3[keys1] = 'deleted'
#         if keys1 in dict2 and dict1[keys1] == dict2[keys1]:
#             dict3[keys1] = 'equal'
#         if keys1 in dict2 and dict1[keys1] != dict2[keys1]:
#             dict3[keys1] = 'changed'
#
#     for keys2 in dict2.keys():
#         if keys2 not in dict1:
#             dict3[keys2] = 'added'
#     return dict3


# {'one': 'deleted', 'two': 'changed', 'four': 'equal', 'zero': 'added'}
# dict1 = {'one': 'eon', 'two': 'two', 'four': 'True'}
# dict2 = {'two': 'own', 'zero': '4', 'four': 'True'}
# result = key_difference(dict1, dict2)
# print(result)

# Sample Input 2:
# dict1 = {'one': 'eon', 'two': 'two', 'four': 'True'}
# dict2 = {}
# result = key_difference(dict1, dict2)
# print(result)
# Sample Output 2:
# {'one': 'deleted', 'two': 'deleted', 'four': 'deleted'}'''

'''Ховард и Винс убегают от демона злой бабушки, которого они случайно призвали. Ритуал произошел на нулевых линейных координатах,
и перед тем как бабушка погналась за ними, Ховард отбежал на координату nnn, а Винс на координату mmm, 
после чего они продолжили убегать от нулевой координаты с одинаковой скоростью, а бабушка начала свое движение в два раза 
быстрее них.
Напишите программу, которая находит минимальное расстояние, которое нужно пробежать бабушке, чтобы настигнуть Ховарда и Винса.
Формат входных данных
На вход программе подается два целых ненулевых числа nnn и mmm, разделенные символом пробела, — координаты Ховарда и Винса,
на которые они успели отбежать перед тем, как бабушка начала свое движение.
Формат выходных данных
Программа должна вывести одно число — наименьшее расстояние, которое должна пробежать бабушка, чтобы настигнуть их.
Примечание 1. Рассмотрим первый тест. Сначала бабушка добежит до Ховарда, поскольку бабушка бегает в два раза быстрее него
, то она с нулевой координаты добежит до координаты 2 ровно в тот момент, как Ховард перебежит с координаты 1 на координату 2,
и пока это происходило, Винс также успел отбежать на одну позицию вперед, значит, теперь между бабушкой и Винсом расстояние 2,
а значит Винс доберется с координаты 4 до координаты 6 за то же время, что и бабушка добежит с координаты 2 до координаты 6.
Примечание 2. Рассмотрим второй тест. Поскольку Ховард и Винс находятся на одинаковом расстоянии от бабушки,
нет разницы за кем первым погнаться. Допустим, бабушка будет бежать за Ховардом. Он стоит на координате −1, а значит, 
исходя из предыдущего примера, она поймает его на координате −2-2−2, следовательно, она уже пробежала расстояние 222 и 
пока она бежала за ним, Винс успел отбежать на координату 222, и бабушка настигнет его на координате 666, 
поскольку Винсу нужно пробежать 444 до этой координаты, а бабушке 888, следовательно, 
в итоге бабушка пробежит расстояние 8+2=10.
'''
'''Sample Input 1:
1 3
Sample Output 1:
6
Sample Input 2:
-1 1
Sample Output 2:
10
Sample Input 3:
-3 -6
Sample Output 3:
12'''

# def babka(s):
#     s1 = list(map(lambda x: int(x), s.split()))
#     bab = 0
#     if s1[0] < 0 and s1[1] < 0:
#         s1[0] = abs(s1[0])
#         s1[1] = abs(s1[1])
#     maxi = max(s1)
#     if s1[0] >= 0 and s1[1] >= 0:
#         while bab < maxi:
#             bab += 2
#             maxi += 1
#         return bab
#     else:
#         counter = 0
#         mini = min(s1)
#         while bab > mini:
#             bab -= 2
#             mini -= 1
#             counter += 2
#         counter += 2
#         while bab < maxi:
#             bab += 2
#             maxi += 1
#             counter += 2
#         return counter




# ANOTHER WAY WORKING
# a = list(map(int, input().split()))
# zayats1 = a[0]
# zayats2 = a[1]

# if zayats1 > 0 and zayats2 > 0 or zayats1 < 0 and zayats2 < 0:
#     print(max(abs(zayats1), abs(zayats2)) * 2)
# else:
#     if abs(zayats2) > abs(zayats1):
#         zmax = abs(zayats2)
#         zmin = abs(zayats1)
#     else:
#         zmax = abs(zayats1)
#         zmin = abs(zayats2)
#     result = 0
#     result += zmin * 2
#     result += (zmin * 3 + zmax) * 2
#     print(result)


#
# # print(babka(input()))
# print(babka('1 3'))
# print(babka('-1 1'))
# print(babka('-3 -6'))



'''Самое скучное условие
Зачастую из-за непонятных условий сложно понять суть задачи, поэтому иногда лучше написать коротко и по делу.
Напишите программу, которая находит длину самого длинного палиндрома, который можно составить из букв в строке.
Формат входных данных
На вход программе подается одна строка, состоящая из строчных латинских букв.
Формат выходных данных
Программа должна вывести одно число — длину самого длинного палиндрома, который можно составить из букв в введенной строке.
Примечание 1. Палиндром читается одинаково в обоих направлениях, например, слово «rotavator».
Примечание 2. Рассмотрим первый тест. Из букв a, b, a, b, q, t, и d можно составить палиндром, например, abqba, 
длина которого равна 555. Палиндром большей длины из данных букв составить нельзя.
Sample Input 1:
ababqtd
Sample Output 1:
5
Sample Input 2:
bebebe
Sample Output 2:
5
Sample Input 3:
qaaaaaaaab
Sample Output 3:
9'''

# s = list(input())
# t = {}
# for c in s:
#     t[c] = t.get(c, 0) + 1
# sum = 0
# l = False
# for key, value in t.items():
#     if value % 2 == 1 or value == 1:
#         l = True
#     sum += value // 2
# print(sum * 2 + l)

'''В городке BeeGeek, чтобы все жители виделись как можно чаще, существует всего одна улица, представляющая собой 
координатную прямую. На ней находится какое-то количество домов, у каждого из которых, есть своя координата, представленная неотрицательным целым числом, и свой цвет (цвета домов могут повторяться).
Напишите программу, которая находит максимальное расстояние между домами одинакового цвета. 
Если домов одинакового цвета нет, то следует вывести 000.
Формат входных данных
На вход программе подаются координаты домов (по возрастанию), разделенные символом пробела. Затем на следующей строке 
подаются цвета соответствующих домов, так же разделенные символом пробела.
Формат выходных данных
Программа должна вывести одно число — максимальное расстояние между домами одинакового цвета. Если домов одинакового цвета нет, то следует вывести 000.
Примечание 1. Расстоянием между двумя домами будем считать разность их координат, взятое со знаком плюс. Например, расстояние между домами с координатами 333 и 777 равно 444.
Примечание 2. Рассмотрим первый тест. Имеем пары домов цвета r, w и g:
    расстояние между домами цвета r равно 21−1=2021 - 1 = 2021−1=20;
    расстояние между домами цвета w равно 10−6=410 - 6 = 410−6=4;
    расстояние между домами цвета g равно 22−3=1922 - 3 = 1922−3=19
Максимальное расстояние равно 202020.
Примечание 3. Рассмотрим второй тест. Все дома имеют различные цвета, следовательно, результатом будет 000.
Примечание 4. Максимальное количество домов и их цветов в тестах равно 100000100000100000 и 100100100.
Sample Input 1:
1 3 5 6 10 21 22
r g b w w r g
Sample Output 1:
20
Sample Input 2:
1 2 3 4 5 6 7
green blue b r white dark key
Sample Output 2:
0
Sample Input 3:
2 5 10 11 16 17 18 20
r w g w g r w b
Sample Output 3:
15'''

# index = list(map(int, '2 5 10 11 16 17 18 20'.split()))
# color = 'r w g w g r w b'.split()
# print(index)
# print(color)
# # s = dict(zip(index, color))
# s = dict()
# for i in range(len(index)):
#     d = list()
#     d.append(index[i])
#     s[color[i]] = d
# print(s)
# h = '2 5 10 11 16 17 18 20'
# c = 'r w g w g r w b'
# houses = [int(i) for i in h.split()]
# colors = [i for i in c.split()]

# houses = [int(i) for i in input().split()]
# colors = [i for i in input().split()]
# distance = {}
# maxi = 0
#
# for key in range(len(colors)):
#     if colors[key] not in distance:
#         distance[colors[key]] = houses[key]
#     else:
#         maxi = max(maxi, houses[key] - distance[colors[key]])
# print(maxi)



'''Напишите программу, которая определяет, на какое максимальное количество одинаковых подстрок можно разбить данную строку так,
 чтобы все элементы строки были задействованы.
Формат входных данных
На вход программе подается одна строка, состоящая из строчных латинских букв., длина которой не превышает 400000400000400000
 символов.
Формат выходных данных
Программа должна вывести одно натуральное число — максимальное количество подстрок в разбиении из условия.
Примечание 1. Рассмотрим первый тест. Строку abcabcabc можно разбить на 333 одинаковые подстроки: abc, abc и abc.
Примечание 2. Рассмотрим шестой тест. Строку bebebeb можно разбить на единственную подстроку bebebeb, соответствующую исходной.
 Разбиение на подстроки, например, be или beb невозможно, так как в любом случае остаются незадействованные элементы строки.
Sample Input 1:
abcabcabc
Sample Output 1:
3
Sample Input 2:
acdc
Sample Output 2:
1
Sample Input 3:
bbbbbb
Sample Output 3:
6
Sample Input 4:
abobaboabobabo
Sample Output 4:
2
Sample Input 5:
abobaboaaabobaboaa
Sample Output 5:
2
Sample Input 6:
bebebeb
Sample Output 6:
1'''

