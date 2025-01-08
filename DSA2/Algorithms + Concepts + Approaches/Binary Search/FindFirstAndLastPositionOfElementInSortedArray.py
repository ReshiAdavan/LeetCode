from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        return [self.binary_search_left(nums, target), self.binary_search_right(nums, target)]

    def binary_search_left(self, nums, target):
        left, right = 0, len(nums) - 1
        leftmost = -1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                leftmost = middle
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return leftmost

    def binary_search_right(self, nums, target):
        left, right = 0, len(nums) - 1
        rightmost = -1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                rightmost = middle
                left = middle + 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return rightmost

# TC: O(log(n))
# SC: O(1)
