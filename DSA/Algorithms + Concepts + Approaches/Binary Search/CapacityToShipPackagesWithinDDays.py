from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lower, upper = max(weights), sum(weights)
        result = upper

        def canShip(capacity):
            ships, currCap = 1, capacity
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    currCap = capacity
                currCap -= w
            return ships <= days

        while lower <= upper:
            middle = (lower + upper) // 2

            # adjust upper
            if canShip(middle):
                result = min(result, middle)
                upper = middle - 1

            # adjust lower
            else:
                lower = middle + 1
                
        return result
    
# Time Complexity: O(n * log(m)))
# Space Complexity: O(1)
# Beats 100% of python users in runtime (it runs in 0ms lol)
# Beats 99.97% of python users in memory usage
