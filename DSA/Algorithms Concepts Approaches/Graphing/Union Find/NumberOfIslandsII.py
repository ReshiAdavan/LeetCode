from typing import List

class Solution:
    def numIslands(self, grid):
        vis = set()
        islands = 0
        r, c = len(grid), len(grid[0])

        def dfs(i, j):
            stack = [(i, j)]
            vis.add((i, j))

            while stack:
                di, dj = stack.pop()
                if di + 1 < r and grid[di + 1][dj] == 1 and (di + 1, dj) not in vis:
                    stack.append((di + 1, dj))
                    vis.add((di + 1, dj))
                if di - 1 >= 0 and grid[di - 1][dj] == 1 and (di - 1, dj) not in vis:
                    stack.append((di - 1, dj))
                    vis.add((di - 1, dj))
                if dj - 1 >= 0 and grid[di][dj - 1] == 1 and (di, dj - 1) not in vis:
                    stack.append((di, dj - 1))
                    vis.add((di, dj - 1))
                if dj + 1 < c and grid[di][dj + 1] == 1 and (di, dj + 1) not in vis:
                    stack.append((di, dj + 1))
                    vis.add((di, dj + 1))

        for i in range(0, r):
            for j in range(0, c):
                if grid[i][j] == 1 and (i, j) not in vis:
                    dfs(i, j)
                    islands += 1
        return islands

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid = [[0] * n for _ in range(m)]
        res = []

        for r, c in positions:
            grid[r][c] = 1
            res.append(self.numIslands(grid))

        return res

## TLE
## Let k rep. len(positions), m rep. rows, and n rep. cols
# TC: O(k * m * n) 
# SC: O(k * m * n)

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid, res, islands = [[0] * n for _ in range(m)], [], 0
        uf = UnionFind(m * n)

        for r, c in positions:
            if grid[r][c] == 1:
                res.append(islands)
                continue

            grid[r][c] = 1
            islands += 1

            idx = r * n + c

            # union new land pieces together and --islandCount
            for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                dr, dc = r + i, c + j
                if 0 <= dr < m and 0 <= dc < n and grid[dr][dc] == 1:
                    nidx = dr * n + dc
                    if uf.union(idx, nidx):
                        islands -= 1
            res.append(islands)
        return res
    
## Let k rep. len(positions), m rep. rows, and n rep. cols
# TC: O(k * α(m + n) => O(k) since ackerman function grows extremely slowly; # k per pos, m + n for union-find
# SC: O(m * n) for grid and union-find
