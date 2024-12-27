from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[float("inf")] * COLS for _ in range(ROWS)]
        dp[0][0] = grid[0][0]

        for c in range(1, COLS):
            dp[0][c] = dp[0][c - 1] + grid[0][c]

        for r in range(1, ROWS):
            dp[r][0] = dp[r - 1][0] + grid[r][0]

        for r in range(1, ROWS):
            for c in range(1, COLS):
                dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]

        return dp[-1][-1]

# TC: O(m * n)
# SC: O(m * n)
