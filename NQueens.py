class Solution(object):
    def solveNQueens(self, n):
        cols, upDiag, downDiag = set(), set(), set()
        NQueensBoard, board = [], [["."] * n for i in range(n)]

        def DFS(r):
            if r == n:
                b = ["".join(row) for row in board]
                NQueensBoard.append(b)
                return

            for c in range(n):
                if c in cols or (r + c) in upDiag or (r - c) in downDiag:
                    continue

                cols.add(c)
                upDiag.add(r + c)
                downDiag.add(r - c)
                board[r][c] = "Q"

                DFS(r + 1)

                cols.remove(c)
                upDiag.remove(r + c)
                downDiag.remove(r - c)
                board[r][c] = "."

        DFS(0)
        return NQueensBoard

# Beats 69.48% python submissions in runtime
# Beats 60.30% python submissions in memory usage 