from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    dict_ = {target - val: idx for idx, val in enumerate(nums)}
    for idx, val in enumerate(nums):
        #print(dict_.get(val), dict_[val])
        if dict_.get(val) and  dict_[val] != idx:
            return [dict_[val], idx]

if __name__ == '__main__':
    print(two_sum([1,2,4], 6))  # [2, 1]
    print(two_sum([1,2,3,4],8)) # None