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

## Greedy
## Store and sort differences between B flights to A flights. Take B flights whem it saves you the most. Be greedy on minimizing loss

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costComparison = []
        for costA, costB in costs:
            costComparison.append([costB - costA, costA, costB])
        costComparison.sort()

        N = len(costComparison)

        cost = 0
        for i in range(0, N // 2):
            cost += costComparison[i][2]
        for i in range(N // 2, N):
            cost += costComparison[i][1]
        return cost
    
# TC: O(nlogn)
# SC: O(n)
