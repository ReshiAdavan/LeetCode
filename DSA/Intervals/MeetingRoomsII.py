from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        for s, e in intervals:
            start.append(s)
            end.append(e)
        
        start = sorted(start)
        end = sorted(end)
        sIdx, eIdx = 0, 0
        count = 0
        maxi = 0

        while sIdx < len(start) and eIdx < len(end):
            if start[sIdx] < end[eIdx] :
                sIdx += 1
                count += 1
            else:
                eIdx += 1
                count -= 1
            maxi = max(maxi, count)
        return maxi
        
# Time Complexity: O(nlog(n))
# Space Complexity: O(n)
# Beats 100% of python users in runtime (it runs in 3ms lol)
# Beats 99.97% of python users in memory usage
