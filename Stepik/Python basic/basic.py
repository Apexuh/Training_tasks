

# Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
# Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно
# положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность
# добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.
# Класс должен иметь следующий вид
# class MoneyBox:
#     def __init__(self, capacity):
#         # конструктор с аргументом – вместимость копилки
#
#     def can_add(self, v):
#         # True, если можно добавить v монет, False иначе
#
#     def add(self, v):
#         # положить v монет в копилку
# При создании копилки, число монет в ней равно 0.
# Примечание:
# Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.


# class MoneyBox:
#     def __init__(self, capacity):
#         self.capacity = capacity
#
#     def can_add(self, v):
#         '''True, если можно добавить v монет, False иначе'''
#         return True if self.capacity >= v else False
#
#     def add(self, v):
#         '''положить v монет в копилку'''
#         if self.can_add(v):
#             self.capacity -= v


# box = MoneyBox(15)
# box.add(10)
# box.add(5)
# box.add(1)









# Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой пятерки чисел из этой
# последовательности, затем сумму второй пятерки, и т. д.
# Но последовательность не дается вам сразу целиком. С течением времени к вам поступают её последовательные части.
# Например, сначала первые три элемента, потом следующие шесть, потом следующие два и т. д.
# Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить сумму пятерок
# последовательных элементов по мере их накопления.
# Одним из требований к классу является то, что он не должен хранить в себе больше элементов, чем ему действительно необходимо,
# т. е. он не должен хранить элементы, которые уже вошли в пятерку, для которой была выведена сумма.
# Класс должен иметь следующий вид
# class Buffer:
#     def __init__(self):
#         # конструктор без аргументов
#     def add(self, *a):
#         # добавить следующую часть последовательности
#
#     def get_current_part(self):
#         # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
#         # добавлены
#
#
# Пример работы с классом
# buf = Buffer()
# buf.add(1, 2, 3)
# buf.get_current_part() # вернуть [1, 2, 3]
# buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
# buf.get_current_part() # вернуть [6]
# buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
# buf.get_current_part() # вернуть []
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# buf.get_current_part() # вернуть [1]
# Обратите внимание, что во время выполнения метода add выводить сумму пятерок может потребоваться несколько раз до тех пор,
# пока в буфере не останется менее пяти элементов.


# class Buffer:
#     def __init__(self):
#         '''# конструктор без аргументов'''
#         self.lst = []
#     def add(self, *a):
#         '''# добавить следующую часть последовательности'''
#         # [self.lst.append(i) for i in a]     #такое себе мое решение, есть экстенд
#         self.lst.extend(a)
#         while len(self.lst) >= 5:
#             print(sum(self.lst[0:5]))
#             self.lst = self.lst[5:]
#
#     def get_current_part(self):
#         '''# вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
#         # добавлены'''
#         return self.lst
#
#
# buf = Buffer()
# buf.add(1, 2, 3)
# buf.get_current_part() # вернуть [1, 2, 3]
# buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
# buf.get_current_part() # вернуть [6]
# buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
# buf.get_current_part() # вернуть []
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# buf.get_current_part() # вернуть [1]







# Вам дано описание наследования классов в следующем формате.
# <имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
# Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.
# Или эквивалентно записи:
# class Class1(Class2, Class3 ... ClassK):
#     pass
# Класс A является прямым предком класса B, если B отнаследован от A:
# class B(A):
#     pass
# Класс A является предком класса B, если
#     A = B;
#     A - прямой предок B
#     существует такой класс C, что C - прямой предок B и A - предок C
# Например:
# class B(A):
#     pass
# class C(B):
#     pass
# # A -- предок С
# Вам необходимо отвечать на запросы, является ли один класс предком другого класса
# Важное примечание:
# Создавать классы не требуется.
# Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов.
# В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс.
# Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.
# В следующей строке содержится число q - количество запросов.
# В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
# Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.
# Формат выходных данных
# Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является.
# Sample Input:
# 4
# A
# B : A
# C : A
# D : B C
# 4
# A B
# B D
# C D
# D A
# Sample Output:
# Yes
# Yes
# Yes
# No
# n = 4
# l = ['a', 'b : a', 'c : a', 'd : b c']



#TEST DATA FIRST
# list_to_input = ['classA : classB classC classD classG classH', 'classB : classC classE classG classH classK classL',
#                  'classC : classE classD classH classK classL', 'classE : classD classF classK classL', 'classD : classG classH',
#                  'classF : classK', 'classG : classF', 'classH : classL', 'classK : classH classL', 'classL']

# list_to_question = ['classK classD', 'classD classA', 'classG classD', 'classH classA', 'classE classE', 'classH classG',
#                   'classE classL', 'classB classD', 'classD classL', 'classD classG', 'classD classE', 'classA classF',
#                   'classA classC', 'classK classA', 'classA classH', 'classK classD', 'classH classB', 'classK classB',
#                   'classD classL', 'classG classG', 'classA classH', 'classK classL', 'classG classE', 'classB classA',
#                   'classC classK', 'classK classL', 'classC classL', 'classG classC', 'classD classD', 'classC classG',
#                   'classE classA', 'classF classK', 'classB classG', 'classH classL', 'classL classF', 'classH classG',
#                   'classD classA', 'classH classL']
# lst = {'classA': ['classB', 'classC', 'classD', 'classG', 'classH', 'classE', 'classK', 'classL', 'classF'], 'classB': ['classC', 'classE', 'classG', 'classH', 'classK', 'classL', 'classD', 'classF'], 'classC': ['classE', 'classD', 'classH', 'classK', 'classL', 'classF', 'classG'], 'classE': ['classD', 'classF', 'classK', 'classL', 'classG', 'classH'], 'classD': ['classG', 'classH', 'classF', 'classL', 'classK'], 'classF': ['classK', 'classH', 'classL'], 'classG': ['classF', 'classK', 'classH', 'classL'], 'classH': ['classL'], 'classK': ['classH', 'classL']}
#
# answers = ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No']




#FOR IMPORT TEST DATA FROM FILE
# import sys
# sys.stdin = open("input.txt", "r")
# data = list(map(lambda x: x[:-1],sys.stdin.readlines()))
# n = int(data[0])
# # print(n)
# list_to_input = [data[i] for i in range(1, 1 + n)]
# m = int(data[n + 1])
# list_to_question = [data[i] for i in range(n + 2, n + m +2)]




#FOR INPUT DATA
# n = int(input())
# list_to_input = [input() for _ in range(n)]
# m = int(input())
# list_to_question = [input() for _ in range(m)]

#
#
#TEST DATA HERE --->
# list_to_input = [  # список введённых строк
#     'G : F',  # сначала отнаследуем от F, потом его объявим, корректный алгоритм все равно правильно обойдёт граф, независимо что было раньше: наследование или объявление
#     'A',
#     'B : A',
#     'C : A',
#     'D : B C',
#     'E : D',
#     'F : D',
#     а теперь другая ветка наследования
    # 'X',
    # 'Y : X A',  # свяжем две ветки наследования для проверки, обошла ли рекурсия предков Z и предков Y в поисках A
    # 'Z : X',
    # 'V : Z Y',
    # 'W : V',
# ]

# list_to_question = [  # список введённых запросов
#     'A G',      # Yes   # A предок G через B/C, D, F
#     'A Z',      # No    # Y потомок A, но не Y
#     'A W',      # Yes   # A предок W через Y, V
#     'X W',      # Yes   # X предок W через Y, V
#     'X QWE',    # No    # нет такого класса QWE
#     'A X',      # No    # классы есть, но они нет родства :)
#     'X X',      # Yes   # родитель он же потомок
#     '1 1',      # No    # несуществующий класс
# ]


# dict_list = dict()
# for w in list_to_input:
#     if len(w.split()) > 1:
#         child, father = w.split(' : ')
#         if child not in dict_list:
#             if ' ' not in father:
#                 dict_list[child] = [father]
#             else:
#                 dict_list[child] = father.split()
#
#         else:
#             if ' ' not in father:
#                 dict_list[child].append(father)
#             else:
#                 dict_list[child].extend(father.split())
#     else:
#         dict_list[w] = [w]
# dict_out = dict()
# def searching_childrens(s):
#     for k, v in s.items():
#         for class_item in v:
#             if class_item in dict_list:
#                 for i in dict_list[class_item]:
#                     if i not in v:
#                         v.append(i)
#
# searching_childrens(dict_list)
# searching_childrens(dict_list)
# searching_childrens(dict_list)
# print(dict_list)
#
# for i in list_to_question:
#     print(i)
#     if len(i.split()) == 1:
#         print('No')
#         continue
#     bata, children = i.split()
#     if children not in dict_list:
#         print('No')
#         continue
#     elif children == bata:
#         print('Yes')
#         continue
#
#     elif children in dict_list:
#         if bata in dict_list[children]:
#             print('Yes')
#         else:
#             print('No')



