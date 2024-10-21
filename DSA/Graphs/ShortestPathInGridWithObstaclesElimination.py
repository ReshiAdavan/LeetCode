from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        ROW, COL = len(grid), len(grid[0])
        queue = deque([(0, 0, k)])
        visited = set((0, 0, k))

        count = 0
        while queue:
            for _ in range(len(queue)):
                r, c, k = queue.popleft()

                if (r, c) == (ROW - 1, COL - 1):
                    return count

                if r + 1 < ROW:
                    if grid[r + 1][c] == 1:
                        if k > 0 and (r + 1, c, k - 1) not in visited:
                            visited.add((r + 1, c, k - 1))
                            queue.append((r + 1, c, k - 1))
                    else:
                        if (r + 1, c, k) not in visited:
                            visited.add((r + 1, c, k))
                            queue.append((r + 1, c, k))

                if r - 1 >= 0:
                    if grid[r - 1][c] == 1:
                        if k > 0 and (r - 1, c, k - 1) not in visited:
                            visited.add((r - 1, c, k - 1))
                            queue.append((r - 1, c, k - 1))
                    else:
                        if (r - 1, c, k) not in visited:
                            visited.add((r - 1, c, k))
                            queue.append((r - 1, c, k))

                if c + 1 < COL:
                    if grid[r][c + 1] == 1:
                        if k > 0 and (r, c + 1, k - 1) not in visited:
                            visited.add((r, c + 1, k - 1))
                            queue.append((r, c + 1, k - 1))
                    else:
                        if (r, c + 1, k) not in visited:
                            visited.add((r, c + 1, k))
                            queue.append((r, c + 1, k))

                if c - 1 >= 0:
                    if grid[r][c - 1] == 1:
                        if k > 0 and (r, c - 1, k - 1) not in visited:
                            visited.add((r, c - 1, k - 1))
                            queue.append((r, c - 1, k - 1))
                    else:
                        if (r, c - 1, k) not in visited:
                            visited.add((r, c - 1, k))
                            queue.append((r, c - 1, k))

            count += 1
        return -1

# Time Complexity: O(n * m)
# Space Complexity: O(m * n)