from typing import List
from collections import defaultdict

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def trav(node, par):
            time = 0

            for nei in adj[node]:
                if nei != par:
                    t = trav(nei, node)
                    if t > 0 or hasApple[nei]:
                        time += (t + 2)

            return time

        return trav(0, -1)

# TC: O(n)
# SC: O(n)
