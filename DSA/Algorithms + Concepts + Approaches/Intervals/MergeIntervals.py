from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key = lambda x : x[0])
        res = [intervals[0]]

        for item in intervals[1:]:
            newEnd = res[-1][1]

            # overlapping
            if item[0] <= newEnd: 
                res[-1][1] = max(newEnd, item[1])
            else:
                res.append(item)
        return res
    
    
# Time Complexity: O(nlog(n))
# Space Complexity: O(n)
# Beats 99.84% of python users in runtime
# Beats 57.24% of python users in memory usage
