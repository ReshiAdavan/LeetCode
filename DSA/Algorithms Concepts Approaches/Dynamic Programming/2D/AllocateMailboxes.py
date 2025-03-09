from typing import List

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses.sort()
        costs = {}

        def cost(i, j):
            if (i, j) in costs:
                return costs[(i, j)]

            median = houses[(i + j) // 2]
            total = sum(abs(houses[idx] - median) for idx in range(i, j + 1))
            costs[(i, j)] = total
            return total

        memo = {}

        def dp(i, j):
            if i < 0:
                return 0
            if j == 0:
                return float('inf')
            if (i, j) in memo:
                return memo[(i, j)]

            result = float('inf')
            for t in range(i, -1, -1):
                if t > 0:
                    result = min(result, dp(t - 1, j - 1) + cost(t, i))
                else:
                    result = min(result, cost(0, i))
            memo[(i, j)] = result
            return result

        return dp(n - 1, k)

# TC: O(n^2 * k)
# SC: O(n^2 * k)