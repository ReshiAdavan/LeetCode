class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]

            res = -1

            # right
            if j + 1 < len(matrix[0]) and matrix[i][j + 1] > matrix[i][j]: 
                res = max(1 + dfs(i, j + 1), res)
            # left
            if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]: 
                res = max(1 + dfs(i, j - 1), res)
            # down
            if i + 1 < len(matrix) and matrix[i + 1][j] > matrix[i][j]: 
                res = max(1 + dfs(i + 1, j), res)
            # up
            if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]: 
                res = max(1 + dfs(i - 1, j), res)

            if res == -1: 
                dp[i][j] = 1
                return 1
            else: 
                dp[i][j] = res
                return res
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j)
        return max(max(row) for row in dp)

# Beats 96.30% of users with Python3 in runtime
# Beats 59.92% of users with Python3 in memory
