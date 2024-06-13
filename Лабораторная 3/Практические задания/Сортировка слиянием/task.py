from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм сортировки слиянием.

    1. Если массив состоит из 1 элемента – он отсортирован
    2. Иначе массив разбивается на две части, которые сортируются рекурсивно
    3. После сортировки двух частей массива к ним применяется процедура слияния

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if not container:
        return container

    def merge(left_part: List[int], right_part: List[int]) -> List[int]:

        result = []
        while True:
            if left_part[0] <= right_part[0]:
                item = left_part.pop(0)
                result.append(item)
            else:
                item = right_part.pop(0)
                result.append(item)
            if not left_part:
                result += right_part
                break
            if not right_part:
                result += left_part
                break
        return result

    if len(container) == 1:
        return container
    middle_idx = len(container) // 2
    new_left_part = sort(container[: middle_idx])
    new_right_part = sort(container[middle_idx:])
    return merge(new_left_part, new_right_part)


assert sort([]) == []
assert sort([1]) == [1]
assert sort([6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6]
