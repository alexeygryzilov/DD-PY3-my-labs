from typing import Sequence


def bubble_sort(container: Sequence[int]) -> Sequence[int]:
    for j in range(len(container) - 1):
        flag = False
        for i in range(len(container) - 1 - j):
            if container[i] > container[i + 1]:
                container[i], container[i + 1] = container[i + 1], container[i]
                flag = True
        if not flag:
            break

    return container


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    sorted_container = []
    dict_ = {}
    for i in container:
        if i in dict_:
            dict_[i] += 1
        else:
            dict_[i] = 1
    dict_keys = [key for key in dict_.keys()]
    for key in bubble_sort(dict_keys):
        sorted_container += [key] * dict_[key]

    return sorted_container


if __name__ == '__main__':
    a = [1, 1, 41, 4, 4, 4, 45, 61, 2, 2, 2, 3, 3, 3, 4, 4, 3, 3, 3, 45, 4, 5, 5]
    c = []
    d = [1, 1, 1]
    assert sort(a) == [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 41, 45, 45, 61]
    assert sort(c) == []
    assert sort(d) == [1, 1, 1]
