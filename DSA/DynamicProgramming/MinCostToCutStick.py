class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        cache = {}
        
        def dfs(l, r):
            if (l, r) in cache:
                return cache[(l, r)]

            if r - l == 1:
                return 0

            res = float("inf")
            for c in cuts: 
                if l < c < r:
                    res = min(r - l + dfs(l, c) + dfs(c, r), res)

            cache[(l, r)] = 0 if res == float("inf") else res
            return cache[(l, r)]

        return dfs(0, n)
    
# Time Complexity: O(N^3)
# Space Complexity: O(N^2)
# Beats 18.55% of python3 users in runtime
# Beats 36.99% of python3 users in memory usage

