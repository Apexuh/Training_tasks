# Испытание магией
#
# Видео-разбор (решение смотреть только после своей попытки): https://youtu.be/1dSxnEFfDu8
#
# Вы прошли магические методы. Начальство оценило вашу стойкость, рвение и решило дать вам испытание для подтверждения уровня полученных навыков.
# Вам выпала великая честь создать полноценную программу игры в "Крестики-нолики". И вот перед вами текст с заданием самого испытания.
# Техническое задание
#
# Необходимо объявить класс с именем TicTacToe (крестики-нолики) для управления игровым процессом. Объекты этого класса будут создаваться командой:
#
# game = TicTacToe()
#
# В каждом объекте этого класса должен быть публичный атрибут:
#
# pole - двумерный кортеж, размером 3x3.
#
# Каждый элемент кортежа pole является объектом класса Cell:
#
# cell = Cell()
#
# В объектах этого класса должно автоматически формироваться локальное свойство:
#
# value - текущее значение в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.
#
# Также с объектами класса Cell должна выполняться функция:
#
# bool(cell) - возвращает True, если клетка свободна (value = 0) и False - в противном случае.
#
# К каждой клетке игрового поля должен быть доступ через операторы:
#
# res = game[i, j] # получение значения из клетки с индексами i, j
# game[i, j] = value # запись нового значения в клетку с индексами i, j
#
# Если индексы указаны неверно (не целые числа или числа, выходящие за диапазон [0; 2]), то следует генерировать исключение командой:
#
# raise IndexError('некорректно указанные индексы')
#
# Чтобы в программе не оперировать величинами: 0 - свободная клетка; 1 - крестики и 2 - нолики, в классе TicTacToe должны быть
# три публичных атрибута (атрибуты класса):
#
# FREE_CELL = 0      # свободная клетка
# HUMAN_X = 1        # крестик (игрок - человек)
# COMPUTER_O = 2     # нолик (игрок - компьютер)
#
# В самом классе TicTacToe должны быть объявлены следующие методы (как минимум):
#
# init() - инициализация игры (очистка игрового поля, возможно, еще какие-либо действия);
# show() - отображение текущего состояния игрового поля (как именно - на свое усмотрение);
# human_go() - реализация хода игрока (запрашивает координаты свободной клетки и ставит туда крестик);
# computer_go() - реализация хода компьютера (ставит случайным образом нолик в свободную клетку).
#
# Также в классе TicTacToe должны быть следующие объекты-свойства (property):
#
# is_human_win - возвращает True, если победил человек, иначе - False;
# is_computer_win - возвращает True, если победил компьютер, иначе - False;
# is_draw - возвращает True, если ничья, иначе - False.
#
# Наконец, с объектами класса TicTacToe должна выполняться функция:
#
# bool(game) - возвращает True, если игра не окончена (никто не победил и есть свободные клетки) и False - в противном случае.
#
# Все эти функции и свойства предполагается использовать следующим образом (эти строчки в программе не писать):
#
# game = TicTacToe()
# game.init()
# step_game = 0
# while game:
#     game.show()
#
#     if step_game % 2 == 0:
#         game.human_go()
#     else:
#         game.computer_go()
#
#     step_game += 1
#
#
# game.show()
#
# if game.is_human_win:
#     print("Поздравляем! Вы победили!")
# elif game.is_computer_win:
#     print("Все получится, со временем")
# else:
#     print("Ничья.")
#
# Вам в программе необходимо объявить только два класса: TicTacToe и Cell так,
# чтобы с их помощью можно было бы сыграть в "Крестики-нолики" между человеком и компьютером.
# P.S. Запускать игру и выводить что-либо на экран не нужно. Только объявить классы.
# P.S.S. Домашнее задание: завершите создание этой игры и выиграйте у компьютера хотя бы один раз.


# ==============================================
from random import randint
class TicTacToe:
    FREE_CELL = 0      # свободная клетка
    HUMAN_X = 1        # крестик (игрок - человек)
    COMPUTER_O = 2     # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = [[Cell(self.FREE_CELL)] * 3 for _ in range(3)]

    def init(self):
        self.__init__()

    def show(self):
        for row in self.pole:
            print(list(map(lambda x: '-' if x.value == 0 else '0' if x.value == 2 else 'X', row)))

    def human_go(self):
        s = input('Please input coords for your step (example: "1 2") ===>  ')
        s = tuple(map(int, s.split()))
        i, j = self.__check_index(s)
        if self.pole[i][j].value == 0:
            self.pole[i][j].value = self.HUMAN_X
        else:
            self.human_go()

    def computer_go(self):
        x, y = randint(0,2), randint(0,2)
        if self.pole[x][y].value != 0:
            self.computer_go()
        self.pole[x][y].value = 2

    @staticmethod
    def __check_index(index):
        x, y = index
        if type(x) != int or type(y) != int or x < 0 or x > 2 or y < 0 or y > 2:
            raise IndexError('некорректно указанные индексы')
        return x, y

    def __setitem__(self, key, value):
        i, j = self.__check_index(key)
        self.pole[i][j].value = value

    def __getitem__(self, item):
        i, j = self.__check_index(item)
        return self.pole[i][j].value

    def someone_win(self, x):
        if x == 0:
            return x
        a = any(list(map(lambda row: all(list(map(lambda i: i.value == x, row))), self.pole)))
        b = any(list(map(lambda row: all(list(map(lambda i: i.value == x, row))), zip(*self.pole))))
        c = all(list(map(lambda i: i == x, [self.pole[i][i].value for i in range(3)])))
        d = all(list(map(lambda i: i == x, [self.pole[i][-i - 1].value for i in range(3)])))
        s = any([a, b, c, d])
        return s

    def __str__(self):
        return str(list(map(lambda row: list(map(lambda x: x.value, row)), self.pole)))

    @property
    def is_human_win(self):
        return self.someone_win(self.HUMAN_X)

    @property
    def is_computer_win(self):
        return self.someone_win(self.COMPUTER_O)

    @property
    def is_draw(self):
        return self.is_computer_win == self.is_human_win != False


class Cell:
    def __init__(self, value=0):
        self.value = value

    def __bool__(self):
        return self.value == 0




# =============================================

# TESTS



cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"
#
game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
# game.someone_win(0)
game.init()
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"
#
game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"
print(game)






# ----------------------------------

# ANOTHER WAY
class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        '''Инициализация'''
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]
        self.free_cells = 9
        self.winner = None
        self.diagonals = [[self.pole[i][i] for i in range(3)], [self.pole[-i-1][i] for i in range(-3, 0)]]
        for diag in self.diagonals:
            for cell in diag:
                cell._priority += 2

    def __getitem__(self, coords):
        '''Геттер значения клетки по координатам'''
        if self._valid_coords(*coords):
            return self.pole[coords[0]][coords[1]].value
        raise IndexError('некорректно указанные индексы')

    def __setitem__(self, coords, value):
        '''Сеттер значения клетки по координатам'''
        if not self._valid_coords(*coords):
            raise IndexError('некорректно указанные индексы')
        if value in (0, 1, 2):
            self.pole[coords[0]][coords[1]].value = value
        self.__bool__()

    def __bool__(self):
        '''Проверка окончена игра или нет'''
        for row in self.pole:
            if not any(row) and len(set(row)) == 1:
                self.winner = row[0].value
                return False
        for col in zip(*self.pole):
            if not any(col) and len(set(col)) == 1:
                self.winner = col[0].value
                return False
        for diag in self.diagonals:
            if not any(diag) and len(set(diag)) == 1:
                self.winner = diag[0].value
                return False
        if self.free_cells == 0:
            self.winner = 0
            return False
        return True

    @property
    def is_human_win(self):
        return self.winner == self.HUMAN_X

    @property
    def is_computer_win(self):
        return self.winner == self.COMPUTER_O

    @property
    def is_draw(self):
        return self.winner == 0

    @classmethod
    def _valid_coords(cls, y, x):
        '''Проверка координат'''
        return type(y) == type(x) == int and 0 <= y < 3 and 0 <= x < 3

    def init(self):
        self.__init__()

    def human_go(self):
        '''Ход человека'''
        while True:
            print('Введите координаты свободной клетки через пробел:')
            coords = input()
            if len(coords.split()) != 2:
                print('Было введено неверное количество координат.')
                continue
            try:
                y, x = map(int, coords.split())
                if not self._valid_coords(y, x):
                    print('Введённые координаты вне диапазона поля.')
                    continue
            except ValueError:
                print('Введённые данные не являются координатами.')
                continue
            if self.pole[y][x]:
                self.pole[y][x].value = self.HUMAN_X
                self.free_cells -= 1
                self._compute_priority(y, x)
                break
            else:
                print('Выбранная клетка занята.')
                continue

    def computer_go(self):
        '''Ход компьютера'''
        free_cells = [(y, x) for y, row in enumerate(self.pole) for x, cell in enumerate(row) if cell]
        y, x = max(free_cells, key=lambda c: self.pole[c[0]][c[1]]._priority)
        if y == x == 1:  # Реакция на среднюю клетку
            for cell in (self.pole[0][1], self.pole[1][0], self.pole[1][2], self.pole[2][1]):
                cell._priority += 2
        self.free_cells -= 1
        self.pole[y][x].value = self.COMPUTER_O

    def _compute_priority(self, y, x):
        '''Просчёт хода компьютера'''
        # Реакция на ход противника
        for cell in self.pole[y]:
            cell._priority -= 1
        for cell in list(zip(*self.pole))[x]:
            cell._priority -= 1
        if y == x:
            for cell in self.diagonals[0]:
                cell._priority -= 1
        if y + x == 2:
            for cell in self.diagonals[1]:
                cell._priority -= 1
        # Корректировка опасности
        for row in self.pole + [list(lst) for lst in zip(*self.pole)] + self.diagonals:
            counter = [0, 0, 0]
            for cell in row:
                counter[cell.value] += 1
            if counter[1] == 2:
                for cell in row:
                    cell._priority = 5
            if counter[2] == 2:
                for cell in row:
                    cell._priority = 6

    def show(self):
        '''Отрисовка поля'''
        for row in self.pole:
            for cell in row:
                print(cell, end=' ')
            print()
        print('* ' * 10)


class Cell:
    def __init__(self):
        self.value = 0
        self._priority = 2

    def __bool__(self):
        return not self.value

    def __str__(self):
        if self.value == 1:
            return 'X'
        if self.value == 2:
            return '0'
        return '-'

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)