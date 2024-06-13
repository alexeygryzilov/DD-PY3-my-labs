from collections import Counter
def is_anagram(s: str, t: str) -> bool:

    count_1 = Counter(s)
    count_2 = Counter(t)
    return count_1 == count_2

def is_anagram_2(s: str, t: str) -> bool:

    dict_ = {}
    for i in s:
        if i in dict_:
            dict_[i] += 1
        else:
            dict_[i] = 1
    for j in t:
        if j in dict_:
            dict_[j] -= 1
        else:
            dict_[j] = 1

    result = sum([abs(value) for value in dict_.values()])
    return result == 0

