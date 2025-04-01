from math import floor, sqrt
from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        lower, upper = 1, min(ranks) * cars * cars
        res = upper

        def repairAllCars(mid):
            count = 0
            for r in ranks:
                count += floor(sqrt((mid // r)))
            return count >= cars

        while lower <= upper:
            mid = (lower + upper) // 2
            if repairAllCars(mid):
                res = mid
                upper = mid - 1
            else:
                lower = mid + 1
        return res

## Let n rep. # of ranks  
# TC: O(n * log(cars * cars * min(ranks)))
# SC: O(1)
