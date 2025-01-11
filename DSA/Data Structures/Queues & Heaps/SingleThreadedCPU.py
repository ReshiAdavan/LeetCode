from typing import List
from collections import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        enqTasks = list(range(n))
        enqTasks.sort(key=lambda i: (tasks[i][0], i))

        res, minHeap = [], []
        time = 1
        i = 0

        while minHeap or i < len(enqTasks):
            while i < len(enqTasks) and time >= tasks[enqTasks[i]][0]:
                heapq.heappush(minHeap, [tasks[enqTasks[i]][1], enqTasks[i]])
                i += 1

            if not minHeap:
                time = tasks[enqTasks[i]][0]
            else:
                pT, j = heapq.heappop(minHeap)
                res.append(j)
                time += pT

        return res

# TC: O(nlogn)
# SC: O(n)
