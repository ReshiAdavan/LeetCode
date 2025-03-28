from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xCoords, yCoords = set(), set()

        for x1, y1, x2, y2 in rectangles:
            xCoords.add(x1)
            xCoords.add(x2)
            yCoords.add(y1)
            yCoords.add(y2)

        xCoords = sorted(xCoords)
        yCoords = sorted(yCoords)

        # vertical cuts
        for i in range(len(xCoords)):
            for j in range(i + 1, len(xCoords)):
                vCut1 = xCoords[i]
                vCut2 = xCoords[j]

                left, mid, right = 0, 0, 0

                for x1, _, x2, _ in rectangles:
                    if x2 <= vCut1:
                        left += 1
                    elif x1 >= vCut2: 
                        right += 1
                    elif x1 >= vCut1 and x2 <= vCut2:
                        mid += 1

                if (left > 0 and mid > 0 and right > 0) and left + mid + right == len(rectangles):
                    return True

        # horizontal cuts
        for i in range(len(yCoords)):
            for j in range(i + 1, len(yCoords)):
                hCut1 = yCoords[i]
                hCut2 = yCoords[j]

                top, mid, bottom = 0, 0, 0

                for _, y1, _, y2 in rectangles:
                    if y1 >= hCut2:
                        top += 1
                    elif y2 <= hCut1:
                        bottom += 1
                    elif y1 >= hCut1 and y2 <= hCut2:
                        mid += 1

                if (top > 0 and mid > 0 and bottom > 0) and top + mid + bottom == len(rectangles):
                    return True
        return False

## TLE
## Let r rep. # rectangles; Let n rep. dimensions of board
# TC: O(rlogr + r^3)
# SC: O(r)
