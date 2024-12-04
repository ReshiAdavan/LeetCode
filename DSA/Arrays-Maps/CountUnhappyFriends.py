from typing import List

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pairMap = {}
        for x, y in pairs:
            pairMap[x] = y
            pairMap[y] = x

        rank = {}
        for i in range(n):
            rank[i] = {person: idx for idx, person in enumerate(preferences[i])}

        count = 0
        for x in range(n):
            y = pairMap[x]
            for u in preferences[x]:
                if u == y:
                    break

                v = pairMap[u]
                if rank[x][u] < rank[x][y] and rank[u][x] < rank[u][v]:
                    count += 1
                    break

        return count

# TC: O(n^2)    
# SC: O(n^2)
