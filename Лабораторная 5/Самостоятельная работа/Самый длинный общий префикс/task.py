from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    ...
    strs.sort(key=lambda x: len(x))

    result  = set()
    for i in range(len(strs[0])):
        set_ = set()
        for j in range(len(strs)):
            set_.add(strs[j][i])
        if len(set_) == 1:
            result.update(set_)

            if strs[i][j] == strs[i + 1][j]:
                result.add(strs[i][j])
    return (''.join(result))

if __name__ == '__main__':
    print(longest_common_prefix( ["dog","racecar","car"]))