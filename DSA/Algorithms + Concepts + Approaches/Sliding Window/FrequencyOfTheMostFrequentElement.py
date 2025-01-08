from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        total = 0
        maxF = 1

        for right in range(len(nums)):
            total += nums[right]
            while nums[right] * (right - left + 1) > total + k:
                total -= nums[left]
                left += 1
            maxF = max(maxF, right - left + 1)
        return maxF

# TC: O(nlogn)
# SC: O(1)
