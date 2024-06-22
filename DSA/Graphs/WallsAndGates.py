class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROW, COL = len(rooms),len(rooms[0])
        q = deque()

        for r in range(ROW):
            for c in range(COL):
                if rooms[r][c] == 0:
                    q.append((r, c))
        ctr = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r - 1 >= 0 and rooms[r - 1][c] == 2147483647:
                    rooms[r - 1][c] = ctr
                    q.append((r - 1, c))
                if r + 1 < ROW and rooms[r + 1][c] == 2147483647:
                    rooms[r + 1][c] = ctr
                    q.append((r + 1, c))
                if c - 1 >= 0 and rooms[r][c - 1] == 2147483647:
                    rooms[r][c - 1] = ctr
                    q.append((r, c - 1))
                if c + 1 < COL and rooms[r][c + 1] == 2147483647:
                    rooms[r][c + 1] = ctr
                    q.append((r, c + 1))
            ctr += 1

# Beats 100.00% of users in runtime
# Beats 69.78% of users in memory
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)
