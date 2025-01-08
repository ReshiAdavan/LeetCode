from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0

        for i in range(len(nums)):
            low = lower - nums[i]
            up = upper - nums[i]
            res += (
                self.binarySearch(nums, i + 1, len(nums) - 1, up + 1) -
                self.binarySearch(nums, i + 1, len(nums) - 1, low)
            )
        return res

    def binarySearch(self, nums, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return right

# TC: O(nlogn)
# SC: O(1)
