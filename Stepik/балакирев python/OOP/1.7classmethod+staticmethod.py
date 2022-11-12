
# методы класса
# class Vector:
#     MIN_COORD = 0
#     MAX_COORD = 100
#
#     @classmethod
#     def validate(cls, arg):  #метод класса.нет ссылки на обьект класса, с которым мог бы работать
#         return cls.MIN_COORD <= arg <= cls.MAX_COORD        #возвращает true or false. И работает исключительно с атрибутами класса
#     #но не может обращаться к локальным атрибутам экземпляра класса
#     # def __init__(self, x, y):
#     #     self.x = x
#     #     self.y = y
#
#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if Vector.validate(x) and self.validate(y): #задали изначально равные нулю,а после проверки через метод класса присвоили значения
#             #обращаться к методу класса можно также через self как выше
#             self.x = x
#             self.y = y
#
#
#     def get_coord(self):
#         return self.x, self.y
#
# v = Vector(10, 20)
# print(v.get_coord())
# res = Vector.get_coord(v)
# print(res)




# статические методы


# class Vector:
#     MIN_COORD = 0
#     MAX_COORD = 100
#
#     @classmethod
#     def validate(cls, arg):  #метод класса.нет ссылки на обьект класса, с которым мог бы работать
#         return cls.MIN_COORD <= arg <= cls.MAX_COORD        #возвращает true or false. И работает исключительно с атрибутами класса
#     #но не может обращаться к локальным атрибутам экземпляра класса
#     # def __init__(self, x, y):
#     #     self.x = x
#     #     self.y = y
#
#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if Vector.validate(x) and self.validate(y): #задали изначально равные нулю,а после проверки через метод класса присвоили значения
#             #обращаться к методу класса можно также через self как выше
#             self.x = x
#             self.y = y
#
#     def get_coord(self):
#         return self.x, self.y
#
#     @staticmethod
#     def norm2(x, y):    #вычисление квадратичной нормы вектора. Работает независимо, не обращается к атрибутам класса и локальным аттрибутам экземпляра класса
#         return x*x + y* y
#
#
# v = Vector(10, 20)
# res = Vector.norm2(5, 6)
# print(res)






# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/KV8T8JDtxW4
# Подвиг 6. В программе предполагается реализовать парсер (обработчик) строки с данными string в определенный выходной формат.
# Для этого объявлен следующий класс:
# class Loader:
#     @staticmethod
#     def parse_format(string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
# И предполагается его использовать следующим образом:
# res = Loader.parse_format("4, 5, -6", Factory)
# На выходе (в переменной res) ожидается получать список из набора целых чисел. Например, для заданной строки, должно получиться:
# [4, 5, -6]
# Для реализации этой идеи необходимо вначале программы прописать класс Factory с двумя статическими методами:
# build_sequence() - для создания пустого списка (метод возвращает пустой список);
# build_number(string) - для преобразования строки (string) в целое число (метод возвращает полученное целочисленное значение).
# Объявите класс с именем Factory, чтобы получать на выходе искомый результат.
# P.S. В программе на экран ничего выводить не нужно.

# Здесь объявляется класс Factory

# class Factory:
#     @classmethod
#     def build_sequence(cls):
#         return []
#
#     def build_number(string):
#         return int(string)
#
#
# class Loader:
#     @staticmethod
#     def parse_format(string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
#
#
# # эти строчки не менять!
# res = Loader.parse_format("1, 2, 3, -5, 10", Factory)
# print(res)







#
# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/D02X5B6zLi8
# Подвиг 7. В программе объявлен следующий класс для работы с формами ввода логин/пароль:
# class FormLogin:
#     def __init__(self, lgn, psw):
#         self.login = lgn
#         self.password = psw
#
#     def render_template(self):
#         return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
# Который предполагается использовать следующим образом:
# login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
# html = login.render_template()
# Необходимо прописать классы TextInput и PasswordInput, объекты которых формируются командами:
# login = TextInput(name, size)
# psw = PasswordInput(name, size)
# В каждом объекте этих классов должны быть следующие локальные свойства:
# name - название для поля (сохраняет передаваемое имя, например, "Логин" или "Пароль");
# size - размер поля ввода (целое число, по умолчанию 10).
# Также классы TextInput и PasswordInput должны иметь метод:
# get_html(self) - возвращает сформированную HTML-строку в формате (1-я строка для класса TextInput ; 2-я - для класса PasswordInput):
# <p class='login'><имя поля>: <input type='text' size=<размер поля> />
# <p class='password'><имя поля>: <input type='text' size=<размер поля> />
# Например, для поля login:
# <p class='login'>Логин: <input type='text' size=10 />
# Также классы TextInput и PasswordInput должны иметь метод класса (@classmethod):
# check_name(cls, name) - для проверки корректности переданного имя поля (следует вызывать в инициализаторе) по следующим критериям:
# - длина имени не менее 3 символов и не более 50;
# - в именах могут использоваться только символы русского, английского алфавитов, цифры и пробелы
# Если проверка не проходит, то генерировать исключение командой:
# raise ValueError("некорректное поле name")
# Для проверки допустимых символов в каждом классе должен быть прописан атрибут CHARS_CORRECT:
# CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
# CHARS_CORRECT = CHARS + CHARS.upper() + digits
# По заданию нужно объявить только классы TextInput и PasswordInput с соответствующим функционалом. Более ничего.
# P. S. В данном задании получится дублирование кода в классах TextInput и PasswordInput. На данном этапе - это нормально.

# from string import ascii_lowercase, digits
# #
# # здесь объявляйте классы TextInput и PasswordInput
# class TextInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     @classmethod
#     def check_name(cls, name):
#         return 3 <= len(name) <= 50 and all([i in TextInput.CHARS_CORRECT for i in name])
#
#     def __init__(self, name, size=10):
#         self.name = name
#         self.size = size
#         if self.check_name(self.name):
#             self.get_html()
#         else:
#             raise ValueError("некорректное поле name")
#
#     def get_html(self):
#         return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
#
#
# class PasswordInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     @classmethod
#     def check_name(cls, name):
#         return 3 <= len(name) <= 50 and all([i in TextInput.CHARS_CORRECT for i in name])
#
#     def __init__(self, name, size=10):
#         self.name = name
#         self.size = size
#         if self.check_name(self.name):
#             self.get_html()
#         else:
#             raise ValueError("некорректное поле name")
#
#     def get_html(self):
#         return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
#
#
# class FormLogin:
#     def __init__(self, lgn, psw):
#         self.login = lgn
#         self.password = psw
#
#     def render_template(self):
#         return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
#
#
# эти строчки не менять
# login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
# html = login.render_template()


# ps = PasswordInput('sd', 10)
# print(ps.__dict__)

# TEST

# class TextInput2:
#     def __init__(self, name, size=10):
#         self.name = name
#         self.size = size
#
#     def get_html(self):
#         return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
#
#
# class PasswordInput2:
#     def __init__(self, name, size=10):
#         self.name = name
#         self.size = size
#
#     def get_html(self):
#         return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
#
# f1_1 = TextInput("Login123")
# f1_2 = PasswordInput("Psw")
#
# f2_1 = TextInput2("Login123")
# f2_2 = PasswordInput2("Psw")
#
# f11 = f1_1.get_html().replace(' ', '').replace('\'', '"')
# f12 = f1_2.get_html().replace(' ', '').replace('\'', '"')
# f21 = f2_1.get_html().replace(' ', '').replace('\'', '"')
# f22 = f2_2.get_html().replace(' ', '').replace('\'', '"')











# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/9766M0dS1qc
# Подвиг 8. Объявите класс CardCheck для проверки корректности информации на пластиковых картах. Этот класс должен иметь следующие методы:
# check_card_number(number) - проверяет строку с номером карты и возвращает булево значение True,
# если номер в верном формате и False - в противном случае. Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9).
# check_name(name) - проверяет строку name с именем пользователя карты. Возвращает булево значение True, если имя записано верно
# и False - в противном случае.
# Формат имени: два слова (имя и фамилия) через пробел, записанные заглавными латинскими символами и цифрами. Например, SERGEI BALAKIREV.
# Предполагается использовать класс CardCheck следующим образом (эти строчки в программе не писать):
# is_number = CardCheck.check_card_number("1234-5678-9012-0000")
# is_name = CardCheck.check_name("SERGEI BALAKIREV")
# Для проверки допустимых символов в классе должен быть прописан атрибут:
# CHARS_FOR_NAME = ascii_lowercase.upper() + digits
# Подумайте, как правильнее объявить методы check_card_number и check_name (декораторами @classmethod и @staticmethod).
# P.S. В программе только объявить класс. На экран ничего выводить не нужно.
# from string import ascii_lowercase, digits
#
# class CardCheck:
#     CHARS_FOR_NAME = ascii_lowercase.upper() + digits + '-'
#     DIGITS = digits + '-'
#     def check_card_number(number):
#         '''- проверяет строку с номером карты и возвращает булево значение True, если номер в
#         верном формате и False - в противном случае. Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9)'''
#         # number = number.replace('-', '')
#         return all([i in CardCheck.DIGITS for i in number]) and len(number) == 19 and number[4]==number[9]==number[14]
#
#
#     def check_name(name):
#         '''- проверяет строку name с именем пользователя карты. Возвращает булево значение True,
#         если имя записано верно и False - в противном случае'''
#         return len(name.split()) == 2 and all([i in CardCheck.CHARS_FOR_NAME for i in name.replace(' ', '')])
# is_number = CardCheck.check_card_number("1234-5678-9012-0000")
# is_name = CardCheck.check_name("SERGEI BALAKIREV")
# print(is_number)
# print(is_name)





# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/YkDq9p8n17A
# Подвиг 9. Объявите в программе класс Video с двумя методами:
# create(self, name) - для задания имени name текущего видео (метод сохраняет имя name в локальном атрибуте name объекта класса Video);
# play(self) - для воспроизведения видео (метод выводит на экран строку "воспроизведение видео <name>").
# Объявите еще один класс с именем YouTube, в котором объявите два метода (с декоратором @classmethod):
# add_video(cls, video) - для добавления нового видео (метод помещает объект video класса Video в список);
# play(cls, video_indx) - для проигрывания видео из списка по указанному индексу (индексация с нуля).
# (здесь cls - ссылка на класс YouTube). И список (тоже внутри класса YouTube):
# videos - для хранения добавленных объектов класса Video (изначально список пуст).
# Метод play() класса YouTube должен обращаться к объекту класса Video по индексу списка videos и, затем, вызывать метод play() класса Video.
# Методы add_video и play вызывайте напрямую из класса YouTube. Создавать экземпляр этого класса не нужно.
# Создайте два объекта v1 и v2 класса Video, затем, через метод create() передайте им имена "Python" и "Python ООП".
# После этого с помощью метода add_video класса YouTube, добавьте в него эти два видео и воспроизведите (с помощью метода play класса YouTube) сначала первое, а затем, второе видео.
# Sample Input:
# Sample Output:
# воспроизведение видео Python
# воспроизведение видео Python ООП

# class Video:
#     def create(self, name):
#         '''- для задания имени name текущего видео (метод сохраняет имя name в локальном атрибуте name объекта класса Video);'''
#         self.name = name
#
#     def play(self):
#         '''- для воспроизведения видео (метод выводит на экран строку "воспроизведение видео <name>").'''
#         print(f"воспроизведение видео {self.name}")
#
# class YouTube:
#     lst_video = []
#     @classmethod
#     def add_video(cls, video):
#         '''- для добавления нового видео (метод помещает объект video класса Video в список);'''
#         cls.lst_video.append(video)
#
#     @classmethod
#     def play(cls, video_indx):
#         '''- для проигрывания видео из списка по указанному индексу (индексация с нуля).
#         (здесь cls - ссылка на класс YouTube). И список (тоже внутри класса YouTube):
#         videos - для хранения добавленных объектов класса Video (изначально список пуст).'''
#         cls.lst_video[video_indx].play()
#
#
#
# v1 = Video()
# v2 = Video()
# v1.create('Python')
# v2.create("Python ООП")
# YouTube.add_video(v1)
# YouTube.add_video(v2)
# YouTube.play(0)
# YouTube.play(1)
# print(YouTube.__dict__)






# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/Y4Hvpg4FuKs
# Подвиг 10 (на повторение). Объявите класс AppStore - интернет-магазин приложений для устройств под iOS.
# В этом классе должны быть реализованы следующие методы:
# add_application(self, app) - добавление нового приложения app в магазин;
# remove_application(self, app) - удаление приложения app из магазина;
# block_application(self, app) - блокировка приложения app (устанавливает локальное свойство blocked объекта app в значение True);
# total_apps(self) - возвращает общее число приложений в магазине.
# Класс AppStore предполагается использовать следующим образом (эти строчки в программе не писать):
# store = AppStore()
# app_youtube = Application("Youtube")
# store.add_application(app_youtube)
# store.remove_application(app_youtube)
# Здесь Application - класс, описывающий добавляемое приложение с указанным именем. Каждый объект класса Application
# должен содержать локальные свойства:
# name - наименование приложения (строка);
# blocked - булево значение (True - приложение заблокировано; False - не заблокировано, изначально False).
# Как хранить список приложений в объектах класса AppStore решите сами.
# P.S. В программе нужно только объявить классы с указанным функционалом.

# class AppStore:
#     app_list = []
#
#     def add_application(self, app):
#         '''- добавление нового приложения app в магазин;'''
#         self.app_list.append(app.name)
#
#     def remove_application(self, app):
#         '''- удаление приложения app из магазина;'''
#         self.app_list.remove(app.name)
#
#     def block_application(self, app):
#         '''- блокировка приложения app (устанавливает локальное свойство blocked объекта app в значение True);'''
#         app.blocked = True
#
#     def total_apps(self):
#         '''- возвращает общее число приложений в магазине.'''
#         return len(self.app_list)
# class Application:
#     def __init__(self, name, blocked=False):
#         self.name = name
#         self.blocked = blocked
#
# store = AppStore()
# app_youtube = Application("Youtube")
# store.add_application(app_youtube)
# store.remove_application(app_youtube)
# # print(app_youtube.__dict__)





# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/38QoBSpQqnM
# Подвиг 11 (на повторение). Объявите класс для мессенджера с именем Viber. В этом классе должны быть следующие методы:
# add_message(msg) - добавление нового сообщения в список сообщений;
# remove_message(msg) - удаление сообщения из списка;
# set_like(msg) - поставить/убрать лайк для сообщения msg (т.е. изменить атрибут fl_like объекта msg:
# если лайка нет то он ставится, если уже есть, то убирается);
# show_last_message(число) - отображение последних сообщений;
# total_messages() - возвращает общее число сообщений.
# Эти методы предполагается использовать следующим образом (эти строчки в программе не писать):
# msg = Message("Всем привет!")
# Viber.add_message(msg)
# Viber.add_message(Message("Это курс по Python ООП."))
# Viber.add_message(Message("Что вы о нем думаете?"))
# Viber.set_like(msg)
# Viber.remove_message(msg)
# Класс Message (необходимо также объявить) позволяет создавать объекты-сообщения со следующим набором локальных свойств:
# text - текст сообщения (строка);
# fl_like - поставлен или не поставлен лайк у сообщения (булево значение True - если лайк есть и False - в противном случае, изначально False);
# P.S. Как хранить список сообщений, решите самостоятельно.

# class Viber:
#     lst_messages = []
#
#     @classmethod
#     def add_message(cls, mesg):
#         '''- добавление нового сообщения в список сообщений;'''
#         cls.lst_messages.append(mesg.text)
#
#     @classmethod
#     def remove_message(cls, mesg):
#         ''' - удаление сообщения из списка;'''
#         cls.lst_messages.remove(mesg.text)
#
#     def set_like(self):
#         '''- поставить/убрать лайк для сообщения msg (т.е. изменить атрибут fl_like объекта msg:
#         если лайка нет то он ставится, если уже есть, то убирается);'''
#         self.fl_like = True if self.fl_like is False else False
#
#     def show_last_message(self, count):
#         ''' - отображение последних сообщений;'''
#         (print(i) for i in self.lst_messages[-count:])
#
#     @staticmethod
#     def total_messages():
#         ''' - возвращает общее число сообщений.'''
#         return len(Viber.lst_messages)
#
# class Message:
#     def __init__(self, text, fl_like=False):
#         self.text = text
#         self.fl_like = fl_like
#
# msg = Message("Всем привет!")
# Viber.add_message(msg)
#
# # print(Viber.lst_messages)
# Viber.add_message(Message("Это курс по Python ООП."))
# Viber.add_message(Message("Что вы о нем думаете?"))
# Viber.set_like(msg)
# # print(Viber.lst_messages)
# Viber.remove_message(msg)

