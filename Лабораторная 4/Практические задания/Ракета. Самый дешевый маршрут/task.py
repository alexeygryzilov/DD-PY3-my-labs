from typing import List


def rocket_costs(table: List[List[int]]) -> List[List[int]]:
    """

    Просчитать минимальные стоимости маршрутов до каждой клетки с учетом возможных перемещений.


    :param table: Таблица размером N*M, где в каждой клетке дана стоимость перемещения в неё
    :return: Таблицу стоимостей перемещения по клеткам
    """
    ...  # TODO рассчитать таблицу стоимостей перемещений

    n = len(table)
    m = len(table[0])
    cost_ = [[0] * m for i in table]
    cost_[0][0] = table[0][0]
    for j in range(1, m):
        cost_[0][j] = cost_[0][j - 1] + table[0][j]
    for i in range(1, n):
        cost_[i][0] = cost_[i - 1][0] + table[i][0]

    for i in range(1, n):
        for j in range(1, m):
            cost_[i][j] = min(cost_[i - 1][j], cost_[i][j - 1]) + table[i][j]

    return cost_


if __name__ == '__main__':
    costs_ceil = [
        [2, 7, 9, 3],
        [12, 4, 1, 9],
        [1, 5, 2, 5]
    ]
    total_costs = rocket_costs(costs_ceil)
    print(total_costs[-1][-1])  # 21
