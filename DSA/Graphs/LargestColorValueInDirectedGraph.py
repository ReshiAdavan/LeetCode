from collections import defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        adjList = defaultdict(list)
        for a, b in edges:
            adjList[a].append(b)

        n, res = len(colors), 0
        path, visit = set(), set()
        cache = [[0] * 26 for _ in range(n)] 

        def dfs(node: int) -> int:
            if node in path: 
                return float("inf")
            if node in visit:
                return 0
            
            visit.add(node)
            path.add(node)

            colorIndex = ord(colors[node]) - ord('a')
            cache[node][colorIndex] = 1

            for nei in adjList[node]:
                if dfs(nei) == float("inf"):
                    return float("inf")
                for c in range(26):
                    cache[node][c] = max(cache[node][c], (1 if c == colorIndex else 0) + cache[nei][c])

            path.remove(node)
            return max(cache[node])

        for i in range(n):
            res = max(res, dfs(i))
        return -1 if res == float("inf") else res
    
# Time Complexity: O(n + m)
# Space Complexity: O(n∗26)
# Beats 29.08% of python3 users in runtime
# Beats 11.28% of python3 users in memory usage