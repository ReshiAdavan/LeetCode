from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        ans = -float("inf")
        for j in range(k):
            sum = 0
            for i in range(j, len(prefix_sum) - k, k):
                sum = max(
                    prefix_sum[i + k] - prefix_sum[i],
                    sum + prefix_sum[i + k] - prefix_sum[i]
                )
                ans = max(ans, sum)

        return ans

# TC: O(N*K)
# SC: O(N)
