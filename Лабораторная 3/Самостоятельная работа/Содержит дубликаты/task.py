from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    dict_ = {}
    for number in nums:
        if number in dict_:
            dict_[number] += 1
        else:
            dict_[number] = 1

    max_value = max([value for value in dict_.values()])
    return max_value >= 2

def contains_duplicate_2(nums: List[int]) -> bool:
    return len(nums) > len(set(nums))