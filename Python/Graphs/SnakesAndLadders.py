class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)

        board.reverse()
        def coordinates(n: int):
            r = (n - 1) // length
            c = (n - 1) % length
            if r % 2: c = (length - 1 ) - c
            return [r, c]

        q = deque()
        q.append([1, 0]) # [square, # of moves]
        visited = set()

        while q:
            square, moves = q.popleft()

            for i in range(1, 7):
                nextSquare = square + i
                r, c = coordinates(nextSquare)

                if board[r][c] != -1:
                    nextSquare = board[r][c]
                if nextSquare == length * length:
                    return moves + 1
                if nextSquare not in visited:
                    visited.add(nextSquare)
                    q.append([nextSquare, moves + 1])
                
        return -1
        
# Beats 94.66% python submissions in runtime
# Beats 78.88% python submissions in memory usage