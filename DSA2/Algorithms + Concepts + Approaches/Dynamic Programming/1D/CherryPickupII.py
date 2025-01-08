class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        cache = {}

        def dfs(r, c1, c2):
            if c1 == c2 or min(c1, c2) < 0 or max(c1, c2) >= COL:
                return 0
            if (r, c1, c2) in cache:
                return cache[(r, c1, c2)]
            if r == ROW - 1:
                return grid[r][c1] + grid[r][c2]

            res = 0
            for c1d in [-1, 0, 1]:
                for c2d in [-1, 0, 1]:
                    res = max(res, dfs(r + 1, c1 + c1d, c2 + c2d))
            res += grid[r][c1] + grid[r][c2]
            cache[(r, c1, c2)] = res
            return cache[(r, c1, c2)]

        return dfs(0, 0, COL - 1)
    
# Time Complexity: O(R*C^2)
# Space Complexity: O(R*C^2)
# Beats 25.61% of python users in runtime
# Beats 26.80% of python users in memory usage

from itertools import product
from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        cache = [[0] * COL for _ in range(COL)]

        for r in reversed(range(ROW)):
            cur_cache = [[0] * COL for _ in range(COL)]
            for c1 in range(COL - 1):
                for c2 in range(c1 + 1, COL):
                    max_cherries = 0
                    cherries = grid[r][c1] + grid[r][c2]
                    for c1_d, c2_d in product([-1, 0, 1], [-1, 0, 1]):
                        nc1, nc2 = c1 + c1_d, c2 + c2_d
                        if nc1 < 0 or nc2 < 0 or nc1 == COL or nc2 == COL:
                            continue
                        max_cherries = max(max_cherries, cherries + cache[nc1][nc2])
                    cur_cache[c1][c2] = max_cherries
            cache = cur_cache
        return cache[0][COL - 1]

# Time Complexity: O(R*C^2)
# Space Complexity: O(C^2)
# Beats 70.01% of python users in runtime
# Beats 95.51% of python users in memory usage

