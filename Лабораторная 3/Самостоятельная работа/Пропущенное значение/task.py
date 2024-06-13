from typing import List


def missing_number(nums: List[int]) -> int:

    b = {i for i in range(len(nums) + 1)}

    return (b - set(nums)).pop()