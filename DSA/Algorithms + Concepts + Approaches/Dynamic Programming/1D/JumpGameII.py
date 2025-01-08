from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf") for _ in range(len(nums))]
        dp[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            farthestJump = min(i + nums[i], len(nums) - 1)
            if i + 1 <= farthestJump:
                dp[i] = 1 + min(dp[i + 1: farthestJump + 1])
        return dp[0]


# TC: O(n*m) 
# SC: O(n)

