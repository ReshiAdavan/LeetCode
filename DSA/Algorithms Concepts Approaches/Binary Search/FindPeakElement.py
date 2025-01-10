from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        left, right = 0, len(nums) - 1

        if nums[left] > nums[left + 1]:
            return left
        if nums[right] > nums[right - 1]:
            return right

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > nums[middle - 1] and nums[middle] > nums[middle + 1]:
                return middle
            elif nums[middle] < nums[middle - 1]:
                right = middle - 1
            else:
                left = middle + 1
        return -1

# Time Complexity: O(log(n))
# Space Complexity: O(1)

