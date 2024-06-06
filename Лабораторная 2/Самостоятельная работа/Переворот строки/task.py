from typing import List


def reverse_string(s: List[str]) -> None:
    #left, right = 0, len(s) - 1
    #while left < right:
    #    s[left], s[right] = s[right], s[left]
    #    left, right = left + 1, right - 1

    m = len(s) // 2
    s[:m], s[-1:-m - 1:-1] = s[-1:-m - 1:-1], s[:m]



if __name__ == '__main__':
    a = [i for i in 'hello']
    reverse_string(a)
    print(a)

