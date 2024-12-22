from typing import List
from collections import heapq

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        sellBacklog = []
        buyBacklog = []
        MOD = 10**9 + 7

        for price, quantity, orderType in orders:
            if orderType == 0:  # Buy order
                while quantity > 0 and sellBacklog and sellBacklog[0][0] <= price:
                    minSellPrice, sellQuantity = heapq.heappop(sellBacklog)
                    if sellQuantity > quantity:
                        heapq.heappush(sellBacklog, [minSellPrice, sellQuantity - quantity])
                        quantity = 0
                    else:
                        quantity -= sellQuantity
                if quantity > 0:
                    heapq.heappush(buyBacklog, [-price, quantity])
            else:  # Sell order
                while quantity > 0 and buyBacklog and -buyBacklog[0][0] >= price:
                    maxBuyPrice, buyQuantity = heapq.heappop(buyBacklog)
                    if buyQuantity > quantity:
                        heapq.heappush(buyBacklog, [maxBuyPrice, buyQuantity - quantity])
                        quantity = 0
                    else:
                        quantity -= buyQuantity
                if quantity > 0:
                    heapq.heappush(sellBacklog, [price, quantity])

        totalBacklog = sum(q for _, q in sellBacklog) + sum(q for _, q in buyBacklog)
        return totalBacklog % MOD

# TC: average case O(nlog(n)), worst case O(n^2 * log⁡n)
# SC: O(n)
