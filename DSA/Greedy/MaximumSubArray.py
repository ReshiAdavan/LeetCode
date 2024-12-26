from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runningSum = 0
        maxSubArrayRes = nums[0]

        for n in nums:
            if runningSum < 0:
                runningSum = 0
            runningSum += n
            maxSubArrayRes = max(maxSubArrayRes, runningSum)

        return maxSubArrayRes

# TC: O(N)
# SC: O(1)