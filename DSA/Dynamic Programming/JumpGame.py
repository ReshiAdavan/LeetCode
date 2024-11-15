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

## Greedy

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalPost = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goalPost:
                goalPost = i
        return True if not goalPost else False  

# TC: O(n)
# SC: O(1)
