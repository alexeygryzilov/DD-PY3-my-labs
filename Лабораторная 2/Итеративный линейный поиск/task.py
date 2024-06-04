"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    idx = 0
    min_ = arr[0]
    for i  in range(1, len(arr)):
        if arr[i] < min_:
            min_ = arr[i]
            idx = i
    return idx

     # TODO реализовать итеративный линейный поиск

