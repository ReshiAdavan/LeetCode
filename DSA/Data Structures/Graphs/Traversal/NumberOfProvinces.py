from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjList = {x + 1: [] for x in range(len(isConnected))}
        for i, nei in enumerate(isConnected):
            for j, isPopulated in enumerate(nei):
                if isPopulated and i + 1 != j + 1:
                    adjList[i + 1].append(j + 1)

        v = set()

        def dfs(n):
            for nei in adjList[n]:
                if nei not in v:
                    v.add(nei)
                    dfs(nei)

        res = 0
        for x in range(len(isConnected)):
            if x + 1 not in v:
                res += 1
                dfs(x + 1)
        return res

# TC: O(N + E)
# SC: O(N + E)
