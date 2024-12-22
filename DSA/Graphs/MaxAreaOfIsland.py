# Solution 1
class Solution(object):
    def maxAreaOfIsland(self, grid):
        def dfs(i, j):
            stack = [(i, j)]
            area, maxi = 1, 1
            while stack:
                di, dj = stack.pop()
                grid[i][j] = 0
                if di + 1 < r and grid[di + 1][dj] == 1:
                    stack.append((di + 1, dj))
                    grid[di + 1][dj] = 0
                    area += 1
                if di - 1 >= 0 and grid[di - 1][dj] == 1:
                    stack.append((di - 1, dj))
                    grid[di - 1][dj] = 0
                    area += 1
                if dj - 1 >= 0 and grid[di][dj - 1] == 1:
                    stack.append((di, dj - 1))
                    grid[di][dj - 1] = 0
                    area += 1
                if dj + 1 < c and grid[di][dj + 1] == 1:
                    stack.append((di, dj + 1))
                    grid[di][dj + 1] = 0
                    area += 1
            maxi = max(maxi, area)
            return maxi
        
        ans, r, c = 0, len(grid), len(grid[0])
        for i in range(0, r):
            for j in range(0, c):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        return ans

# Beats 98.80% python submissions in runtime
# Beats 87.93% python submissions in memory usage  

# Solution 2
class Solution(object):
    def maxAreaOfIsland(self, grid):
        ans = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            a = 1
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0

            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    ans = max(ans, dfs(r, c))
        return ans
                
# Beats 16.04% python submissions in runtime
# Beats 21.64% python submissions in memory usage

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        r, c = len(grid), len(grid[0])
        v = set()
        res = 0

        def dfs(i, j):
            if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] == 0 or (i, j) in v:
                return 0
            v.add((i, j))
            return (1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) +dfs(i, j - 1))
        
        for i in range(r):
            for j in range(c):
                if (i, j) not in v and grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res

# Beats 95.84% of users with Python3 in runtime
# Beats 23.71% of users with Python3 in memory