from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        summ = 0
        mini_len = float("inf")

        for right in range(len(nums)):
            summ += nums[right]

            while summ >= target:
                mini_len = min(mini_len, right - left + 1)
                summ -= nums[left]
                left += 1

        return 0 if mini_len == float("inf") else mini_len
    
# TC: O(n)
# SC: O(1)
