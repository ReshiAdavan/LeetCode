from collections import defaultdict
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1 + dp[j][diff]
                res += dp[j][diff]

        return res

# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# Beats 54.93% of python users in runtime
# Beats 38.51% of python users in memory usage
