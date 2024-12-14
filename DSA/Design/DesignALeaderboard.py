from collections import defaultdict, heapq

class Leaderboard:

    def __init__(self):
        self.board = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.board[playerId] += score

    def top(self, K: int) -> int:
        heap = [-score for score in self.board.values()]
        heapq.heapify(heap)

        sumScore = 0
        for _ in range(K):
            sumScore += heapq.heappop(heap)
        return -sumScore

    def reset(self, playerId: int) -> None:
        del self.board[playerId]

# TC: O(1), O(nlogn), O(1)
# SC: O(n)

from collections import defaultdict
import heapq

class Leaderboard:

    def __init__(self):
        self.board = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.board[playerId] += score

    def top(self, K: int) -> int:
        top_scores = sorted(self.board.values(), reverse=True)
        return sum(top_scores[:K])

    def reset(self, playerId: int) -> None:
        del self.board[playerId]

# TC: O(1), O(nlogn), O(1)
# SC: O(n)