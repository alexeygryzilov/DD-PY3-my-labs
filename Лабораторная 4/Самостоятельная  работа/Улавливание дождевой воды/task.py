from typing import List


def trap(height: List[int]) -> int:
    volume = 0

    for layer in range(max(height)):
        for i in range(len(height) - 1):
            if height[i + 1] <= layer and height[i] > layer:
                left = i
                rev_height = height[::-1]
                for j in range(len(height) - 1):
                    if rev_height[j + 1] <= layer and rev_height[j] > layer:
                        right = len(height) - 1 - j
                        for k in range(layer + 1):
                            volume += height[left:right + 1].count(k)

                        break
                break
    return volume

if __name__ == '__main__':
    print(trap([4,2,0,3,2,5]))   #9
    print(trap([3,1,2,0,0,0,1,0,2,0,1]))    #11