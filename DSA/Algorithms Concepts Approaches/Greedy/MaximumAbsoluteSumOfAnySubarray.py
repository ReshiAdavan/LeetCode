from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        def computeSum(nums):
            prefix = 0
            maxi = nums[0]

            for n in nums:
                if prefix < 0:
                    prefix = 0
                prefix += n
                maxi = max(maxi, prefix)
            return maxi

        negNums = [-n for n in nums]
        posMaxi, negMaxi = computeSum(nums), computeSum(negNums)
        return max(posMaxi, negMaxi)

# TC: O(3n)
# SC: O(1)

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxi, mini = nums[0], nums[0]
        prefixPos, prefixNeg = 0, 0

        for n in nums:
            if prefixPos < 0:
                prefixPos = 0
            prefixPos += n
            maxi = max(maxi, prefixPos)

            if prefixNeg > 0:
                prefixNeg = 0
            prefixNeg += n
            mini = min(mini, prefixNeg)

        return max(maxi, abs(mini))

# TC: O(n)
# SC: O(1)
