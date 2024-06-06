from typing import List


def reverse_string(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1


if __name__ == '__main__':
    a = [i for i in 'hello']
    reverse_string(a)
    print(a)
    b = []
    print(reverse_string(b))
