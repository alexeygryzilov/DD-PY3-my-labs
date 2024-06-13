from typing import List


def majority_element(nums: List[int]) -> int:
    dict_ = {}
    for number in nums:
        if number in dict_:
            dict_[number] += 1
        else:
            dict_[number] = 1

    max_value = max([value for value in dict_.values()])

    for key, value in dict_.items():
        if value == max_value:
            return key