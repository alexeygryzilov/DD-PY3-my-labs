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

    def one_search(value, seq,l_border =0, r_border = len(seq)):
        print('---')

        middle = (r_border + l_border) // 2
        print(l_border, middle, r_border, seq)
        if seq[middle] == value:
            print('yes1', middle)
            return middle
        elif seq[middle] < value:
            print('<',middle, seq, seq[middle])
            l_border = middle
            middle = (r_border + l_border) // 2
            if seq[middle] == value:
                print('yes2', middle)
                return middle
            else:

                one_search(value, seq, l_border, r_border)
                print("next")

        elif seq[middle] > value:

            print('>',middle,seq, seq[middle])
            r_border = middle
            middle = (l_border + r_border) // 2
            if seq[middle] == value:
                print('yes3', middle)
                return middle
            else:
                one_search(value, seq, l_border, r_border)
                print('next')


    return one_search(value, seq)


if __name__ == '__main__':
    print(binary_search(1, [1,2,3,6,8,10,12]))