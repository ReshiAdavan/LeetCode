class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if not n: 
            return True
        adjList = {i : [] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        v = set()        
        def dfs(i, p):
            if i in v: 
                return False
            v.add(i)
            for nei in adjList[i]:
                if nei == p:
                    continue
                if not dfs(nei, i):
                    return False
            return True
        return dfs(0, -1) and len(v) == n
    
# Beats 85.60% of users with Python3 in runtime
# Beats 24.51% of users with Python3 in memory