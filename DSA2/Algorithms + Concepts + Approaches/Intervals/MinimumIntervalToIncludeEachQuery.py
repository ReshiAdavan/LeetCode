from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = []
        for q in queries:
            mini = float('inf')
            for s, e in intervals:
                if s <= q <= e:
                    length = e - s + 1
                    mini = min(mini, length)
            if mini == float('inf'):
                res.append(-1)
            else:
                res.append(mini)
        return res

## TLE
# TC: O(nlogn + m*n) = O(m*n)
# SC: O(n)

from collections import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        res = {}
        i = 0

        for q in sorted(queries):
            # add all intervals where query value falls in that interval
            while i < len(intervals) and intervals[i][0] <= q:
                s, e = intervals[i]
                heapq.heappush(minHeap, [e - s + 1, e])
                i += 1

            # pop pairs from heap until query falls in that interval
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            # write to hashmap (key: query value, value: size of interval) 
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]

# TC: O(nlogn + mlogm)
# SC: O(n + m)
