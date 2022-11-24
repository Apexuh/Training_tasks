# односвязный список: head(start) -->data-->next--> null(end)
# двусвязный список: null(start) --> data1(prev:null, next:data2)--> data2(prev:data1, next:null)-->null
# кольцевой двусвязный список: head--> data1(next:data2)-->data2(next:data1)--> back to data1


class Box:
    def __init__(self, cat=None):
        self.cat = cat
        self.nextcat = None

    def __str__(self):
        return f'{self.cat} --> next: {self.nextcat}'


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return str(self.head)

    def length(self):
        temp = self.head  #присваивание temp = первому элементу
        counter = 0     #счетчик
        while temp:   #пока temp не None(то есть конец списка), то цикл выполняется
            counter += 1
            temp = temp.nextcat   #присваивание temp = temp next, то есть следующий цикл "ныряет" в следующее значение
        return counter
# cat1 = Box(1)
# print(cat1)
# cat2 = Box(2)
# cat1.nextcat = cat2 #1 --> next: 2 --> next: None
# cat1.nextcat = cat2.cat # выше и этот вариант разные. При запуске в этом варианте срабатывает 1 --> next: 2, выше же
# # запускается благодаря методу стр проход по связаным элементам
# print(cat1)

if __name__ == '__main__':
    linked_list = LinkedList()
    temp = Box(1)
    linked_list.head = temp  #временный элемент ,которому присваивается первое значение из класса выше
    for i in range(2, 5):
        temp.nextcat = Box(i)   #присваиваем 1 элементу next = следующему элементу
        temp = temp.nextcat   #и меняем текущий temp на следующий
    print(linked_list)
    print(linked_list.length())