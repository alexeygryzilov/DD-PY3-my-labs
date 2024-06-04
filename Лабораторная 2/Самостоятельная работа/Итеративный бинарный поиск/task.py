from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    l_border = 0
    r_border = len(seq) - 1
    middle = (r_border - l_border) //2
    while l_border <= r_border:
        if seq[middle] == value:
            return middle
        elif seq[middle] < value:
            l_border = middle + 1
            middle =( r_border + l_border ) //2
            if seq[middle] == value:
                return middle
        elif seq[middle] > value:
            r_border = middle - 1
            middle = (l_border + r_border) //2
            if seq[value] == middle:
                return middle
    return ValueError("Элемент не найден")

if __name__ == '__main__':
    a=[1,2,2,3,4,5,5,6]
    print(binary_search(5,a))
    ...  # TODO реализовать итеративный алгоритм бинарного поиска