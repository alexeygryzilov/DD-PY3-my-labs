from typing import Sequence


def binary_search(
        value: int, seq: Sequence[int],
        left_border: int = 0, right_border: int = None) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск
    :param left_border: Левая граница массива, нужна для рекурсивного алгоритма
    :param right_border: Правая граница массива, нужна для рекурсивного алгоритма

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    if right_border is None:
        right_border = len(seq) - 1
    if left_border > right_border:
        raise ValueError("Элемента нет")
    middle: int = (left_border + right_border) // 2
    if seq[middle] == value:
        print(left_border, middle)
        while seq[left_border] != value:
            left_border += 1
        return left_border

    elif seq[middle] < value:
        left_border = middle + 1
        if seq[middle] == value:
            return middle

        else:
            return binary_search(value, seq, left_border, right_border)
    elif seq[middle] > value:
        right_border: int = middle - 1
        if seq[middle] == value:
            return middle
        else:
            return binary_search(value, seq, left_border, right_border)


if __name__ == '__main__':
    print(binary_search(4, [1, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5]))

