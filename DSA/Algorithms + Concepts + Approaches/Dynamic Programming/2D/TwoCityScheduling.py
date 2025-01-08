from typing import List

## Recursive Memoization

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cache = {}

        def memo(i, balance):
            if i >= len(costs) and balance != 0:
                return float("inf")
            elif i >= len(costs):
                return 0
            if (i, balance) in cache:
                return cache[(i, balance)]

            A = costs[i][0] + memo(i + 1, balance - 1)
            B = costs[i][1] + memo(i + 1, balance + 1)

            cache[(i, balance)] = min(A, B)
            return cache[(i, balance)]

        return memo(0, 0)

# TC: O(n^2)
# SC: O(n^2)

