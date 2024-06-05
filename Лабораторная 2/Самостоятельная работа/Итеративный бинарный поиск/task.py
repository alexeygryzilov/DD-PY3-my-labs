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
    middle = (r_border - l_border) // 2
    while l_border <= r_border:
        if seq[middle] == value:
            while seq[l_border] != value:
                l_border += 1
            return l_border
        elif seq[middle] < value:
            l_border = middle + 1
            middle = (r_border + l_border) // 2

        elif seq[middle] > value:
            r_border = middle - 1
            middle = (l_border + r_border) // 2

    raise ValueError("Элемент не найден")


if __name__ == '__main__':
    a = [1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 5, 5, 6]
    print(binary_search(2, a))
    ...  # TODO реализовать итеративный алгоритм бинарного поиска
