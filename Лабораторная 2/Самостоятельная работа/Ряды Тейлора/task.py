from typing import Union
from itertools import count
from math import factorial

DELTA = 0.000001


def sin_tay(x, n):
    result = x ** (2 * n - 1) * (-1) ** (n - 1) / factorial(2 * n - 1)
    return result


def sin_tay_2(x, n):
    if n == 1:
        return x
    else:
        return sin_tay_2(x, n - 1) * (-1) ** (n - 1) / ((2 * n - 1) * (2 * n - 2))


def sinx(x: Union[int, float]) -> float:
    """
    Вычисление sin(x) с помощью разложения в ряд Тейлора

    :param x: x значение в радианах
    :return: значение sin(x)
    """
    n = 1
    result = 0
    while abs(sin_tay(x, n)) >= DELTA:
        result += sin_tay(x, n)
        n += 1
    return result


if __name__ == '__main__':
    print(sinx(1))  # 0.8414710097001764
