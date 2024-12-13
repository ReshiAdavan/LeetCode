from typing import List
from math import ceil

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def validator(limit):
            storesNeeded = 0
            for q in quantities:
                storesNeeded += ceil(q / limit)
            return storesNeeded <= n

        lower, upper = 1, sum(quantities)
        minimax = upper
        while lower <= upper:
            mid = (lower + upper) // 2
            if validator(mid):
                minimax = mid
                upper = mid - 1
            else:
                lower = mid + 1

        return minimax

## m is sum(quantities)
# TC: O(nlogm)
# SC: O(1)
