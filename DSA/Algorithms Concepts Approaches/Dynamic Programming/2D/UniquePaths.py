class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1 , -1):
                if i == m - 1:
                    dp[m - 1][j] = 1
                elif j == n - 1:
                    dp[i][n - 1] = 1
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]

# Beats 69.42% of users with Python3 in runtime
# Beats 86.23% of users with Python3 in memory


