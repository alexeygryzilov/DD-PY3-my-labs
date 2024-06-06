def fib_iterative(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя итеративный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """
    if n < 0:
        raise ValueError("n должно быть целым положительным числом!")
    fib_1 = 0
    fib_2 = 1
    if n == 0:
        return fib_1
    if n == 1:
        return fib_2
    for i in range(2, n + 1):
        result = fib_2 + fib_1
        fib_1 = fib_2
        fib_2 = result
    return result


if __name__ == '__main__':
    print(fib_iterative(8))
