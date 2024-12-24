from typing import List
from collections import heapq, deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxHeap = []

        for right in range(len(nums)):
            heapq.heappush(maxHeap, [-nums[right], right])

            if right >= k - 1:
                while maxHeap[0][1] <= right - k:
                    heapq.heappop(maxHeap)
                res.append(-maxHeap[0][0])
        return res
    
# TC: O(Nlogk)
# SC: O(k)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        left = 0

        for right in range(len(nums)):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            if left > q[0]:
                q.popleft()

            if right >= k - 1:
                output.append(nums[q[0]])
                left += 1

        return output
    
# TC: O(k)
# SC: O(k)
