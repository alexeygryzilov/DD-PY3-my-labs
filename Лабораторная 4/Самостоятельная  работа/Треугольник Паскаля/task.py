from typing import List


def generate(num_rows: int) -> List[List[int]]:

    list_ = []
    for i in range(num_rows):
        nested_list = [1] * (i + 1)
        list_.append(nested_list)

    for i in range(2, len(list_)):
        for j in range(1, len(list_[i]) -1):
            list_[i][j] = list_[i-1][j-1] + list_[i-1][j]
    if list_ is None:
        return None
    return list_

if __name__ == '__main__':
    print(generate(8))