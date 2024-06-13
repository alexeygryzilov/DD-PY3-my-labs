from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    for j in range(len(container) - 1):
        flag = False
        for i in range(len(container) - 1 - j):
            if container[i] > container[i + 1]:
                container[i], container[i + 1] = container[i + 1], container[i]
                flag = True
        if not flag:
            break

    return container


if __name__ == '__main__':
    a = [i for i in range(10, 0, -1)]
    b = [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]
    c = [3, 3, 3, 3, 3]
    d = []
    assert sort(a) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sort(b) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sort(c) == [3, 3, 3, 3, 3]
    assert sort(d) == []

    # TODO реализовать алгоритм сортировки пузырьком
