from typing import List
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        cache = {}
        intervals = sorted(zip(startTime, endTime, profit))
        l = len(intervals)

        def dfs(i):
            if i >= l:
                return 0
            if i in cache:
                return cache[i]
            ## Linear search for next index [O(n)]
            # j = i + 1
            # while j < l:
            #     if intervals[i][1] <= intervals[j][0]:
            #         break
            #     j += 1

            ## Binary search for next index [O(log(n))]
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = max(intervals[i][2] + dfs(j), dfs(i + 1))
            return cache[i]

        return dfs(0)
    
# Beats 74.29% of users with Python3
# Beats 25.51% of users with Python3

# TC: O(nlog(n))
# SC: O(n)

