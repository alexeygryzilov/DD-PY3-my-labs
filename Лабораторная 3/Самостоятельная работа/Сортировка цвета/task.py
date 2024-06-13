from typing import List
def sort_сolors(nums: List[int]) -> None:
    """
    Ничего не возвращайте, вместо этого измените nums на месте.
    """

    red = []
    white = []
    blue = []
    for i in nums:
        if i == 0:
            red.append(i)
        elif i == 1:
            white.append(i)
        else:
            blue.append(i)
    nums.clear()
    nums = red + white + blue

