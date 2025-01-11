from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]:
            return 0

        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * COLS for _ in range(ROWS)]
        dp[-1][-1] = 1 if obstacleGrid[-1][-1] != 1 else 0

        for i in range(ROWS - 1, -1, -1):
            for j in range(COLS - 1, -1, -1):
                if i + 1 < ROWS and obstacleGrid[i + 1][j] != 1:
                    dp[i][j] += dp[i + 1][j]
                if j + 1 < COLS and obstacleGrid[i][j + 1] != 1:
                    dp[i][j] += dp[i][j + 1]

        return dp[0][0]

# TC: O(n * m)
# SC: O(n * m)
