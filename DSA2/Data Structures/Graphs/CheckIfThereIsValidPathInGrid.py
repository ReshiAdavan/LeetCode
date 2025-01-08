from collections import deque
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        paths = {
            1: ["L", "R"],
            2: ["U", "D"],
            3: ["L", "D"],
            4: ["R", "D"],
            5: ["L", "U"],
            6: ["R", "U"]
        }
        directions = {
            "R": (0,1),
            "L": (0,-1),
            "D": (1,0),
            "U": (-1,0)
        }
        opposites = {
            "R": "L",
            "L": "R",
            "U": "D",
            "D": "U"
        }

        visited = set()
        queue = deque()
        queue.append(((0, 0), None))

        while queue:
            cur, prev = queue.popleft()
            x, y = cur

            if x < 0 or x >= m or y < 0 or y >= n:
                continue
            street = grid[x][y]
            if prev and prev not in paths[street]:
                continue

            if x == m - 1 and y == n - 1:
                return True

            for path in paths[street]:
                if path == prev:
                    continue
                dx, dy = directions[path]
                newx, newy = x + dx, y + dy
                if (newx, newy) not in visited:
                    visited.add((newx, newy))
                    queue.append(((newx, newy), opposites[path]))
        return False

# TC: O(M + N)
# SC: O(M + N)
