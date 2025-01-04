from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        def canMakeBouquets(days):
            bouquets = 0
            flowers = 0
            for day in bloomDay:
                if day <= days:
                    flowers += 1
                    if flowers >= k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m

        lower, upper = min(bloomDay), max(bloomDay)
        days = upper

        while lower <= upper:
            mid = (lower + upper) // 2

            if canMakeBouquets(mid):
                days = mid
                upper = mid - 1
            else:
                lower = mid + 1
        return days

# TC: O(n * log(max(bloomDay) - min(bloomDay)))
# SC: O(1)
