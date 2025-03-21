from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        maxi = 0
        mask = 0

        for right in range(len(nums)):
            while left < right and mask & nums[right] != 0:
                mask ^= nums[left]
                left += 1

            mask |= nums[right]
            maxi = max(maxi, right - left + 1)

        return maxi

# TC: O(N)
# SC: O(1)
