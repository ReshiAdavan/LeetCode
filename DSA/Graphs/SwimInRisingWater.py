class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        N = len(grid)
        visit = set((0, 0))
        minH = [[grid[0][0], 0, 0]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if not (
                    neiR < 0
                    or neiC < 0
                    or neiR == N
                    or neiC == N
                    or (neiR, neiC) in visit
                ):
                    visit.add((neiR, neiC))
                    heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])

# Beats 73.91% of users in runtime
# Beats 59.11% of users in memory
# Time Complexity: O(N*N*log(N))
# Space Complexity: O(N*N)