
# Посвящение в ООП

# Вы прошли серию испытаний и совершили множество подвигов, чтобы лицом к лицу столкнуться с настоящим вызовом, достойным лишь избранных!
# Для подтверждения своих знаний и навыков вам предлагается пройти этап посвящения в объектно-ориентированное программирование.
# И вот задание, которое выпало на вашу долю.
#
# Руководство компании целыми днями не знает куда себя деть. Поэтому они решили дать задание своим программистам написать
# программу игры "Морской бой". Но эта игра будет немного отличаться от классической. Для тех, кто не знаком с этой древней,
# как мир, игрой, напомню ее краткое описание.
#
# Каждый игрок у себя на бумаге рисует игровое поле 10 х 10 клеток и расставляет на нем десять кораблей: однопалубных - 4;
# двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1.
#
# https://ucarecdn.com/47c71b81-ff5d-4d16-b6ab-a566a14d2242/
#
# Корабли расставляются случайным образом, но так, чтобы не выходили за пределы игрового поля и не соприкасались друг с другом
# (в том числе и по диагонали).
#
# Затем, игроки по очереди называют клетки, куда производят выстрелы. И отмечают эти выстрелы на другом таком же поле в 10 х 10 клеток,
# которое представляет поле соперника. Соперник при этом должен честно отвечать: "промах", если ни один корабль не был задет и "попал",
# если произошло попадание. Выигрывает тот игрок, который первым поразит все корабли соперника.
#
# Но это была игра из глубокого прошлого. Теперь же, в компьютерную эру, корабли на игровом поле могут перемещаться в
# направлении своей ориентации на одну клетку после каждого хода соперника, если в них не было ни одного попадания.
#
# Итак, лично вам поручается сделать важный фрагмент этой игры - расстановку и управление кораблями в этой игре. А само задание звучит так.
# Техническое задание
#
# В программе необходимо объявить два класса:
#
# Ship - для представления кораблей;
# GamePole - для описания игрового поля.
# Класс Ship
#
# Класс Ship должен описывать корабли набором следующих параметров:
#
# https://ucarecdn.com/250c5cd8-3534-454f-af88-c58dd60977b4/
#
# x, y - координаты начала расположения корабля (целые числа);
# length - длина корабля (число палуб: целое значение: 1, 2, 3 или 4);
# tp - ориентация корабля (1 - горизонтальная; 2 - вертикальная).
''''''
# Объекты класса Ship должны создаваться командами:
#
# ship = Ship(length)
# ship = Ship(length, tp)
# ship = Ship(length, tp, x, y)
#
# По умолчанию (если не указывается) параметр tp = 1, а координаты x, y равны None.
#
# В каждом объекте класса Ship должны формироваться следующие локальные атрибуты:
#
# _x, _y - координаты корабля (целые значения в диапазоне [0; size), где size - размер игрового поля);
# _length - длина корабля (число палуб);
# _tp - ориентация корабля;
# _is_move - возможно ли перемещение корабля (изначально равно True);
# _cells - изначально список длиной length, состоящий из единиц (например, при length=3, _cells = [1, 1, 1]).
#
# Список _cells будет сигнализировать о попадании соперником в какую-либо палубу корабля. Если стоит 1, то попадания не было, а если стоит значение 2, то произошло попадание в соответствующую палубу.
#
# При попадании в корабль (хотя бы одну его палубу), флаг _is_move устанавливается в False и перемещение корабля по игровому полю прекращается.
#
# В самом классе Ship должны быть реализованы следующие методы (конечно, возможны и другие, дополнительные):
#
# set_start_coords(x, y) - установка начальных координат (запись значений в локальные атрибуты _x, _y);
# get_start_coords() - получение начальных координат корабля в виде кортежа x, y;
# move(go) - перемещение корабля в направлении его ориентации на go клеток (go = 1 - движение в одну сторону на клетку; go = -1 - движение в другую сторону на одну клетку); движение возможно только если флаг _is_move = True;
# is_collide(ship) - проверка на столкновение с другим кораблем ship (столкновением считается, если другой корабль или пересекается с текущим или просто соприкасается, в том числе и по диагонали); метод возвращает True, если столкновение есть и False - в противном случае;
# is_out_pole(size) - проверка на выход корабля за пределы игрового поля (size - размер игрового поля, обычно, size = 10); возвращается булево значение True, если корабль вышел из игрового поля и False - в противном случае;
#
# С помощью магических методов __getitem__() и __setitem__() обеспечить доступ к коллекции _cells следующим образом:
#
# value = ship[indx] # считывание значения из _cells по индексу indx (индекс отсчитывается от 0)
# ship[indx] = value # запись нового значения в коллекцию _cells
''''''
# Класс GamePole
#
# Следующий класс GamePole должен обеспечивать работу с игровым полем. Объекты этого класса создаются командой:
#
# pole = GamePole(size)
#
# где size - размеры игрового поля (обычно, size = 10).
#
# В каждом объекте этого класса должны формироваться локальные атрибуты:
#
# _size - размер игрового поля (целое положительное число);
# _ships - список из кораблей (объектов класса Ship); изначально пустой список.
#
# В самом классе GamePole должны быть реализованы следующие методы (возможны и другие, дополнительные методы):
#
# init() - начальная инициализация игрового поля; здесь создается список из кораблей (объектов класса Ship): однопалубных - 4; двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1 (ориентация этих кораблей должна быть случайной).
#
# Корабли формируются в коллекции _ships следующим образом: однопалубных - 4; двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1. Ориентация этих кораблей должна быть случайной. Для этого можно воспользоваться функцией randint следующим образом:
#
# [Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), ...]
#
# Начальные координаты x, y не расставленных кораблей равны None.
#
# После этого, выполняется их расстановка на игровом поле со случайными координатами так, чтобы корабли не пересекались между собой.
#
# get_ships() - возвращает коллекцию _ships;
# move_ships() - перемещает каждый корабль из коллекции _ships на одну клетку (случайным образом вперед или назад) в направлении ориентации корабля; если перемещение в выбранную сторону невозможно (другой корабль или пределы игрового поля), то попытаться переместиться в противоположную сторону, иначе (если перемещения невозможны), оставаться на месте;
# show() - отображение игрового поля в консоли (корабли должны отображаться значениями из коллекции _cells каждого корабля, вода - значением 0);
#
# get_pole() - получение текущего игрового поля в виде двумерного (вложенного) кортежа размерами size x size элементов.
''''''
# Пример отображения игрового поля:
#
# 0 0 1 0 1 1 1 0 0 0
# 1 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 1 0 0 1
# 0 0 0 0 1 0 1 0 0 1
# 0 0 0 0 0 0 1 0 0 0
# 1 1 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 1 0 0 0
# 0 1 1 1 1 0 0 0 0 0
# 0 0 0 0 0 0 0 1 1 0

# Пример использования классов (эти строчки в программе не писать):
#
# SIZE_GAME_POLE = 10
#
# pole = GamePole(SIZE_GAME_POLE)
# pole.init()
# pole.show()
#
# pole.move_ships()
# print()
# pole.show()
#
# В программе требуется только объявить классы Ship и GamePole с соответствующим функционалом. На экран выводить ничего не нужно.
#
# P.S. Для самых преданных поклонников программирования и ООП. Завершите эту программу, добавив еще один класс SeaBattle для управления игровым процессом в целом. Игра должна осуществляться между человеком и компьютером. Выстрелы со стороны компьютера можно реализовать случайным образом в свободные клетки. Сыграйте в эту игру и выиграйте у компьютера.



from random import randint

class Ship:
    def __init__(self, length,  tp=1, x=None, y=None):
        self._x = x #start coord
        self._y = y #start coord
        self._length = length # length of ship (1,2,3 or 4)
        self._tp = tp    #ship orientation(1 - horizontal, 2- vertical)
        self._is_move = True #True if ship can move
        self._cells = [1] * self._length #1 if part of ship is unbroken, 2 -this part is broken

    def set_start_coords(self, x, y):  # - установка начальных координат (запись значений в локальные атрибуты _x, _y);
        self._x = x
        self._y = y

    def get_start_coords(self): # - получение начальных координат корабля в виде кортежа x, y;
        return self._x, self._y

    def move(self, go):  #- перемещение корабля в направлении его ориентации на go клеток (go = 1 - движение в одну сторону на клетку; go = -1 - движение в другую сторону на одну клетку); движение возможно только если флаг _is_move = True;
        if self._is_move:
            if self._tp == 1:
                self._x += go
            else:
                self._y += go

    def is_collide(self, ship): # - проверка на столкновение с другим кораблем ship (столкновением считается, если другой корабль или пересекается с текущим или просто соприкасается, в том числе и по диагонали); метод возвращает True, если столкновение есть и False - в противном случае;
        if self._x is not None and self._y is not None and ship._x is not None and ship._y is not None:
            return len(set(self.is_collide_location()) & set(ship.ship_position())) != 0
        return False

    def is_collide_location(self):
        s01 = []
        for i in self.ship_position():
            for x in range(i[0] - 1, i[0] + 2):
                for y in range(i[1] - 1, i[1] + 2):
                    if (x, y) not in s01 and 0 <= x and 0 <= y:
                        s01.append((x, y))
        return s01

    def is_out_pole(self, size): # - проверка на выход корабля за пределы игрового поля (size - размер игрового поля, обычно, size = 10); возвращается булево значение True, если корабль вышел из игрового поля и False - в противном случае;
        hor, vert = 0, 0    #дополнительные параметры (в зависимости от направления судна).
        if self._tp == 1: # если горизонтально расположено судно, то х максимальная меняется
            hor = self._length
        else:
            vert = self._length
        if self._x < 0 or self._y < 0 or self._x + hor >= size or self._y + vert >= size:
            return True
        return False

    def ship_position(self):
        start_x, start_y = self._x, self._y
        if self._tp == 1:
            end_x, end_y = start_x + self._length, start_y + 1
        else:
            end_x, end_y = start_x + 1, start_y + self._length
        s = [(i, j) for i in range(start_x, end_x) for j in range(start_y, end_y)]
        return s

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value


class GamePole:
    def __init__(self, size=10):
        self._size = size
        self._ships = []
        self.__name = None

    def init(self):
        count_ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        self._ships = [Ship(i, tp=randint(1, 2)) for i in count_ships]
        self.istallation_ships()


    def istallation_ships(self):
        i = 0
        while i < 10:
            ship = self._ships[i]
            x = randint(0, self._size)
            y = randint(0, self._size)
            ship.set_start_coords(x, y)
            if ship.is_out_pole(self._size): # проверка выхода за поле
                continue

            s = []
            for boat in self._ships:   # проход по списку из судов, если есть пересечение с каким-то судном, то запуск генерации заново
                if ship == boat:
                    continue
                else:
                    s.append(ship.is_collide(boat))
            if any(s):
                continue
            # self._pole[y][x] = ship
            i += 1



    def get_ships(self):    # - возвращает коллекцию _ships;
        return self._ships

    def move_ships(self):
        '''- перемещает каждый корабль из коллекции _ships на одну клетку (случайным образом вперед или назад) в
        направлении ориентации корабля; если перемещение в выбранную сторону невозможно (другой корабль или пределы игрового поля),
         то попытаться переместиться в противоположную сторону, иначе (если перемещения невозможны), оставаться на месте;'''
        for ship in self._ships:
            temp_coords = ship.get_start_coords()
            if ship._is_move:
                ship.move(1)
                any_list_collide = [ship.is_collide(boat) for boat in self._ships if ship != boat]
                if any(any_list_collide) or ship.is_out_pole(self._size):
                    ship.move(-2)
                    any_list_collide = [ship.is_collide(boat) for boat in self._ships if ship != boat]
                    if any(any_list_collide) or ship.is_out_pole(self._size):
                        ship.set_start_coords(*temp_coords)
                        ship._is_move = False



    def show(self):
        '''- отображение игрового поля в консоли (корабли должны отображаться значениями из коллекции _cells каждого корабля, вода - значением 0);'''
        s = '\n'.join(tuple(map(lambda x: ' '.join(tuple(map(str, x))), self.get_pole())))
        print(s)



    def get_pole(self):
        '''- получение текущего игрового поля в виде двумерного (вложенного) кортежа размерами size x size элементов.'''
        self._pole = [[0] * self._size for _ in range(self._size)]
        for ship in self._ships:
            for i, coords in enumerate(ship.ship_position()):
                x, y = coords
                value = ship._cells[i]
                self._pole[y][x] = value
        self._pole = tuple(map(lambda x: tuple(x), self._pole))
        return self._pole

    def take_shot(self, x, y):
        if type(x) != int or type(y) != int or x < 0 or y < 0 or x >= self._size or x >= self._size:
            raise ValueError
        for boat in self._ships:
            if (x, y) in boat.ship_position():
                boat._cells[boat.ship_position().index((x, y))] = 2
                ship_is_broken = all(list(map(lambda x: x == 2, boat._cells)))
                if ship_is_broken:
                    print(f'A ship with {boat._length} deck(s) was destroyed')
                    print(f'{boat._length} ships left')
                    self._ships.remove(boat)
                else:
                    print(f'There was a hit on the ship')
                break




# RUN
SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
pole.show()

pole.move_ships()
print()
pole.show()
pole.take_shot(1,2)






# MY TESTS
# s1 = Ship(3) #horizontal
# assert s1._cells == [1, 1, 1]
# s1.set_start_coords(9, 5)
# assert s1.ship_position() == [(9, 5), (10, 5), (11, 5)]
# assert s1.is_out_pole(10) == True

# s = Ship(4, 2) #vertical
# s.set_start_coords(3, 7)
# assert s.ship_position() == [(3, 7), (3, 8), (3, 9), (3, 10)]
# assert s.is_out_pole(10) == True
#
# s2 = Ship(4)
# s3 = Ship(4)
# s4 = Ship(4)
# assert s2._cells == [1, 1, 1, 1]
# s2.set_start_coords(3, 3)
# s3.set_start_coords(3, 4)
# s4.set_start_coords(3, 5)
#
# # print(s4.ship_position())
# print(s2.is_collide(s3))
# print(s2.is_collide(s4))


# s5 = Ship(3)
# s5.set_start_coords(1, 1)
# print(s5.ship_position())
# print(s5.is_collide_location())
#
# s6 = Ship(3,2)
# s6.set_start_coords(1, 1)
# print(s6.ship_position())
# print(sorted(s6.is_collide_location(),key=lambda x: x[0]))
''''''

# TESTS
# ship = Ship(2)
# ship = Ship(2, 1)
# ship = Ship(3, 2, 0, 0)
#
# assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
# assert ship._cells == [1, 1, 1], "неверный список _cells"
# assert ship._is_move, "неверное значение атрибута _is_move"
# #
# ship.set_start_coords(1, 2)
# assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
# assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"
# #
# ship.move(1)
# s1 = Ship(4, 1, 0, 0)
# s2 = Ship(3, 2, 0, 0)
# s3 = Ship(3, 2, 0, 2)
# # print(s1.ship_position())
# # print(s1.is_collide_location())
# # print(s3.ship_position())
# # print(s3.is_collide_location())
# # print(s1.is_collide(s3))
#
# assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
# assert s1.is_collide(
#     s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"
#
# s2 = Ship(3, 2, 1, 1)
# assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"
#
# s2 = Ship(3, 1, 8, 1)
# assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"
#
# s2 = Ship(3, 2, 1, 5)
# assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"
#
# s2[0] = 2
# # print(s2[0])
# assert s2[0] == 2, "неверно работает обращение ship[indx]"
#
#
#
# p = GamePole(10)
# p.init()
# # print(*p._pole, sep='\n')
# #
# #
# # print(p.get_ships())
# # print(p.get_ships()[0].is_collide(s2))
#
# for nn in range(5):
#     for s in p._ships:
#         assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"
# #
#         for ship in p.get_ships():
#             if s != ship:
#                 assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
#     p.move_ships()
#     # print(*p._pole, sep='\n')
#
# # print('============================================')
# gp = p.get_pole()
# # print(gp)
# # print(p.show())
# assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
# assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"
#
# pole_size_8 = GamePole(8)
# pole_size_8.init()



