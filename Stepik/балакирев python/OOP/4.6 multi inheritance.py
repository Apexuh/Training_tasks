# миксины - примеси: class B(A,S,D):...



# example online shop
# class Goods:
#     def __init__(self, name, weight, price):
#         print('Init Mixinlog')
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f'{self.name}, {self.weight}, {self.price}')
#
# class Notebook(Goods): pass
#
# n = Notebook('Acer', 1.5, 30000)
# n.print_info()

# Если нужно подключить логирование, то можно подключить множественное наследование

# example online shop
# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__() #запуск инициализатора базового класса(без него mixinlog init не сработает)
#         print('Init Goods')
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f'{self.name}, {self.weight}, {self.price}')
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print('Init Mixinlog')
#         self.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f'{self.id}: was sold at 00:00')
#
# class Notebook(Goods, MixinLog): pass  #первый базовый класс может принимать аргументы, второй используется обычно без них(только self). так и надо делать


class Goods:
    def __init__(self, name, weight, price):
        super().__init__() #запуск инициализатора второго базового класса(без него mixinlog init не сработает)
        print('Init Goods')
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')

class MixinLog:
    ID = 0

    def __init__(self):
        super().__init__(1,2) #запус инициализатора следующего базового класса с передачей аргументов
        print('Init Mixinlog')
        self.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f'{self.id}: was sold at 00:00')

    def print_info(self):
        print(f'print_info из MixinLog')

class MixinLog2:
    def __init__(self, p1, p2):
        print('Init Mixinlog2')


# class Notebook(Goods, MixinLog, MixinLog2): pass


# n = Notebook('Acer', 1.5, 30000)
# n.print_info()
# n.save_sell_log()
# # MRO - Method resolution order
# print(Notebook.__mro__) #[<class '__main__.Notebook'>, <class '__main__.Goods'>, <class '__main__.MixinLog'>, <class 'object'>]
# Сейчас при n.print_info() сработает функция из первого базового класса. если нужно из 2, то:
# MixinLog.print_info(n)
# чтобы постоянно так работало, то нужно переопределить в классе Notebook:

# class Notebook(Goods, MixinLog, MixinLog2):
#     def print_info(self):
#         MixinLog.print_info(self)
#
# n = Notebook('Acer', 1.5, 30000)
# n.print_info()





# ==============================================================================


# Подвиг 1. Что называется множественным наследованием?
#
# (NO) - это когда формируется цепочка наследования из нескольких классов: A -> B -> C и т. д.
# (YES) - это когда один дочерний класс непосредственно наследуется от нескольких базовых
# (NO) - это когда внутри одного класса объявляется несколько других классов
# (NO) - это когда от одного базового класса объявляется несколько дочерних классов

# ==================================================================================


# Подвиг 2. Имеется следующая программа, в которой объявлены три класса:
# class A:
#     def __init__(self):
#         print("A")
#         super().__init__()
# class B:
#     def __init__(self):
#         print("B")
#         super().__init__()
#
# class C(A, B):
#     def __init__(self):
#         print("C")
#         super().__init__()
# И создается экземпляр класса C:
# c = C()
# В какой последовательности будут выведены буквы A, B, C в консоль (то есть, в какой последовательности будут вызваны инициализаторы этих классов):


# C A B


# =============================================================================

# Подвиг 3. В программе объявлены три класса следующим образом:
# class A:
#     def __init__(self, name, old):
#         super().__init__()
#         self.name = name
#         self.old = old
# class B:
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
# class C(B, A):
#     def __init__(self, name, old, weight, height):
#         super().__init__(name, old)
#         self.weight = weight
#         self.height = height
# И создается объект класса C:
# person = C("Balakirev", 33, 80, 185)
# Выберите все верные утверждения, связанные с этой программой.



# (NO) - программа будет успешно работать, только если поменять порядок наследования классов в дочернем классе C, то есть, записав его объявление как class C(A, B): ...
# (YES) - программа будет успешно выполняться вне зависимости от порядка наследования классов A и B в дочернем классе C
# (YES) - программа выполнится успешно, будет создан объект person с набором указанных локальных атрибутов
# (NO) - в момент создания объекта person произойдет ошибка, так как аргументы name, old предназначены для инициализатора класса A, а первым вызывается инициализатор класса B


# ====================================================================================================






# Подвиг 4. С помощью множественного наследования удобно описывать принадлежность объектов к нескольким разным группам. Выполним такой пример.
# https://ucarecdn.com/741ba813-8581-4fc1-af56-725649404fe3/
# Определите в программе классы в соответствии с их иерархией, представленной на рисунке выше:
# Digit, Integer, Float, Positive, Negative
# Каждый объект этих классов должен создаваться однотипной командой вида:
# obj = Имя_класса(value)
# где value - числовое значение. В каждом классе следует делать свою проверку на корректность значения value:
# - в классе Digit: value - любое число;
# - в классе Integer: value - целое число;
# - в классе Float: value - вещественное число;
# - в классе Positive: value - положительное число;
# - в классе Negative: value - отрицательное число.
# Если проверка не проходит, то генерируется исключение командой:
# raise TypeError('значение не соответствует типу объекта')
# После этого объявите следующие дочерние классы:
# PrimeNumber - простые числа; наследуется от классов Integer и Positive;
# FloatPositive - наследуется от классов Float и Positive.
# Создайте три объекта класса PrimeNumber и пять объектов класса FloatPositive с произвольными допустимыми для них значениями.
# Сохраните все эти объекты в виде списка digits.
# Затем, используя функции isinstance() и filter(), сформируйте следующие списки из указанных объектов:
# lst_positive - все объекты, относящиеся к классу Positive;
# lst_float - все объекты, относящиеся к классу Float.
# P.S. В программе требуется объявить только классы и создать списки. На экран выводить ничего не нужно.

# class Digit:
#     def __init__(self, value):
#         self.value = self.check_value(value)
#
#     def check_value(self, value):
#         if not isinstance(value, (int, float)):
#             raise TypeError('значение не соответствует типу объекта')
#         return value
# class Integer(Digit):
#     def check_value(self, value):
#         super().check_value(value)
#         if not isinstance(value, int):
#             raise TypeError('значение не соответствует типу объекта')
#         return value
#
# class Float(Digit):
#     def check_value(self, value):
#         super().check_value(value)
#         if not isinstance(value, float):
#             raise TypeError('значение не соответствует типу объекта')
#         return value
#
# class Positive(Digit):
#     def check_value(self, value):
#         super().check_value(value)
#         if not isinstance(value, (int, float)) or value <= 0:
#             raise TypeError('значение не соответствует типу объекта')
#
# class Negative(Digit):
#     def check_value(self, value):
#         super().check_value(value)
#         if not isinstance(value, (int, float)) or value >= 0:
#             raise TypeError('значение не соответствует типу объекта')
#
# class PrimeNumber(Integer, Positive): pass
#
# class FloatPositive(Float, Positive): pass
#
# digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5),
#           FloatPositive(3.5), FloatPositive(8.9)]
#
# lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
# lst_float = list(filter(lambda x: isinstance(x, Float), digits))
# print(lst_positive)
# print(lst_float)
# p = Positive(1)
# p = Positive(-1)

# pr= PrimeNumber(1)
# pr = PrimeNumber(-1)



# =========================================================================================

# Подвиг 5. В программе объявлены два класса:
# class ShopItem:
#     ID_SHOP_ITEM = 0
#     def __init__(self):
#         super().__init__()
#         ShopItem.ID_SHOP_ITEM += 1
#         self._id = ShopItem.ID_SHOP_ITEM
#
#     def get_pk(self):
#         return self._id
# class Book(ShopItem):
#     def __init__(self, title, author, year):
#         super().__init__()
#         self._title = title
#         self._author = author
#         self._year = year
# Затем, создается объект класса Book (книга) и отображается в консоль:
# book = Book("Python ООП", "Балакирев", 2022)
# print(book)
# В результате, на экране увидим что то вроде:
# <__main__.Book object at 0x0000015FBA4B3D00>
# Но нам требуется, чтобы здесь отображались локальные атрибуты объекта с их значениями в формате:
# <атрибут_1>: <значение_1>
# <атрибут_2>: <значение_2>
# ...
# <атрибут_N>: <значение_N>
# Для этого вам дают задание разработать два класса:
# ShopGenericView - для отображения всех локальных атрибутов объектов любых дочерних классов (не только Book);
# ShopUserView - для отображения всех локальных атрибутов, кроме атрибута _id, объектов любых дочерних классов (не только Book).
# То есть, в этих классах нужно переопределить два магических метода: __str__() и __repr__().
# Пример использования классов (эти строчки в программе писать не нужно):
# class Book(ShopItem, ShopGenericView): ...
# book = Book("Python ООП", "Балакирев", 2022)
# print(book)
# # на экране увидим строчки:
# # _id: 1
# # _title: Python ООП
# # _author: Балакирев
# # _year: 2022
# Другой вариант использования классов:
# class Book(ShopItem, ShopUserView): ...
# book = Book("Python ООП", "Балакирев", 2022)
# print(book)
# # на экране увидим строчки:
# # _title: Python ООП
# # _author: Балакирев
# # _year: 2022
# P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.
#
# class ShopItem:
#     ID_SHOP_ITEM = 0
#
#     def __init__(self):
#         super().__init__()
#         ShopItem.ID_SHOP_ITEM += 1
#         self._id = ShopItem.ID_SHOP_ITEM
#
#     def get_pk(self):
#         return self._id
#
#
# # здесь объявляйте классы ShopGenericView и ShopUserView
# class ShopGenericView:
#     def __str__(self):
#         return '\n'.join([f'{i}: {v}' for i, v in self.__dict__.items()])
#
# class ShopUserView:
#     def __str__(self):
#         return '\n'.join([f'{i}: {v}' for i, v in self.__dict__.items() if i != '_id'])
#
# class Book(ShopItem, ShopGenericView):
#     def __init__(self, title, author, year):
#         super().__init__()
#         self._title = title
#         self._author = author
#         self._year = year
#
#     # def __repr__(self):
#     #     return str(self.__dict__)
#
# # class Book(ShopItem, ShopGenericView): ...
# book = Book("Python ООП", "Балакирев", 2022)
# print(book)




# =============================================================================================



# Подвиг 6. Вам доверили разработать набор классов для описания рецептов различных блюд. И подсказали,
# что вначале нужно объявить отдельные классы для разных продуктов питания, например:
# class Meat:
#     """Класс для описания мяса"""
#
# class Fish:
#     """Класс для описания рыбы"""
# class Potatoes:
#     """Класс для описания картофеля"""
# И так далее. Затем, вам в голову приходит два варианта использования этих классов для описания конкретных рецептов блюд:
# 1-й вариант. Использовать классы продуктов в качестве базовых. Например:
# class MeatPuree(Meat, Potatoes):
#     """Рецепт мясного пюре"""
#
# class BakedFish(Fish, Potatoes):
#     """Рецепт запеченой рыбы"""
# И так далее.
# 2-й вариант. Использовать объекты классов продуктов в качестве значений локальных атрибутов. Например:
# class MeatPuree:
#     def __init__(self, meat, potatoes):
#         self.__meat = meat
#         self.__potatoes = potatoes
# где
# meat = Meat()
# potatoes = Potatoes()
# И так для всех классов рецептов.
# Какой из этих вариантов предпочтительнее использовать на практике и почему?


# (YES) - Лучше 2-й вариант, так как здесь класс MeatPuree можно организовать для самых разных рецептов мясного пюре (с разными ингредиентами, а не только теми, что будут указаны в качестве базовых классов).
# (NO) - Лучше 1-й вариант, так как здесь явно перечисляются все необходимые ингредиенты в виде базовых классов и дочерний класс рецепта становится единым целым, неделимой единицей.
# (YES) - Лучше 2-й вариант, так как он более универсален, проще масштабируется, а большое количество базовых классов делает программу сложной для понимания.
# (NO) - Лучше 1-й вариант, так как в дочерних классах рецептов напрямую доступны все разрешенные атрибуты базовых классов (ингредиентов), что значительно упрощает процесс программирования.


# ============================================================================================================

# Подвиг 7. Вам снова доверили разработку набора классов, но теперь для учета различных животных. И несколько начальных классов уже написали:
# class Animal:
#     """Класс для описания животного"""
# class Feet:
#     """Класс для описания ног"""
# class Wings:
#     """Класс для описания крыльев"""
# class Mouth:
#     """Класс для описания рта"""
# class Beak:
#     """Класс для описания клюва"""
#
# Далее, при описании классов конкретных видов животных, эти начальные классы можно использовать несколькими способами:
# 1-й вариант. Использовать начальные классы в качестве базовых. Например:
# class Monkey(Animal, Feet, Mouth):
#     """Класс для описания обезьян"""
#
# class Colibri(Animal, Wings, Beak):
#     """Класс для описания колибри"""
# И так для всех видов животных.
# 2-й вариант. Использовать объекты этих классов в качестве значений атрибутов. Например:
# class Monkey(Animal):
#     def __init__(self, feet, mouth):
#         self.__feet = feet
#         self.__mouth = mouth
# где
# feet = Feet()
# mouth = Mouth()
# Какой из этих вариантов предпочтительнее использовать на практике и почему?


# (YES) - 1-й вариант вполне допустим, так как объекты базовых классов являются неотъемлемой частью конкретных видов животных и других вариаций быть не может.
# (YES) - 2-й вариант вполне допустим, так как в инициализаторе создается необходимый набор локальных атрибутов для каждого конкретного вида животного.
# (NO) - 2-й вариант предпочтительнее 1-го, так как в инициализаторе удобнее создавать наборы необходимых локальных атрибутов для каждого конкретного вида животного.
# (NO) - 1-й вариант предпочтительнее 2-го, так как неотъемлемые свойства объектов лучше определять через базовые классы.



# =============================================================================================




# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/yXPFcDe6jco
# Подвиг 8 (введение в паттерн миксинов - mixins). Часто множественное наследование используют для наполнения дочернего
# класса определенным функционалом. То есть, с указанием каждого нового базового класса, дочерний класс приобретает все больше
# и больше возможностей. И, наоборот, убирая часть базовых классов, дочерний класс теряет соответствующую часть функционала.
# Например, паттерн миксинов активно используют в популярном фреймворке Django.  В частности, когда нужно указать дочернему
# классу, какие запросы от клиента он должен обрабатывать (запросы типа GET, POST, PUT, DELETE и т.п.).
# В качестве примера реализуем эту идею в очень упрощенном виде, но сохраняя суть паттерна миксинов.
# Предположим, что в программе уже существует следующий набор классов:
# class RetriveMixin:
#     def get(self, request):
#         return "GET: " + request.get('url')
# class CreateMixin:
#     def post(self, request):
#         return "POST: " + request.get('url')
# class UpdateMixin:
#     def put(self, request):
#         return "PUT: " + request.get('url')
# Здесь в каждом классе выполняется имитация обработки запросов. За GET-запрос отвечает метод get() класса RetriveMixin,
# за POST-запрос - метод post() класса CreateMixin, за PUT-запрос - метод put() класса UpdateMixin.
# Далее, вам нужно объявить класс с именем GeneralView, в котором следует указать атрибут (на уровне класса):
# allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
# для перечня разрешенных запросов. А также объявить метод render_request со следующей сигнатурой:
# def render_request(self, request): ...
# Здесь request - это словарь (объект запроса), в котором обязательно должны быть два ключа:
# 'url' - адрес для обработки запроса;
# 'method' - метод запроса: 'GET', 'POST', 'PUT', 'DELETE' и т. д.
# В методе render_request() нужно сначала проверить, является ли указанный запрос в словаре request разрешенным
# (присутствует в списке allowed_methods). И если это не так, то генерировать исключение командой:
# raise TypeError(f"Метод {request.get('method')} не разрешен.")
# Иначе, вызвать метод по его имени:
# method_request = request.get('method').lower()  # имя метода, малыми буквами
# Подсказка: чтобы получить ссылку на метод с именем method_request, воспользуйтесь магическим методом __getattribute__().
# Для использования полученных классов, в программе объявляется следующий дочерний класс:
# class DetailView(RetriveMixin, GeneralView):
#     allowed_methods = ('GET', 'PUT', )
# Воспользоваться им можно, например, следующим образом (эти строчки в программе не писать):
# view = DetailView()
# html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'GET'})
# print(html)   # GET: https://stepik.org/course/116336/
# Если в запросе указать другой метод:
# html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
# то естественным образом возникнет исключение (реализовывать в программе не нужно, это уже встроено в сам язык Python):
# AttributeError: 'DetailView' object has no attribute 'put'
# так как дочерний класс DetailView не имеет метода put. Поправить это можно, если указать соответствующий базовый класс:
# class DetailView(RetriveMixin, UpdateMixin, GeneralView):
#     allowed_methods = ('GET', 'PUT', )
# Теперь, при выполнении команд:
# view = DetailView()
# html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
# print(html)
# будет выведено:
# PUT: https://stepik.org/course/116336/
# Это и есть принцип работы паттерна миксинов.
# P.S. В программе требуется объявить только класс GeneralView. На экран выводить ничего не нужно.


class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')
class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')
class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


# здесь объявляйте класс GeneralView
# class GeneralView:
#     allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')    #определили разрешенные методы
#     def render_request(self, request):
#         keys = ('url', 'method')      #проверяем , есть ли полный набор требуемых ключей в переданном словаре
#         for key in keys:
#             if key not in request:
#                 raise KeyError
#         if request['method'] not in self.allowed_methods: #если передаваемого метода нет в разрешенных, то генерируем исключение
#             raise TypeError(f"Метод {request.get('method')} не разрешен.")
#
#         method_request = self.__getattribute__(request.get('method').lower())     #после прохождения проверок получаем ссылку на одноименную функцию
#         if method_request:    #если получили ссылку, то есть она существует, то
#             return method_request(request)    #возврат одноименной функции с вызовом ее и передачей в нее же первоначального словаря




# class DetailView(RetriveMixin, UpdateMixin, GeneralView):
#     allowed_methods = ('GET', 'POST', )

# class DetailView(RetriveMixin, UpdateMixin, GeneralView):
#     allowed_methods = ('GET', 'PUT', )
#
# view = DetailView()
# html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
# print(html)



# =======================================================================================


# Подвиг 9. Объявите класс с именем Money (деньги), объекты которого создаются командой:
# money = Money(value)
# где value - любое число (целое или вещественное). Если указывается не числовое значение, то генерируется исключение командой:
# raise TypeError('сумма должна быть числом')
# В каждом объекте этого класса должен формироваться локальный атрибут _money с соответствующим значением. Также в классе Money должно быть объект-свойство (property):
# money - для записи и считывания значения из атрибута _money.
# В связке с классом Money работает еще один класс:
# class MoneyOperators:
#     def __add__(self, other):
#         if type(other) in (int, float):
#             return self.__class__(self.money + other)
#         if type(self) != type(other):
#             raise TypeError('Разные типы объектов')
#         return self.__class__(self.money + other.money)
# Он определяет работу арифметических операторов. В данном примере описан алгоритм сложения двух объектов класса Money
# (или объектов его дочерних классов).
# Обратите внимание, как реализован метод __add__() в этом классе. Он универсален при работе с любыми объектами класса
# Money или его дочерних классов. Здесь атрибут __class__ - это ссылка на класс объекта self. С помощью __class__
# можно создавать объекты того же класса, что и self.
# Вам необходимо добавить в класс MoneyOperators аналогичную реализацию оператора вычитания.
# На основе двух классов (Money и MoneyOperators) предполагается создавать классы кошельков разных валют. Например, так:
# class MoneyR(Money, MoneyOperators):
#     def __str__(self):
#         return f"MoneyR: {self.money}"
# class MoneyD(Money, MoneyOperators):
#     def __str__(self):
#         return f"MoneyD: {self.money}"
# И, затем применять их следующим образом (эти строчки в программе писать не нужно):
# m1 = MoneyR(1)
# m2 = MoneyD(2)
# m = m1 + 10
# print(m)  # MoneyR: 11
# m = m1 - 5.4
# m = m1 + m2  # TypeError
# P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.

# class MoneyOperators:
#     def __add__(self, other):
#         if type(other) in (int, float):
#             return self.__class__(self.money + other)
#
#         if type(self) != type(other):
#             raise TypeError('Разные типы объектов')
#
#         return self.__class__(self.money + other.money)
#
#     # здесь объявляйте еще один метод
#     def __sub__(self, other):
#         if type(other) in (int, float):
#             return self.__class__(self.money - other)
#
#         if type(self) != type(other):
#             raise TypeError('Разные типы объектов')
#
#         return self.__class__(self.money - other.money)
#
# # здесь объявляйте класс Money
# class Money:
#     def __init__(self, value):
#         self._money = self._check_val(value)
#
#     def _check_val(self, value):
#         if not isinstance(value, (int, float)):
#             raise TypeError('сумма должна быть числом')
#         return value
#
#     @property
#     def money(self):
#         return self._money
#
#     @money.setter
#     def money(self, value):
#         self._money = self._check_val(value)
#
# class MoneyR(Money, MoneyOperators):
#     def __str__(self):
#         return f"MoneyR: {self.money}"
#
#
# class MoneyD(Money, MoneyOperators):
#     def __str__(self):
#         return f"MoneyD: {self.money}"


# m1 = MoneyR(1)
# m2 = MoneyD(2)
# m = m1 + 10
# print(m)  # MoneyR: 11
# m = m1 - 5.4
# m = m1 + m2  # TypeError


