from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sumIndexMap = {0: -1}
        maxi = 0
        currSum = 0

        for i, num in enumerate(nums):
            currSum += -1 if num == 0 else 1

            if currSum in sumIndexMap:
                maxi = max(maxi, i - sumIndexMap[currSum])
            else:
                sumIndexMap[currSum] = i
        return maxi

# O(n)
# O(n)
