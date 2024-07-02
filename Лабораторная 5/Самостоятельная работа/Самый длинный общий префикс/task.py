from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    ...
    strs.sort(key=lambda x: len(x))


    result_ = []
    for i in range(len(strs[0])):
        set_ = set()
        for j in range(len(strs)):
            set_.add(strs[j][i])
        if len(set_) == 1:
            result_.append(strs[j][i])



    return (''.join(result_))


if __name__ == '__main__':
    print(longest_common_prefix(["flowers", "flow", "fly"]))
