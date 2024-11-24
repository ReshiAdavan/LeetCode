from typing import List

class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        dp = {}
        N = len(present)

        def dfs(i, remainingBudget):
            if i >= N:
                return 0
            
            if (i, remainingBudget) in dp:
                return dp[(i, remainingBudget)]

            if remainingBudget < present[i]:
                dp[(i, remainingBudget)] = max(0, dfs(i + 1, remainingBudget))
                
            else:
                dp[(i, remainingBudget)] = max(
                    future[i] - present[i] + dfs(i + 1, remainingBudget - present[i]), 
                    dfs(i + 1, remainingBudget)
                )

            return dp[(i, remainingBudget)]

        return dfs(0, budget)

## MLE
# TC: O(n*budget)
# SC: O(n*budget)

class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        n = len(present)
        dp = [0] * (budget + 1)

        for i in range(n):
            profit = future[i] - present[i]
            cost = present[i]
            for b in range(budget, cost - 1, -1):
                dp[b] = max(dp[b], dp[b - cost] + profit)
        return dp[budget]
    
# TC: O(n*budget)
# SC: O(budget)
