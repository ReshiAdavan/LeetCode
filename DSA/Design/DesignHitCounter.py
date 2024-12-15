from collections import deque

class HitCounter:

    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        return len(self.hits)
    
## Using a Queue
# TC: O(1)
# SC: O(n)
    
class HitCounter:

    def __init__(self):
        self.datapoints = []
        self.left = 0
        self.curSum = 0

    def hit(self, timestamp: int) -> None:
        if self.datapoints and self.datapoints[-1][0] == timestamp:
            self.datapoints[-1][1] += 1
        else:
            self.datapoints.append([timestamp, 1])

        self.curSum += 1

        while self.datapoints[self.left][0] <= timestamp - 300:
            self.curSum -= self.datapoints[self.left][1]
            self.left += 1

    def getHits(self, timestamp: int) -> int:
        while self.left < len(self.datapoints) and self.datapoints[self.left][0] <= timestamp - 300:
            self.curSum -= self.datapoints[self.left][1]
            self.left += 1
        return self.curSum

## Using sliding window + array => scales better for multiple hits at the same time
# TC: O(1) 
# SC: O(n)
