class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [0 for i in range(amount + 1)]
        if not amount: return dp[0]
        for i in range(1, amount + 1):
            if i in coins: dp[i] = 1
            else:
                mini = float("inf")
                for coin in coins:
                    if coin < i: mini = min(mini, dp[coin] + dp[i - coin]) 
                dp[i] = mini
        if dp[amount] == float("inf"): return -1
        return dp[amount]

# Beats 46.35% of users with Python3 in runtime
# Beats 90.61% of users with Python3 in memory

