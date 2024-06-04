from collections import deque

from typing import Any


class PriorityQueue:
    HIGH_PRIORITY = 0  # наивысший приоритет
    LOW_PRIORITY = 10  # наименьший приоритет

    # counters = [0 for _ in range(LOW_PRIORITY, HIGH_PRIORITY + 1)]

    def __init__(self):
        self.list_ = []

        self.counters = [0 for _ in range(self.HIGH_PRIORITY, self.LOW_PRIORITY)]
        # print(len(self.counters))
        # print(self.counters)
        ...  # TODO использовать deque для реализации очереди с приоритетами

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Добавление элемент в конец очереди c учетом приоритета

        :param elem: Элемент, который должен быть добавлен
        :param priority: Приоритет добавляемого элемента
        """

        idx = sum(self.counters[:priority + 1])
        self.list_.insert(idx, elem)
        self.counters[priority] += 1
        ...  # TODO реализовать метод enqueue

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        idx = 0
        deque_ = []
        for number in self.counters:
            if number != 0:
                deque_.append(self.list_[idx])
                idx += number
        return deque_


        raise IndexError("Извлечение из пустой очереди")

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди с указанным приоритетом, и т.д.)
        :param priority: Приоритет очереди

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента """

        if type(ind) == int and ind > self.counters[priority] - 1:
            raise IndexError("Индекс вне границы диапазона")
        else:
            try:
                index = ind + sum(self.counters[:priority])
            except TypeError as err:
                print("Неверный тип индекса, должен быть 'str'", err)
                raise
            else:
                elem = self.list_[index]
                return elem

    def clear(self):
        self.list_.clear()

    def __len__(self):
        return len(self.list_)


if __name__ == '__main__':
    myqueue = PriorityQueue()

    print(myqueue.list_)  # []
    myqueue.enqueue(1, 0)
    myqueue.enqueue(2, 0)
    myqueue.enqueue(4, 1)
    myqueue.enqueue(7,4)
    myqueue.enqueue(3, 2)
    myqueue.enqueue(8, 2)
    myqueue.enqueue(15, 1)
    print(myqueue.list_)  # [1, 2, 4, 15, 3, 8, 7]
    print(myqueue.dequeue()) # [1, 4, 3, 7]
    print(myqueue.peek(1, 0))  # 2
    print(myqueue.peek(1, 2))  # 8
    print(myqueue.list_)  # [1, 2, 4, 15, 3, 8, 7]
    print(myqueue.__len__())  # 7
    myqueue.clear()
    print(myqueue.list_)  # []
