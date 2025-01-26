from collections import deque

class Solution(object):
    def orangesRotting(self, grid): 
        q = deque()
        fresh, time = 0, 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

# Beats 68.92% python submissions in runtime
# Beats 47.69% python submissions in memory usage 

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        r, c = len(grid), len(grid[0])
        q = deque()
        f = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    f += 1
                if grid[i][j] == 2:
                    q.append((i, j))

        mins = 0
        while q and f > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                if row + 1 < r and grid[row + 1][col] == 1:
                    f -= 1
                    grid[row + 1][col] = 2
                    q.append((row + 1, col))
                if row - 1 >= 0 and grid[row - 1][col] == 1:
                    f -= 1
                    grid[row - 1][col] = 2
                    q.append((row - 1, col))
                if col + 1 < c and grid[row][col + 1] == 1:
                    f -= 1
                    grid[row][col + 1] = 2
                    q.append((row, col + 1))
                if col - 1 >= 0 and grid[row][col - 1] == 1:
                    f -= 1
                    grid[row][col - 1] = 2
                    q.append((row, col - 1))
            mins += 1
        if f == 0:
            return mins
        return -1

# Beats 84.68% of users with Python3 in runtime
# Beats 25.15% of users with Python3 in memory