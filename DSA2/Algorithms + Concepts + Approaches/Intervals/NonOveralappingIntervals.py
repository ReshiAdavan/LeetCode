from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        
        intervals.sort(key=lambda x: x[0])
        removals = 0
        prev = intervals[0][1]

        for i in range(1, len(intervals)):
            if prev > intervals[i][0]:
                removals += 1
                prev = min(intervals[i][1], prev)
            else:
                prev = intervals[i][1]
        return removals
    
# TC: O(nlogn)
# SC: O(n)