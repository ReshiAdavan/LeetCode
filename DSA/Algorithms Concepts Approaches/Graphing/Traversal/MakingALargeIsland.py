from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def dfs(i, j, uid):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = uid
            return 1 + dfs(i + 1, j, uid) + dfs(i - 1, j, uid) + dfs(i, j + 1, uid) + dfs(i, j - 1, uid)

        uidAreaMap = {}
        uid = 2

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j, uid)
                    uidAreaMap[uid] = area
                    uid += 1

        if not uidAreaMap:
            return 1
        if len(uidAreaMap) == 1 and uidAreaMap[2] == n * n:
            return n * n

        maxiSize = max(uidAreaMap.values())

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    v = set()
                    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        r, c = i + di, j + dj
                        if 0 <= r < n and 0 <= c < n and grid[r][c] != 0:
                            v.add(grid[r][c])

                    size = 0
                    for uid in v:
                        size += uidAreaMap[uid]
                    maxiSize = max(maxiSize, 1 + size)
        return maxiSize

# TC: O(n^2)
# SC: O(i) where i is the number of islands in the grid
