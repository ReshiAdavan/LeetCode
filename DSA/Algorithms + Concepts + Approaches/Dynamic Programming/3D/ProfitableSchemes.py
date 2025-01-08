class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        numCrimes = len(group)
        cache = {}
        M = 10**9 + 7

        def dfs(i, m, p):
            if m < 0:
                return 0
            p = min(p, minProfit)
            if i >= numCrimes:
                return p >= minProfit
            if (i, m, p) in cache:
                return cache[(i, m, p)]
            cache[(i, m, p)] = (dfs(i + 1, m, p) + dfs(i + 1, m - group[i], p + profit[i])) % M
            return cache[(i, m, p)]

        return dfs(0, n, 0)

# Time Complexity: O(len(group) * n * minProfit)
# Space Complexity: O(len(group) * n * minProfit)
# Beats 12.71% of python users in runtime
# Beats 31.27% of python users in memory usage

