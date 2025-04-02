from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        candyCount = sum(candies)
        if k > candyCount:
            return 0

        lower, upper = 1, candyCount // k

        def canAllocate(numCandies):
            piles = 0
            for c in candies:
                piles += (c // numCandies)
            return piles >= k

        while lower <= upper:
            mid = (lower + upper) // 2
            if canAllocate(mid):
                res = mid
                lower = mid + 1
            else:
                upper = mid - 1
        return res

## Let n rep. # of candies
# TC: O(n * log(sum(candies) // k))
# SC: O(1)
