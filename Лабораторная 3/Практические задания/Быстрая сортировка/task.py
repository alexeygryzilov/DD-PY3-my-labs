from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм быстрой сортировки.

    1. Выбираем опорный элемент. Например, первый элемент.
    2. В левую часть отправляем всё что меньше опорного элемента, в правую всё что больше.
    3. К левой и правой части рекурсивно применяет алгоритм быстрой сортировки.

    :param container: последовательность, которую надо отсортировать
    :return: Отсортированная в порядке возрастания последовательность
    """
    if len(container) <= 1:
        return container
    delimiter = container[len(container) // 2]
    return (sort([item for item in container if item < delimiter]) +
            [item for item in container if item == delimiter] +
            sort([item for item in container if item > delimiter]))


assert sort([]) == []
assert sort([1, 1, 1]) == [1, 1, 1]
assert sort([9, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7,  9]
