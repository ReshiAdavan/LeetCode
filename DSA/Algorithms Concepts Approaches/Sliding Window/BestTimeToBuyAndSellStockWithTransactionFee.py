from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]

        for i in range(1, len(prices)):
            # If not holding stock, either not hold or sell
            cash = max(cash, hold + prices[i] - fee)

            # If holding stock, either keep holding or buy
            hold = max(hold, cash - prices[i])

        return cash
    
# TC: O(n)
# SC: O(1)
