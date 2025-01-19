from typing import List
from collections import defaultdict, deque

## DFS
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adjList = defaultdict(list)
        for cur, nei in enumerate(graph):
            adjList[cur].extend(nei)

        res = []

        def dfs(node, path):
            if node == len(graph) - 1:
                res.append(path)
                return

            for nei in adjList[node]:
                dfs(nei, path + [nei])

        dfs(0, [0])
        return res

# TC: O(V + E)
# SC: O(V + E)

## BFS
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adjList = defaultdict(list)
        for cur, nei in enumerate(graph):
            adjList[cur].extend(nei)

        q = deque([[0, [0]]])
        res = []

        while q:
            for _ in range(len(q)):
                node, path = q.popleft()
                if node == len(graph) - 1:
                    res.append(path)

                for nei in adjList[node]:
                    q.append([nei, path + [nei]])
        return res

# TC: O(V + E)
# SC: O(V + E)
