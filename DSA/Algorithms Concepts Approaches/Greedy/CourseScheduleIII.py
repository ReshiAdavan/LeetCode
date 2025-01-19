from typing import List
from collections import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        maxHeap, time = [], 0

        for duration, lastDay in courses:
            time += duration
            heapq.heappush(maxHeap, -duration)

            if time > lastDay:
                duration = -heapq.heappop(maxHeap)
                time -= duration

        return len(maxHeap)
    
# TC: O(NlogN)
# SC: O(N)
