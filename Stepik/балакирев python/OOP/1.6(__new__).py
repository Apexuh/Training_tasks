# class Point:
#     def __new__(cls, *args, **kwargs):
#         print('Вызов __new__ для', str(cls))
#         return super().__new__(cls)     #без возврата init не вызывался бы
#
#     def __init__(self, x=0, y=0):
#         print('Вызов __init__ для', str(self))
#         self.x = x
#         self.y = y
#
# d = Point(1,3)


# Паттерн проектирования Singleton: должен создаваться только один экземпляр класса
# class DataBase:
#     __instance = None   #ссылка на экземпляр класса
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance   #если экземпляр класса не существует(none), то ему будет присвоен адрес нового созданного
#         # обьекта через базовый класс super в условии if. если условие не выполнится(то есть обьект уже создан), то будет
#         # возвращен адрес ранее созданного обьекта. Таким образом будет контроль за тем,что в программе ровно один обьект класса.
#         # Также требуется финализатор del, который будет снова присваивать значение None. То есть при проходе сборщика мусора
#         # у нас появится возможность снова создать обьект класса
#     def __del__(self):
#         DataBase.__instance = None  # то есть
#     def __init__(self, user, psw, port):
#         self.user = user
#         self.psw = psw
#         self.port = port
#
#     def connect(self):
#         print(f'Connecting to DB : {self.user}, {self.psw}, {self.port}')
#
#     def close(self):
#         print(f'Closing connection')
#
#     def read(self):
#         return 'data from DB'
#
#     def write(self, data):
#         print(f'Writing {data} to DB')
#
#
# db1 = DataBase('root', '1234', 80)
# db2 = DataBase('root2', '5678', 40)
# print(id(db1), id(db2))     #4340791760 4340791760 - id меняются, но самое важное,что они равны. То есть при повторном
# # создании обьекта класса ничего создано не было. То есть db2 ссылается на тот же обьект.
# db1.connect()
# db2.connect()   # это минус такого варианта, тк при создании данные из второй бд заменили данные первой





# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/7aVqWfrAdqw
# Подвиг 6. Объявите класс AbstractClass, объекты которого нельзя было бы создавать. При выполнении команды:
# obj = AbstractClass()
# переменная obj должна ссылаться на строку с содержимым:
# "Ошибка: нельзя создавать объекты абстрактного класса"
# P.S. В программе объявить только класс, выводить на экран ничего не нужно.

# class AbstractClass:
#     def __new__(cls, *args, **kwargs):
#         return 'Ошибка: нельзя создавать объекты абстрактного класса'
#
#
# obj = AbstractClass()
# print(obj)





# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/uE1uf7Qtbh4
# Подвиг 7. Объявите класс SingletonFive, с помощью которого можно было бы создавать объекты командой:
# a = SingletonFive(<наименование>)
# Здесь <наименование> - это данные, которые сохраняются в локальном свойстве name созданного объекта.
# Этот класс должен формировать только первые пять объектов. Остальные (шестой, седьмой и т.д.) должны быть ссылкой на последний (пятый) созданный объект.
# Создайте первые десять объектов класса SingletonFive с помощью следующего фрагмента программы:
# objs = [SingletonFive(str(n)) for n in range(10)]
# P.S. В программе на экран ничего выводить не нужно.

# class SingletonFive:
#     __cnt = 0
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__cnt < 5:
#             cls.__instance = super().__new__(cls)
#             cls.__cnt += 1
#         return cls.__instance
#     def __init__(self, name):
#         self.name = name
#
#
# objs = [SingletonFive(str(n)) for n in range(10)]





# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/sX_uP7GVqkc
# Подвиг 8. В программе объявлена переменная TYPE_OS и два следующих класса:
# TYPE_OS = 1 # 1 - Windows; 2 - Linux
# class DialogWindows:
#     name_class = "DialogWindows"
# class DialogLinux:
#     name_class = "DialogLinux"
# Необходимо объявить третий класс с именем Dialog, который бы создавал объекты командой:
# dlg = Dialog(<название>)
# Здесь <название> - это строка, которая сохраняется в локальном свойстве name объекта dlg.
# Класс Dialog должен создавать объекты класса DialogWindows, если переменная TYPE_OS = 1 и объекты класса DialogLinux,
# если переменная TYPE_OS не равна 1. При этом, переменная TYPE_OS может меняться в последующих строчках программы. Имейте это в виду, при объявлении класса Dialog.
# P.S. В программе на экран ничего выводить не нужно. Только объявить класс Dialog.


# TYPE_OS = 1 # 1 - Windows; 2 - Linux
# class DialogWindows:
#     name_class = "DialogWindows"
# class DialogLinux:
#     name_class = "DialogLinux"
#
# class Dialog:
#     def __new__(cls, *args, **kwargs):
#         obj = None
#         if TYPE_OS == 1:
#             obj = super().__new__(DialogWindows)
#         else:
#             obj = super().__new__(DialogLinux)
#         obj.__dict__['name'] = args[0]
#         return obj
#
#
# dlg = Dialog('post')
# print(dlg.__dict__)





# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/U4zwfmbEiCI
# Подвиг 9 (на повторение материала). Объявите класс Point для представления точек на плоскости.
# Создавать объекты этого класса предполагается командой:
# pt = Point(x, y)
# Здесь x, y - числовые координаты точки на плоскости (числа), то есть, в каждом объекте этого класса создаются
# локальные свойства x, y, которые хранят конкретные координаты точки.
# Необходимо в классе Point реализовать метод clone(self), который бы создавал новый объект класса
# Point как копию текущего объекта с локальными атрибутами x, y и соответствующими значениями.
# Создайте в программе объект pt класса Point и еще один объект pt_clone через вызов метода clone.
# P.S. В программе на экран ничего выводить не нужно.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        class Poin(Point):
            def __init__(self):
                self.x = Point.i
pt = Point(10,20)
print(pt.__dict__)
