class Solution(object):
    def solve(self, board):
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