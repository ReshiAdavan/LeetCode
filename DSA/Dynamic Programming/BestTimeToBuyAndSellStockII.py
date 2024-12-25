from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def memo(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in cache:
                return cache[(i, buy)]

            A = B = C = D = float("-inf")

            # buy
            if buy:
                A = -prices[i] + memo(i + 1, not buy)

            # dont buy
            B = memo(i + 1, buy)

            # sell
            if not buy:
                C = prices[i] + memo(i + 1, not buy)

            # dont sell
            D = memo(i + 1, buy)

            cache[(i, buy)] = max(A, B, C, D)
            return cache[(i, buy)]

        return memo(0, True)


# TC: O(n)
# SC: O(n)
