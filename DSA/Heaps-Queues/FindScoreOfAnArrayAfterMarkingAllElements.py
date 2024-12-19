from typing import List
from collections import heapq

class Solution:
    def findScore(self, nums: List[int]) -> int:
        visited = set() # store indexes
        heap = [[n, idx] for idx, n in enumerate(nums)]
        heapq.heapify(heap)
        score = 0

        while heap:
            value, index = heapq.heappop(heap)
            if index in visited:
                continue

            score += value

            visited.add(index)
            if index + 1 < len(nums):
                visited.add(index + 1)
            if index - 1 >= 0:
                visited.add(index - 1)
        return score

# TC: O(nlogn)
# SC: O(2n)

class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = [[n, idx] for idx, n in enumerate(nums)]
        heapq.heapify(heap)
        score = 0

        while heap:
            value, index = heapq.heappop(heap)
            if nums[index] == -1:
                continue

            score += value

            nums[index] = -1
            if index + 1 < len(nums):
                nums[index + 1] = -1
            if index - 1 >= 0:
                nums[index - 1] = -1
        return score

# TC: O(nlogn)
# SC: O(n)