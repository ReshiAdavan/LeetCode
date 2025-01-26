from typing import List

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        distinctIslands = set()

        def dfs(r, c, shape, origin):
            grid[r][c] = 0
            shape.append((r - origin[0], c - origin[1]))
            # right
            if c + 1 < COL and grid[r][c + 1] == 1:
                dfs(r, c + 1, shape, origin)
            # down
            if r + 1 < ROW and grid[r + 1][c] == 1:
                dfs(r + 1, c, shape, origin)
            # left
            if c - 1 >= 0 and grid[r][c - 1] == 1:
                dfs(r, c - 1, shape, origin)
            # up
            if r - 1 >= 0 and grid[r - 1][c] == 1:
                dfs(r - 1, c, shape, origin)

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    shape = []
                    dfs(i, j, shape, (i, j))
                    distinctIslands.add(tuple(shape))
        return len(distinctIslands)

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
# Beats 100% of python users in runtime (it runs in 0ms lol)
# Beats 48.10% of python users in memory usage
