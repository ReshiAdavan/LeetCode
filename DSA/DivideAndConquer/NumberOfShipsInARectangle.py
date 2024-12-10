"""
This is Sea's API interface.
You should not implement it, or speculate about its implementation
"""
class Sea:
   def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
        pass

class Point:
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y

class Solution:
    def countShips(self, sea, topRight, bottomLeft):
        def countShipsInRegion(x1, y1, x2, y2):
            if x1 > x2 or y1 > y2 or not sea.hasShips(Point(x2, y2), Point(x1, y1)):
                return 0
            if x1 == x2 and y1 == y2:
                return 1

            midX = (x1 + x2) // 2
            midY = (y1 + y2) // 2

            topLeft = countShipsInRegion(x1, midY + 1, midX, y2)
            topRight = countShipsInRegion(midX + 1, midY + 1, x2, y2)
            bottomLeft = countShipsInRegion(x1, y1, midX, midY)
            bottomRight = countShipsInRegion(midX + 1, y1, x2, midY)

            return topLeft + topRight + bottomLeft + bottomRight

        return countShipsInRegion(bottomLeft.x, bottomLeft.y, topRight.x, topRight.y)
