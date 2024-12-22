from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        redMap = defaultdict(list)
        blueMap = defaultdict(list)

        for src, dest in redEdges: redMap[src].append(dest)
        for src, dest in blueEdges: blueMap[src].append(dest)

        answer = [-1 for i in range(n)]
        q = deque()
        q.append([0, 0, None]) # node, len, color
        visited = set()
        visited.add((0, None)) # node, color

        while q:
            node, length, edgeColor = q.popleft()
            if answer[node] == -1: 
                answer[node] = length
            
            if edgeColor != "RED":
                for nei in redMap[node]:
                    if (nei, "RED") not in visited:
                        visited.add((nei, "RED"))
                        q.append([nei, length + 1, "RED"])
            
            if edgeColor != "BLUE":
                for nei in blueMap[node]:
                    if (nei, "BLUE") not in visited:
                        visited.add((nei, "BLUE"))
                        q.append([nei, length + 1, "BLUE"])
        return answer
    
# Beats 94.44% python submissions in runtime
# Beats 89.44% python submissions in memory usage 