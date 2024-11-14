from typing import List
import math

class Solution(object):
    def maxArea(self, height):
        l, r, A = 0, len(height) - 1, 0
        while l < r:
            A = max(A, (r - l) * (min(height[l], height[r])))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return A

# Beats 82.77% python submissions in runtime
# Beats 77.34% python submissions in memory usage

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        left, right = 0, len(height) - 1

        while left < right:
            waterArea = (right - left) * min(height[left], height[right])
            maxi = max(maxi, waterArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxi

## If container could be slanted 

class Solution:
    def maxSlantedArea(self, height: List[int]) -> int:
        maxi = 0
        left, right = 0, len(height) - 1

        while left < right:
            # Horizontal container area (original calculation)
            horizontal_area = (right - left) * min(height[left], height[right])

            # Slanted container area (using Euclidean distance)
            distance = math.sqrt((right - left) ** 2 + (height[right] - height[left]) ** 2)
            slanted_area = distance * min(height[left], height[right])

            # Compare both areas and update maximum area
            maxi = max(maxi, horizontal_area, slanted_area)

            # Move pointers based on height (similar to the original approach)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxi
