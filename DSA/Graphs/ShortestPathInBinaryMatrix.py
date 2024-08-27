# Solution 1: More time-effiicent BFS approach:

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        queue = deque([(0, 0, 1)])
        visited = set((0, 0))
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        while queue:
            row, col, length = queue.popleft()
            if row == n - 1 and col == n - 1:
                return length
            if (min(row, col) < 0 or max(row, col) >= n or grid[row][col]):
                continue
            for dr, dc in directions:
                if (row + dr, col + dc) not in visited:
                    queue.append((row + dr, col + dc, length + 1))
                    visited.add((row + dr, col + dc))
        return -1
    
    # Beats 81.29% python submissions in runtime
    # Beats 12.57% python submissions in memory usage
    
# Solution 2: More space-effiicent BFS approach:

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        queue = deque([(0, 0, 1)])
        visited = set((0, 0))
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        while queue:
            row, col, length = queue.popleft()
            if row == n - 1 and col == n - 1:
                return length
            for dr, dc in directions:
                if (row + dr, col + dc) not in visited and min(row, col) >= 0 and max(row, col) < n and not grid[row][col]:
                    queue.append((row + dr, col + dc, length + 1))
                    visited.add((row + dr, col + dc))
        return -1
    
    # Beats 50.21% python submissions in runtime
    # Beats 26.71% python submissions in memory usage
