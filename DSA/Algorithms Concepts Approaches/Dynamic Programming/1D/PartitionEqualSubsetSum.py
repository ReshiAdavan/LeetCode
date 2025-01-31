from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        cache = {}
        subsetSum = total // 2

        def memo(i, curSum):
            if curSum == subsetSum:
                return True
            if curSum > subsetSum or i >= len(nums):
                return False
            if (i, curSum) in cache:
                return cache[(i, curSum)]

            cache[(i, curSum)] = memo(i + 1, curSum) or memo(i + 1, curSum + nums[i])
            return cache[(i, curSum)]

        return memo(0, 0)

# TC: O(n * sum(nums))
# SC : O(n * sum(nums))
