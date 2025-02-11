from collections import heapq
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        n, m = len(heightMap), len(heightMap[0])
        if n < 3 or m < 3:
            return 0

        vis = [[0] * m for _ in range(n)]
        pq = []

        for i in range(n):
            heapq.heappush(pq, [heightMap[i][0], i, 0])
            heapq.heappush(pq, [heightMap[i][m - 1], i, m - 1])
            vis[i][0] = vis[i][m - 1] = 1

        for j in range(1, m - 1):
            heapq.heappush(pq, [heightMap[0][j], 0, j])
            heapq.heappush(pq, [heightMap[n - 1][j], n - 1, j])
            vis[0][j] = vis[n - 1][j] = 1

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        water = 0
        boundary = 0

        while pq:
            h, r, c = heapq.heappop(pq)
            boundary = max(boundary, h)

            for dx, dy in directions:
                dr, dc = r + dx, c + dy
                if 0 <= dr < n and 0 <= dc < m and not vis[dr][dc]:
                    vis[dr][dc] = 1
                    if boundary > heightMap[dr][dc]:
                        water += (boundary - heightMap[dr][dc])
                    heapq.heappush(pq, [heightMap[dr][dc], dr, dc])
        return water

# TC: O(N * M * log(N + M))
# SC: O(N * M)
