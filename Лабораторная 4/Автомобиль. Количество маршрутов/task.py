from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    ...  # TODO решить задачу с помощью динамического программирования

    routes = [[0] * m for i in range(n)]

    for j in range( m):
        routes[0][j] = 1
    for i in range(1, n):
        routes[i][0] = 1
    for i in range(1, n):
        for j in range(1, m):
            routes[i][j]  = routes[i -1][j] + routes[i][j - 1] + routes[i -1][j - 1]
    for line in routes:
        print(line)

    return routes


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
