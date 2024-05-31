"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        """
        self.list_ = []  # TODO инициализировать список

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self.list_.append(elem)# TODO реализовать метод enqueue

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        try:
            elem = self.list_.pop(0)
        except IndexError as err:
            print("Очередь пуста:"
                  , err)
            raise
        else:
            return elem# TODO реализовать метод dequeue

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        try:
            elem = self.list_[ind]
        except TypeError as err:
            print("Индекс должен быть целым числом: ", err)
            raise
        except IndexError as err:
            print("Индекс вне граиц очереди: ", err)
            raise
        else:
            return elem# TODO реализовать метод peek

    def clear(self) -> None:
        """ Очистка очереди. """
        self.list_.clear()  # TODO реализовать метод clear

    def __len__(self):

        """ Количество элементов в очереди. """
        return (len(self.list_))  # TODO реализовать метод __len__

if __name__ == '__main__':
    a = Queue()
    a.enqueue(1)
    a.enqueue(2)
    print(a.__len__())
    #print(a.peek('alfa'))
    a.clear()

    print(a.list_)
