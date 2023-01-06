# Испытание "Бремя наследия"
#
# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/M_UctsRbNGA
#
# Всевидящее око начальства увидело, что вы прошли еще одну ступень в постижении глубин ООП языка Python - наследование.
# Вас вновь решили испытать и посмотреть, на что вы действительно способны. Тимлид (Teamleader) с широкой улыбкой протянул вам следующее задание.
# Техническое задание
#
# Необходимо написать универсальную основу для представления ненаправленных связных графов и поиска в них кратчайших маршрутов.
# Далее, этот алгоритм предполагается применять для прокладки маршрутов: на картах, в метро и так далее.
# https://ucarecdn.com/0951c9d3-953b-4a8e-a823-7766c5d69ceb/
# Для универсального описания графов, вам требуется объявить в программе следующие классы:
#
# Vertex - для представления вершин графа (на карте это могут быть: здания, остановки, достопримечательности и т.п.);
# Link - для описания связи между двумя произвольными вершинами графа (на карте: маршруты, время в пути и т.п.);
# LinkedGraph - для представления связного графа в целом (карта целиком).
# https://ucarecdn.com/6527dab4-60c6-4d36-90e1-16e5a4ca5889/
# Объекты класса Vertex должны создаваться командой:
#
# v = Vertex()
#
# и содержать локальный атрибут:
#
# _links - список связей с другими вершинами графа (список объектов класса Link).
#
# Также в этом классе должно быть объект-свойство (property):
#
# links - для получения ссылки на список _links.
#
# Объекты следующего класса Link должны создаваться командой:
#
# link = Link(v1, v2)
#
# где v1, v2 - объекты класса Vertex (вершины графа). Внутри каждого объекта класса Link должны формироваться следующие локальные атрибуты:
#
# _v1, _v2 - ссылки на объекты класса Vertex, которые соединяются данной связью;
# _dist - длина связи (по умолчанию 1); это может быть длина пути, время в пути и др.
#
# В классе Link должны быть объявлены следующие объекты-свойства:
#
# v1 - для получения ссылки на вершину v1;
# v2 - для получения ссылки на вершину v2;
# dist - для изменения и считывания значения атрибута _dist.
#
# Наконец, объекты третьего класса LinkedGraph должны создаваться командой:
#
# map_graph = LinkedGraph()
#
# В каждом объекте класса LinkedGraph должны формироваться локальные атрибуты:
#
# _links - список из всех связей графа (из объектов класса Link);
# # _vertex - список из всех вершин графа (из объектов класса Vertex).
#
# В самом классе LinkedGraph необходимо объявить (как минимум) следующие методы:
#
# def add_vertex(self, v): ... - для добавления новой вершины v в список _vertex (если она там отсутствует);
# def add_link(self, link): ... - для добавления новой связи link в список _links (если объект link с указанными вершинами в списке отсутствует);
# def find_path(self, start_v, stop_v): ... - для поиска кратчайшего маршрута из вершины start_v в вершину stop_v.
#
# Метод find_path() должен возвращать список из вершин кратчайшего маршрута и список из связей этого же маршрута в виде кортежа: 
#
# ([вершины кратчайшего пути], [связи между вершинами])
#
# Поиск кратчайшего маршрута допустимо делать полным перебором с помощью рекурсивной функции (будем полагать,
# что общее число вершин в графе не превышает 100).
# Для тех, кто желает испытать себя в полной мере, можно реализовать алгоритм Дейкстры поиска кратчайшего пути в связном взвешенном графе.
#
# В методе add_link() при добавлении новой связи следует автоматически добавлять вершины этой связи в список _vertex, если они там отсутствуют.
#
# Проверку наличия связи в списке _links следует определять по вершинам этой связи. Например, если в списке имеется объект:
#
# _links = [Link(v1, v2)]
#
# то добавлять в него новые объекты Link(v2, v1) или Link(v1, v2) нельзя (обратите внимание у всех трех объектов будут разные id,
# т.е. по id определять вхождение в список нельзя).
#
# Подсказка: проверку на наличие существующей связи можно выполнить с использованием функции filter() и указанием нужного условия для отбора объектов.
#
# Пример использования классов, применительно к схеме метро (эти строчки в программе писать не нужно):
#
# map_graph = LinkedGraph()
#
# v1 = Vertex()
# v2 = Vertex()
# v3 = Vertex()
# v4 = Vertex()
# v5 = Vertex()
# v6 = Vertex()
# v7 = Vertex()
#
# map_graph.add_link(Link(v1, v2))
# map_graph.add_link(Link(v2, v3))
# map_graph.add_link(Link(v1, v3))
#
# map_graph.add_link(Link(v4, v5))
# map_graph.add_link(Link(v6, v7))
#
# map_graph.add_link(Link(v2, v7))
# map_graph.add_link(Link(v3, v4))
# map_graph.add_link(Link(v5, v6))
#
# print(len(map_graph._links))   # 8 связей
# print(len(map_graph._vertex))  # 7 вершин
# path = map_graph.find_path(v1, v6)
#
# Однако, в таком виде применять классы для схемы карты метро не очень удобно. Например, здесь нет указаний названий станций,
# а также длина каждого сегмента равна 1, что не соответствует действительности.
#
# Чтобы поправить этот момент и реализовать программу поиска кратчайшего пути в метро между двумя произвольными станциями,
# объявите еще два дочерних класса:
#
# class Station(Vertex): ... - для описания станций метро;
# class LinkMetro(Link): ... - для описания связей между станциями метро.
#
# Объекты класса Station должны создаваться командой:
#
# st = Station(name)
#
# где name - название станции (строка). В каждом объекте класса Station должен дополнительно формироваться локальный атрибут:
#
# name - название станции метро.
#
# (Не забудьте в инициализаторе дочернего класса вызывать инициализатор базового класса).
#
# В самом классе Station переопределите магические методы __str__() и __repr__(), чтобы они возвращали название станции метро (локальный атрибут name).
#
# Объекты второго класса LinkMetro должны создаваться командой:
#
# link = LinkMetro(v1, v2, dist)
#
# где v1, v2 - вершины (станции метро); dist - расстояние между станциями (любое положительное число).
#
# (Также не забывайте в инициализаторе этого дочернего класса вызывать инициализатор базового класса).
#
# В результате, эти классы должны совместно работать следующим образом (эти строчки в программе писать не нужно):
#
# map_metro = LinkedGraph()
# v1 = Station("Сретенский бульвар")
# v2 = Station("Тургеневская")
# v3 = Station("Чистые пруды")
# v4 = Station("Лубянка")
# v5 = Station("Кузнецкий мост")
# v6 = Station("Китай-город 1")
# v7 = Station("Китай-город 2")
#
# map_metro.add_link(LinkMetro(v1, v2, 1))
# map_metro.add_link(LinkMetro(v2, v3, 1))
# map_metro.add_link(LinkMetro(v1, v3, 1))
#
# map_metro.add_link(LinkMetro(v4, v5, 1))
# map_metro.add_link(LinkMetro(v6, v7, 1))
#
# map_metro.add_link(LinkMetro(v2, v7, 5))
# map_metro.add_link(LinkMetro(v3, v4, 3))
# map_metro.add_link(LinkMetro(v5, v6, 3))
#
# print(len(map_metro._links))
# print(len(map_metro._vertex))
# path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
# print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
# print(sum([x.dist for x in path[1]]))  # 7
#
# P.S. В программе нужно объявить только классы Vertex, Link, LinkedGraph, Station, LinkMetro. На экран ничего выводить не нужно.


# class Vertex:  # - для представления вершин графа (на карте это могут быть: здания, остановки, достопримечательности и т.п.);
#     def __init__(self):
#         self._links = []
#
#     @property
#     def links(self):
#         return self._links
#
# class Link:  # - для описания связи между двумя произвольными вершинами графа (на карте: маршруты, время в пути и т.п.);
#     def __init__(self, v1, v2):
#         self._v1 = v1
#         self._v2 = v2
#         self._dist = 1
#
#     @property
#     def v1(self):
#         return self._v1
#     @property
#     def v2(self):
#         return self._v2
#     @property
#     def dist(self):
#         return self._dist
#
#
# class LinkedGraph:  # - для представления связного графа в целом (карта целиком).
#     def __init__(self):
#         self._links = []    #_links - список из всех связей графа (из объектов класса Link);
#         self._vertex = []   # _vertex - список из всех вершин графа (из объектов класса Vertex).
#
#     def add_vertex(self, v):    #... - для добавления новой вершины v в список _vertex (если она там отсутствует);
#         if v not in self._vertex:
#             self._vertex.append(v)
#
#     def add_link(self, link):     #... - для добавления новой связи link в список _links (если объект link с указанными вершинами в списке отсутствует);
#         t = tuple(filter(lambda x: (id(x.v1) == id(link.v1) and id(x.v2) == id(link.v2)) or \
#                                     (id(x.v2) == id(link.v1) and id(x.v1) == id(link.v2)), self._links))
#
#         if len(t) == 0:
#             self._links.append(link)
#             self.add_vertex(link.v1)
#             self.add_vertex(link.v2)
#             link.v1.links.append(link)
#             link.v2.links.append(link)
#
#
#     def find_path(self, start_v, stop_v):     #... - для поиска кратчайшего маршрута из вершины start_v в вершину stop_v.
#         self._start_v = start_v
#         self._stop_v = stop_v
#         return self._next(self._start_v, None, [], [])
#
#     def _dist_path(self, links):
#         return sum([x.dist for x in links if x is not None])
#
#     def _next(self, current, link_prev, current_path, current_links):
#         current_path += [current]
#         if link_prev:
#             current_links += [link_prev]
#
#         if current == self._stop_v:
#             return current_path, current_links
#
#         len_path = -1
#         best_path = []
#         best_links = []
#         for link in current.links:
#             path = []
#             links = []
#             if link.v1 not in current_path:
#                 path, links = self._next(link.v1, link, current_path[:], current_links[:])
#             elif link.v2 not in current_path:
#                 path, links = self._next(link.v2, link, current_path[:], current_links[:])
#
#             if self._stop_v in path and (len_path > self._dist_path(links) or len_path == -1):
#                 len_path = self._dist_path(links)
#                 best_path = path[:]
#                 best_links = links[:]
#
#         return best_path, best_links
#
# class Station(Vertex):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def __repr__(self):
#         return self.name
#
# class LinkMetro(Link):
#     def __init__(self, v1, v2, dist):
#         super().__init__(v1, v2)
#         self._dist = dist


# TEST

# map_metro = LinkedGraph()
# v1 = Station("Сретенский бульвар")
# v2 = Station("Тургеневская")
# v3 = Station("Чистые пруды")
# v4 = Station("Лубянка")
# v5 = Station("Кузнецкий мост")
# v6 = Station("Китай-город 1")
# v7 = Station("Китай-город 2")
#
# map_metro.add_link(LinkMetro(v1, v2, 1))
# map_metro.add_link(LinkMetro(v2, v3, 1))
# map_metro.add_link(LinkMetro(v1, v3, 1))
#
# map_metro.add_link(LinkMetro(v4, v5, 1))
# map_metro.add_link(LinkMetro(v6, v7, 1))
#
# map_metro.add_link(LinkMetro(v2, v7, 5))
# map_metro.add_link(LinkMetro(v3, v4, 3))
# map_metro.add_link(LinkMetro(v5, v6, 3))
#
# print(len(map_metro._links))
# print(len(map_metro._vertex))
# path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
# print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
# print(sum([x.dist for x in path[1]]))  # 7




# TESTS

# map2 = LinkedGraph()
# v1 = Vertex()
# v2 = Vertex()
# v3 = Vertex()
# v4 = Vertex()
# v5 = Vertex()
#
# map2.add_link(Link(v1, v2))
# map2.add_link(Link(v2, v3))
# map2.add_link(Link(v2, v4))
# map2.add_link(Link(v3, v4))
# map2.add_link(Link(v4, v5))
#
# assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
# assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"
#
# map2.add_link(Link(v2, v1))
# assert len(map2._links) == 5, "метод add_link() добавил связь Link(v2, v1), хотя уже имеется связь Link(v1, v2)"
#
# path = map2.find_path(v1, v5)
# s = sum([x.dist for x in path[1]])
# assert s == 3, "неверная суммарная длина маршрута, возможно, некорректно работает объект-свойство dist"
#
# assert issubclass(Station, Vertex) and issubclass(LinkMetro, Link), "класс Station должен наследоваться от класса Vertex, а класс LinkMetro от класса Link"
#
# map2 = LinkedGraph()
# v1 = Station("1")
# v2 = Station("2")
# v3 = Station("3")
# v4 = Station("4")
# v5 = Station("5")
#
# map2.add_link(LinkMetro(v1, v2, 1))
# map2.add_link(LinkMetro(v2, v3, 2))
# map2.add_link(LinkMetro(v2, v4, 7))
# map2.add_link(LinkMetro(v3, v4, 3))
# map2.add_link(LinkMetro(v4, v5, 1))
#
# assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
# assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"
#
# path = map2.find_path(v1, v5)
#
# assert str(path[0]) == '[1, 2, 3, 4, 5]', path[0]
# s = sum([x.dist for x in path[1]])
# assert s == 7, "неверная суммарная длина маршрута для карты метро"



# алгоритм Дейкстры ( int - номера гвершин графов, str- вес пути)

# 1 -----'3'-------2
# |\               /
# |  \            /
# |   -'1'--3-'4'/
# '3'     /  \
# |      /    \
# 4     /      |
# |    '5'    '7'
# '2' /        |
# |  /         |
# 6------'4'---5

# можно представить через матрицу смежности(симметричная):
#    1 | 2 | 3 | 4 | 5 | 6
# 1| 0   3   1   3   0   0
# 2| 2   0   4   0   0   0
# 3| 1   4   0   0   7   5
# 4| 3   0   0   0   0   2
# 5| 0   0   7   0   0   4
# 6| 0   0   5   2   4   0

# import math
#
#
# def arg_min(T, S):
#     amin = -1
#     m = math.inf  # максимальное значение
#     for i, t in enumerate(T):
#         if t < m and i not in S:
#             m = t
#             amin = i
#
#     return amin
#
#
# D = ((0, 3, 1, 3, math.inf, math.inf),
#      (3, 0, 4, math.inf, math.inf, math.inf),
#      (1, 4, 0, math.inf, 7, 5),
#      (3, math.inf, math.inf, 0, math.inf, 2),
#      (math.inf, math.inf, 7, math.inf, 0, 4),
#      (math.inf, math.inf, 5, 2, 4, 0))
#
# N = len(D)  # число вершин в графе
# T = [math.inf]*N   # последняя строка таблицы
#
# v = 0       # стартовая вершина (нумерация с нуля)
# S = {v}     # просмотренные вершины
# T[v] = 0    # нулевой вес для стартовой вершины
# M = [0]*N   # оптимальные связи между вершинами
#
# while v != -1:          # цикл, пока не просмотрим все вершины
#     for j, dw in enumerate(D[v]):   # перебираем все связанные вершины с вершиной v
#         if j not in S:           # если вершина еще не просмотрена
#             w = T[v] + dw
#             if w < T[j]:
#                 T[j] = w
#                 M[j] = v        # связываем вершину j с вершиной v
#
#     v = arg_min(T, S)            # выбираем следующий узел с наименьшим весом
#     if v >= 0:                    # выбрана очередная вершина
#         S.add(v)                 # добавляем новую вершину в рассмотрение
#
# print(T, M, sep="\n")
#
# # # формирование оптимального маршрута:
# # start = 0
# # end = 4
# # P = [end]
# # while end != start:
# #     end = M[P[-1]]
# #     P.append(end)
# #
# print(P)




# ANOTHER WAY


class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links

    def get_link(self, v):
        '''Возвращает ребро с другим узлом, если есть'''
        for link in self._links:
            if link.get_v(self) is v:
                return link


class Link:
    def __init__(self, v1, v2, dist=1):
        self._v1 = v1
        self._v2 = v2
        self._dist = dist

    def __eq__(self, other):
        return (self._v1, self._v2) == (other.v1, other.v2) or (self._v1, self._v2) == (other.v2, other.v1)

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value

    def get_v(self, v):
        '''Возвращает второй узел'''
        return (self._v1, self._v2)[v is self.v1]


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
        '''Добавляет узел'''
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        '''Добавляет ребро'''
        if link not in self._links:
            self._links.append(link)
            for v in (link.v1, link.v2):
                self.add_vertex(v)
                v.links.append(link)

    def find_path(self, start_v, stop_v):
        '''Алгоритм Дейкстры'''
        costs = {link.get_v(start_v): link.dist for link in start_v.links}
        parents = dict.fromkeys(costs, start_v)
        processed = {start_v}

        def min_cost():
            return min(tuple(x for x in costs.items() if x[0] not in processed or x[0] == stop_v),
                       key=lambda x: x[1])[0]

        vertex = min_cost()
        while vertex != stop_v:
            cost = costs[vertex]
            for link in vertex.links:  # Перебираем все связи узла
                new_cost = cost + link.dist  # Стоимость с новой связью
                linked_vertex = link.get_v(vertex)  # Получаем узел по связи
                costs.setdefault(linked_vertex, new_cost)  # Добавляем стоимость до него, если нет
                parents.setdefault(linked_vertex, vertex)  # Добавляем его родителя, если нет
                if costs[linked_vertex] > new_cost:  # Если старая стоимость до узла больше
                    costs[linked_vertex] = new_cost  # Назначаем новую стоимость
                    parents[linked_vertex] = vertex  # Указываем нового родителя
            processed.add(vertex)  # Узел обработан
            vertex = min_cost()

        vertices = [stop_v]
        links = []
        while vertex != start_v:
            links.append(vertex.get_link(parents[vertex]))
            vertex = parents[vertex]
            vertices.append(vertex)
        vertices.reverse()
        links.reverse()
        return vertices, links


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    pass

