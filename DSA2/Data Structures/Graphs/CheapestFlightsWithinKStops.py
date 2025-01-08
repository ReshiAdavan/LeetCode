class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float("inf")] * n
        prices[src] = 0
        for _ in range(k + 1):
            tmpPrices = prices[:]
            for s, d, p in flights:
                if prices[s] != float("inf"):
                    if prices[s] + p < tmpPrices[d]:
                        tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        if prices[dst] == float("inf"): return -1 
        return prices[dst]

# Beats 45.10% python submissions in runtime
# Beats 89.07% python submissions in memory usage