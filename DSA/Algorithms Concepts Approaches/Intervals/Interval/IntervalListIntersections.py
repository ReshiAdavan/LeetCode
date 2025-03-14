from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1, p2 = 0, 0
        res = []

        while p1 < len(firstList) and p2 < len(secondList):
            new = []
            left = max(firstList[p1][0], secondList[p2][0])
            right = min(firstList[p1][1], secondList[p2][1])

            if left <= right:
                new = [left, right]
            if new:
                res.append(new)

            if firstList[p1][1] > secondList[p2][1]:
                p2 += 1
            else:
                p1 += 1
        return res

# TC: O(N + M)
# SC: O(1) auxillary space
