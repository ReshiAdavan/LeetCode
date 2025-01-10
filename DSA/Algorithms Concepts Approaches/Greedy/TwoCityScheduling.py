## Greedy
## Store and sort differences between B flights to A flights. Take B flights whem it saves you the most. Be greedy on minimizing loss

from typing import List
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
