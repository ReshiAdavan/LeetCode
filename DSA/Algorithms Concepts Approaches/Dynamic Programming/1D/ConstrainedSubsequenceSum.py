from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        cache = {}
        
        def memo(i):
            if i >= len(nums):
                return -float("inf")
            if i in cache:
                return cache[i]
            
            cur = nums[i]
            maxiNext = 0

            for j in range(1, k + 1):
                maxiNext = max(maxiNext, memo(i + j))
            cache[i] = cur + max(0, maxiNext)
            return cache[i]
        
        return max(memo(i) for i in range(len(nums)))

# TLE
# TC: O(n * k)
# SC: O(n)

from collections import defaultdict, deque
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = defaultdict(list)
        q = deque()
        result = max(nums)

        for i in range(len(nums)):
            while q and q[0] < i - k:
                q.popleft()

            cur = nums[i]
            if q:
                cur += max(0, dp[q[0]])
            dp[i] = cur

            while q and dp[q[-1]] <= dp[i]:
                q.pop()
            q.append(i)

            result = max(result, dp[i])
        return result

# TC: O(n + k)
# SC: O(n)

