from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def checkCuts(dim: int) -> bool:
            gaps = 0
            rectangles.sort(key=lambda x: x[dim])
            end = rectangles[0][dim + 2]

            for i in range(1, len(rectangles)):
                rect = rectangles[i]
                if end <= rect[dim]:
                    gaps += 1
                end = max(end, rect[dim + 2])

            return gaps >= 2
        return checkCuts(0) or checkCuts(1)

## Let r rep. # rectangles; Let n rep. dimensions of board
# TC: O(rlogr)
# SC: O(r)
