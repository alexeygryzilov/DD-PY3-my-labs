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
        if n == 0 or n == 1:
            return 1
        return number(n - 1) + number(n - 2)

    result = [number(i) for i in range(count_stairs + 1)]
    return result


if __name__ == '__main__':
    print(stairway_path(2))  # [0]
    print(stairway_path(5))  # [0, 1, 1, 2, 3, 5]
