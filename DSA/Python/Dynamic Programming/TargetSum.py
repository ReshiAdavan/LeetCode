class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i, t):
            if (i, t) in cache:
                return cache[(i, t)]
            if i >= len(nums) and t == target:
                cache[(i, t)] = 1
                return cache[(i, t)]
            if i >= len(nums):
                cache[(i, t)] = 0
                return cache[(i, t)]
            
            cache[(i, t)] = dfs(i + 1, t - nums[i]) + dfs(i + 1, t + nums[i])
            return cache[(i, t)]

        return dfs(0, 0)

# Beats 17.64% of users with Python3 in runtime
# Beats 8.34% of users with Python3 in memory