def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """

    if not isinstance(n, int):
        raise TypeError (f"Паарметр n должен быть целым положительным числом, а не {type(n)} ")
    if n < 0:
        raise ValueError ("Факториал не вычисляется для отрицательных чисел")
    if n == 0:
        return 1
    if n == 1:
        return 1
    return factorial_recursive(n-1) * n
    ...  # TODO реализовать рекурсивный алгоритм нахождения факториала

if __name__ == '__main__':
    print(factorial_recursive(6))
    assert factorial_recursive(5) == 120
    print(factorial_recursive(12.3))
