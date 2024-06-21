from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    ...  # TODO реализовать прямой метод расчета
    stairs = len(stairway)

    if stairs == 1:
        return stairway[0]
    if stairs == 2:
        return stairway[1]

    cost = [0] * stairs
    cost[0] = stairway[0]
    cost[1] = stairway[1]

    for stair in range(2, stairs):
        cost[stair] = min(cost[stair - 1], cost[stair - 2]) + stairway[stair]

    return cost[-1]

if __name__ == '__main__':
    print(stairway_path([1, 3, 1, 5]))  # 7