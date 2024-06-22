class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        W = len(word)
        ROW, COL = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i >= W:
                return True
            
            if (r < 0 or r >= ROW or c < 0 or c >= COL or 
                board[r][c] != word[i] or (r, c) in path):
                return False

            path.add((r, c))
            
            res = (dfs(r - 1, c, i + 1) or dfs(r + 1, c, i + 1) 
                or dfs(r, c - 1, i + 1) or dfs(r, c + 1, i + 1))
            
            path.remove((r, c))
            return res

        for x in range(ROW):
            for y in range(COL):
                if dfs(x, y, 0):
                    return True
        return False
    
# Beats 68.82% of users in runtime
# Beats 53.80% of users in memory
# Time Complexity: O(N * M * 4^W)
# Space Complexity: O(W)
