from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        adjList = defaultdict(list)
        visit = set()
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        def dfs(i):
            if i not in visit:
                visit.add(i)
                for nei in adjList[i]:
                    adjList[nei].remove(i)
                    dfs(nei)

        res = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1
        return res

# Beats 67.69% of users in runtime
# Beats 44.32% of users in memory
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)