class Solution(object):
    def maxProfit(self, prices):
        x, c = 1, 0
        diff = 0
        while x < len(prices):
            if prices[x] < prices[c]:
                c = x
            diff = max(diff, prices[x] - prices[c])
            x += 1
        return diff

# Beats 75.54% python submissions in runtime
# Beats 30.45% python submissions in memory usage  