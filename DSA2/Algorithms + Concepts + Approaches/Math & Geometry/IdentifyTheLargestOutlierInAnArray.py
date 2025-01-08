from typing import List
from collections import Counter

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        counter = Counter(nums)
        outlier = float('-inf')

        # total = sum_of_special_nums + sum_element + outlier
        # total = S + S + outlier
        # total = 2S + outlier
        # in other words, if curTotal was not even, sum_element != sum_of_special_nums

        for x in nums:
            curTotal = total - x
            if curTotal % 2:
                continue

            dividedTotal = curTotal // 2
            counter[x] -= 1
            if counter[dividedTotal] >= 1:
                outlier = max(outlier, x)
            counter[x] += 1
        return outlier

# TC: O(n)
# SC: O(n)
