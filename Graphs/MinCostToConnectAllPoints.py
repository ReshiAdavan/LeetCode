class Solution(object):
    def minCostConnectPoints(self, points):
        L = len(points)
        AList = {i: [] for i in range(L)}
        for i in range(L):
            x1, y1 = points[i]
            for j in range(i + 1, L):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                AList[i].append([dist, j])
                AList[j].append([dist, i])

        endCost = 0
        visited = set()
        minH = [[0, 0]]
        while len(visited) < L:
            cost, i = heapq.heappop(minH)
            if i not in visited:
                visited.add(i)
                endCost += cost
                for neighbourCost, neighbour in AList[i]:
                    if neighbour not in visited:
                        heapq.heappush(minH, [neighbourCost, neighbour])
        return endCost

# Beats 34.06% python submissions in runtime
# Beats 13.92% python submissions in memory usage  