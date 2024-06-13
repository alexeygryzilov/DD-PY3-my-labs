from typing import List


def maximum_gap(nums: List[int]) -> int:
    if len(nums) < 2:
        return 0
    nums = sorted(nums)
    delta = []
    print(type(nums))
    for i in range(len(nums) - 1):
        diff = abs(nums[i] - nums[i +1])
        delta.append(diff)
    return max(delta)