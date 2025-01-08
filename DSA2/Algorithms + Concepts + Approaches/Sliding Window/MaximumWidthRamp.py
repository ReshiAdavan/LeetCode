from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        maxToTheRight = [0] * len(nums)
        maxToTheRight[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            maxToTheRight[i] = max(maxToTheRight[i + 1], nums[i])

        left = 0
        maxWidth = 0
        for right in range(left + 1, len(nums)):
            while nums[left] > maxToTheRight[right]:
                left += 1
            maxWidth = max(maxWidth, right - left)
        return maxWidth
    
# TC: O(n)
# SC: O(n)
