def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """

    count = 0

    for item in brackets_row:

        if count == 0 and item == ')':
            return False
            break
        if item == '(':
            count += 1
            brackets_row = brackets_row[1:]
        elif item == ')':
            count -= 1
            brackets_row = brackets_row[1:]
        else:
            brackets_row = brackets_row[1:]
    return count == 0



if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
