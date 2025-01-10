from typing import List

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # LIS
        lis = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], 1 + lis[j])

        # LDS
        lds = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    lds[i] = max(lds[i], 1 + lds[j])

        removals = len(nums) - 3
        for p in range(1, len(nums) - 1):
            if lis[p] > 1 and lds[p] > 1:
                removals = min(
                    removals,
                    len(nums) - (lis[p] + lds[p] - 1)
                )
        return removals

# TC: O(n^2)
# SC: O(n)

