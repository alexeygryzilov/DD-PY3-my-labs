from typing import List


def reverse_string(s: List[str]) -> None:
    # left, right = 0, len(s) - 1
    # while left < right:
    #    s[left], s[right] = s[right], s[left]
    #    left, right = left + 1, right - 1

    middle = len(s) // 2
    for i in range(middle):
        s[i], s[-1 - i] = s[-1 - i], s[i]


if __name__ == '__main__':
    a = [i for i in 'hello']
    reverse_string(a)
    print(a)
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    reverse_string(b)
    print(b)
