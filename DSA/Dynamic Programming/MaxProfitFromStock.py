class Solution:
    def maximumProfit(self, present: list[int], future: list[int], budget: int) -> int:
        dp = {}
        N = len(present)

        def dfs(i, remainingBudget):
            if i >= N:
                return 0
            
            if (i, remainingBudget) in dp:
                return dp[(i, remainingBudget)]

            buyStock = 0
            
            if remainingBudget < present[i]:
                skipStock = dfs(i + 1, remainingBudget)
            else:
                buyStock = future[i] - present[i] + dfs(i + 1, remainingBudget - present[i])
                skipStock = dfs(i + 1, remainingBudget)

            dp[(i, remainingBudget)] = max(buyStock, skipStock)
            return dp[(i, remainingBudget)]

        return dfs(0, budget)