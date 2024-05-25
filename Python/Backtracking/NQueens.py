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

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols, pDiag, nDiag = set(), set(), set()
        board = [["."] * n for _ in range(n)]

        def dfs(i):
            if i >= n:
                soln = ["".join(row) for row in board] 
                res.append(soln)
                return
            
            for k in range(n):
                if k not in cols and (k - i) not in nDiag and (k + i) not in pDiag:
                    cols.add(k)
                    pDiag.add(k + i)
                    nDiag.add(k - i)
                    board[i][k] = "Q"
                    dfs(i + 1)
                    board[i][k] = "."
                    cols.remove(k)
                    pDiag.remove(k + i)
                    nDiag.remove(k - i)
            return

        dfs(0)
        return res
    
# Beats 83.75% of users with Python3 in runtime 
# Beats 79.78% of users with Python3 in memory