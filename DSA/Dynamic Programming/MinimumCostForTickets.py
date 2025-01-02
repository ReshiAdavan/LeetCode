from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        travelDays = set(days)

        for i in range(1, days[-1] + 1):
            if i not in travelDays:
                dp[i] = dp[i - 1]
                continue

            dp[i] = min(
                dp[max(0, i - 1)] + costs[0],
                dp[max(0, i - 7)] + costs[1],
                dp[max(0, i - 30)] + costs[2]
            )
        return dp[-1]

# TC: O(n)
# SC: O(n)
