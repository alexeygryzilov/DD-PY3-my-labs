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

    right_border = len(seq)
    middle: int = (left_border + right_border) // 2

    print('start', left_border, middle, right_border)
    print('---')
    if seq[middle] == value:
        print('yes1')
        return middle
    elif seq[middle] < value:
        print('+')
        left_border = middle + 1
        middle: int = (left_border + right_border) // 2
        print('+', left_border, middle, right_border)

        if seq[middle] == value:
            print('yes2')
            return middle
        else:
            print('++')
            binary_search(value, seq, left_border, right_border)
            print('+', left_border, middle, right_border)
    elif seq[middle] > value:
        print('-')
        right_border: int = middle - 1
        middle = (left_border + right_border) // 2
        print('-', left_border, middle, right_border)

        if seq[middle] == value:
            print('yes3')
            return middle
        else:
            print('--')
            binary_search(value, seq, left_border, right_border)
            print('-', left_border, middle, right_border)


if __name__ == '__main__':
    print(binary_search(1, [1, 2, 3, 4, 5]))
