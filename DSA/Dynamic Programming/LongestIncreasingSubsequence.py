from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}

        def dfs(idx, prev):
            if idx >= len(nums):
                return 0
            
            if (idx, prev) in cache:
                return cache[(idx, prev)]
            
            skip = dfs(idx + 1, prev)
            take = 0
            if nums[idx] > prev:
                take = 1 + dfs(idx + 1, nums[idx])

            cache[(idx, prev)] = max(take, skip)
            return cache[(idx, prev)]

        return dfs(0, float("-inf"))

### Memory Limit Exceeded
# Time Complexity: O(n^2)
# Space Complexity: O(n)

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)


# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Beats 49% of python users in runtime
# Beats 74.19% of python users in memory usage

from bisect import bisect_left
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        
        dp = []
        for num in nums:
            pos = bisect_left(dp, num)
            if pos == len(dp):
                dp.append(num)
            else:
                dp[pos] = num
            
        return len(dp)
    
# Time Complexity: O(nlog(n))
# Space Complexity: O(n)
# Beats 100% of python users in runtime (runs in 0ms lol)
# Beats 74.19% of python users in memory usage
