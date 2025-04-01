from typing import List

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [[float('inf')] * 4 for _ in range(n)]

        # pos, lane
        dp[0][2] = 0
        dp[0][1] = dp[0][3] = 1

        for pos in range(1, n):
            for lane in range(1, 4):
                if obstacles[pos] != lane:
                    dp[pos][lane] = dp[pos - 1][lane]

            for lane in range(1, 4):
                if obstacles[pos] == lane:
                    continue

                for otherLane in range(1, 4):
                    if otherLane != lane and obstacles[pos] != otherLane:
                        dp[pos][lane] = min(dp[pos][lane], 1 + dp[pos][otherLane])

        return min(dp[-1][1], dp[-1][2], dp[-1][3])

# TC: O(n * 3)
# SC: O(n * 3)

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [1, 0, 1]

        for pos in range(1, n):
            if obstacles[pos] > 0:
                dp[obstacles[pos] - 1] = float("inf")

            minJumps = min(dp)

            for j in range(3):
                if obstacles[pos] != j + 1:
                    dp[j] = min(dp[j], minJumps + 1)

        return min(dp)

# TC: O(n * 3)
# SC: O(3)
