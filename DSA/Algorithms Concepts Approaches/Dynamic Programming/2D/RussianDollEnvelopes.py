from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        cache = {}

        def memo(i):
            if i in cache:
                return cache[i]
            if i >= len(envelopes):
                return 0

            maxi = 1
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    maxi = max(maxi, 1 + memo(j))
            cache[i] = maxi
            return maxi

        res = 0
        for k in range(len(envelopes)):
            res = max(res, memo(k))
        return res

## Let n rep. len(envelopes)
# TC: O(n^2)
# SC: O(n^2)

from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []

        for _, h in envelopes:
            i = bisect_left(dp, h)  # determines where to place h in dp

            # adding h either extends our solution or improves it
            if i == len(dp):
                dp.append(h)  # extends
            else:
                dp[i] = h  # improves

        return len(dp)

# TC: O(nlogn)
# SC: O(n)
