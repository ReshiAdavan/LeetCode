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

