from typing import List
from math import random

class Solution:

    def __init__(self, w: List[int]):
        self.total = 0
        self.distance_line = []

        for weight in w:
            self.total += weight
            self.distance_line.append(self.total) 

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)

        ## Linear Seaarch (O(n))
        for idx, dist in enumerate(self.distance_line):
            if target <= dist:
                return idx

        ## Binary Search (O(log(n)))
        left, right = 0, len(self.distance_line)

        while left <= right:
            mid = (left + right) // 2
            if target > self.distance_line[mid]: 
                left = mid + 1
            else:
                right = mid - 1
        return left

# TC: O(log(m))
# SC: O(n)
