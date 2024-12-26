from typing import List
from collections import heapq, deque

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

class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        n = len(nums)
        q = deque()

        for i in range(n):
            if q and nums[i] >= q[-1]:
                skip = False
                while q:
                    mini = q.pop()
                    if not skip:
                        score += mini
                    skip = not skip
            else:
                q.append(nums[i])

        skip = False
        while q:
            mini = q.pop()
            if not skip:
                score += mini
            skip = not skip
        return score

# TC: O(n)
# SC: O(n)
