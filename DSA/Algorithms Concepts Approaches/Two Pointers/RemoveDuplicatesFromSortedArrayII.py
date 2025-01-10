from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = 2

        for r in range(2, len(nums)):
            if nums[r] != nums[w - 2]:
                nums[w] = nums[r]
                w += 1

        return w

# TC: O(N)
# SC: O(1)
