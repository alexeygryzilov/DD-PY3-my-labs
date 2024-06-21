from typing import List


def stairway_path(count_stairs: int) -> List[int]:
    """
    Вычислить количество маршрутов до каждой ступени,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param count_stairs: Количество ступеней
    :return: Количество маршрутов до каждой ступени
    """
    ...  # TODO найти количество маршрутов до каждой ступени

    def number(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        return number(n - 1) + number(n - 2)

    result = [number(i) for i in range(count_stairs + 1)]
    return result


def stairway_path_2(count_stairs: int) -> List[int]:
    """
    Вычислить количество маршрутов до каждой ступени,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param count_stairs: Количество ступеней
    :return: Количество маршрутов до каждой ступени
    """
    if count_stairs < 0:
        raise ValueError("Количество ступеней не может быть отрицательным числом")
    if count_stairs == 0:
        return [0]
    if count_stairs == 1:
        return [0, 1]

    list_ = [0] * (count_stairs + 1)
    list_[0] = 0
    list_[1] = 1

    for stair in range(2, count_stairs + 1):
        list_[stair] = list_[stair - 1] + list_[stair - 2]

    return list_


if __name__ == '__main__':
    print(stairway_path(0))  # [0]
    print(stairway_path(5))  # [0, 1, 1, 2, 3, 5]
