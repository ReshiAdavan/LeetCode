from typing import List, defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for s, e in adjacentPairs:
            adjList[s].append(e)
            adjList[e].append(s)

        for k, v in adjList.items():
            if len(v) == 1:
                start = k
                break

        res = []
        visited = set()

        def dfs(node):
            res.append(node)
            visited.add(node)

            for nei in adjList[node]:
                if nei not in visited:
                    dfs(nei)

        dfs(start)
        return res
    
# TC: O(n)
# SC: O(n)
