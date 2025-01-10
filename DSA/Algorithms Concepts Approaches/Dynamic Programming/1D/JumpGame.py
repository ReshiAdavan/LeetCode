from typing import List

## Tabular DP

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums))]
        dp[-1] = True

        for j in range(len(nums) - 2, -1, -1):
            jumps = nums[j]
            for k in range(j + 1, min(j + jumps + 1, len(nums))):
                if dp[k]:
                    dp[j] = True
                    break
        return dp[0]

# TC: O(n*n)
# SC: O(n)

