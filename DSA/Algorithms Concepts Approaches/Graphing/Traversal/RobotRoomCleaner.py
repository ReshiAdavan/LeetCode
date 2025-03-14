# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def goBack():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell, d):
            visited.add(cell)
            robot.clean()
            # clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'

            for i in range(4):
                nd = (d + i) % 4
                newCell = (cell[0] + directions[nd][0], cell[1] + directions[nd][1])

                if newCell not in visited and robot.move():
                    backtrack(newCell, nd)
                    goBack()
                robot.turnRight()
        backtrack((0, 0), 0)

# N -> # of cells in the room, M -> # of obstacles
# TC: O(4^N - M)
# SC: O(N - M)
