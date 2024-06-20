def is_subsequence(s: str, t: str) -> bool:
    if len(s) > len(t):
        s, t = t, s

    list_1 = [_ for _ in s]
    list_2 = [_ for _ in t]
    list_3 = list_2.copy()
    counter = 0

    for i in list_2:
        if i in list_1:
            counter == 1
        if i not in list_1:
            list_3.remove(i)
        if counter == len(list_1):
            list_3 = list_3[:counter]
            break

    return list_3 == list_1


if __name__ == '__main__':
    print(is_subsequence('acb', 'ahbgdc'))
