def is_subsequence(s: str, t: str) -> bool:
    if len(s) > len(t):
        s, t = t, s

    list_1 = [_ for _ in s]
    list_2 = [_ for _ in t]
    list_2_unique = list(dict.fromkeys(list_2))
    list_3 = list_2_unique.copy()

    for i in list_2_unique:
        if i not in list_1:
            list_3.remove(i)

    return list_3 == list_1


if __name__ == '__main__':
    print(is_subsequence('acb', 'ahbcgdbbc'))  # False
