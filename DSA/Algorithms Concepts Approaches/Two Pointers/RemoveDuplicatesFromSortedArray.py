from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        i = 0

        while i < len(nums):
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            nums[p] = nums[i]
            p, i = p + 1, i + 1

        return p

# TC: O(N)
# SC: O(1)
