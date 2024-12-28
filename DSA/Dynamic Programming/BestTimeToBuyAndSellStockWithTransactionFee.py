from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cache = {}

        def memo(i, isBuy):
            if i >= len(prices):
                return 0
            if (i, isBuy) in cache:
                return cache[(i, isBuy)]

            A = B = C = D = -float("inf")

            if isBuy:
                A = -prices[i] + memo(i + 1, not isBuy)

            B = memo(i + 1, isBuy)

            if not isBuy:
                C = prices[i] - fee + memo(i + 1, not isBuy)

            D = memo(i + 1, isBuy)

            cache[(i, isBuy)] = max(A, B, C, D)
            return cache[(i, isBuy)]

        return memo(0, True)

# TC: O(n)
# SC: O(n)
