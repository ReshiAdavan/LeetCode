from typing import List
from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque([[0, 0, health - grid[0][0]]])
        v = set((0, 0, grid[0][0]))
        d = [[0, 1], [-1, 0], [1, 0], [0, -1]]

        while q:
            r, c, h = q.popleft()
            if (r, c) == (ROWS - 1, COLS - 1) and h > 0:
                return True
            if (r, c, h) in v:
                continue
            v.add((r, c, h))

            for dx, dy in d:
                dr, dc = r + dx, c + dy
                if 0 <= dr < ROWS and 0 <= dc < COLS and (dr, dc, h) not in v:
                    if grid[dr][dc] == 0:
                        q.append([dr, dc, h])
                    elif h > 1:
                        q.append([dr, dc, h - 1])
        return False

# TC: O(M * N)
# SC: O(M * N)
