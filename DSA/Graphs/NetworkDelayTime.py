from collections import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        edges = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visited = set()
        maxTime = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 not in visited:
                visited.add(n1)
                maxTime = max(maxTime, w1)

                for n2, w2 in edges[n1]:
                    if n2 not in visited:
                        heapq.heappush(minHeap, (w1 + w2, n2))
        if len(visited) == n: 
            return maxTime
        return -1
        
# Beats 96.83% python submissions in runtime
# Beats 58.76% python submissions in memory usage