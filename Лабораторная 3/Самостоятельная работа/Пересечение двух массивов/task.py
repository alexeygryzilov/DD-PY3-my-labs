from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    result = []
    for number in nums1:
        if number in nums2 and number not in result:
            result.append(number)
    return result

def intersection_2(nums1: List[int], nums2: List[int]) -> List[int]:
    set_1 = {item for item in nums1}
    set_2 = {item for item in nums2}

    return list(set_1.intersection(set_2))


print( intersection_2([1, 2, 2, 1], [2, 2]))
