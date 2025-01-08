class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) == len(t):
            if s == t:
                return 1
            else: 
                return 0
        dp = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]

            if s[i] == t[j]:
                dp[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else: 
                dp[(i, j)] = dfs(i + 1, j)
            return dp[(i, j)]

        return dfs(0, 0)

# Beats 48.46% of users with Python3 in runtime
# Beats 34.57% of users with Python3 in memory

