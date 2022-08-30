class Solution(object):
    def numIslands(self, grid):
        def dfs(i, j):
            stack = [(i, j)]
            while stack:
                di, dj = stack.pop()
                grid[i][j] = '0'
                if di + 1 < r and grid[di + 1][dj] == '1':
                    stack.append((di + 1, dj))
                    grid[di + 1][dj] = '0'
                if di - 1 >= 0 and grid[di - 1][dj] == '1':
                    stack.append((di - 1, dj))
                    grid[di - 1][dj] = '0'
                if dj - 1 >= 0 and grid[di][dj - 1] == '1':
                    stack.append((di, dj - 1))
                    grid[di][dj - 1] = '0'
                if dj + 1 < c and grid[di][dj + 1] == '1':
                    stack.append((di, dj + 1))
                    grid[di][dj + 1] = '0'
            return

        islands = 0
        r, c = len(grid), len(grid[0])
        for i in range(0, r):
            for j in range(0, c):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islands += 1
        return islands

# Beats 99.09% python submissions in runtime
# Beats 93.60% python submissions in memory usage  
            