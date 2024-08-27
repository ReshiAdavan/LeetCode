class Solution(object):
    def solve(self, board):
        """Do not return anything, modify board in-place instead."""
        rows, cols = len(board), len(board[0])

        def DFS(r, c):
            if r not in range(rows) or c not in range(cols) or board[r][c] != "O":
                return
            board[r][c] = "A"
            DFS(r + 1, c)
            DFS(r - 1, c)
            DFS(r, c + 1)
            DFS(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols - 1]):
                    DFS(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "A":
                    board[r][c] = "O"

# Beats 86.68% python submissions in runtime
# Beats 68.16% python submissions in memory usage 

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """Do not return anything, modify board in-place instead."""
        ROWS, COLS = len(board), len(board[0])
        v = set()
        
        def dfs(i, j):
            if (i < 0 or i == ROWS or j < 0 or j == COLS 
            or board[i][j] != "O" or (i, j) in v):
                return
            v.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in v:
                    board[i][j] = "X"

# Beats 54.96% of users with Python3 in runtime
# Beats 82.31% of users with Python3 in memory