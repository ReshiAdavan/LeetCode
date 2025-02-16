from typing import List
import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap, maxi = [], 0
        for i in range(len(nums)):
            n = nums[i]
            while n % 2 == 0:
                n //= 2
            heap.append([n, nums[i] if nums[i] % 2 == 0 else 2 * nums[i]])
            maxi = max(maxi, n)

        res = float("inf")
        heapq.heapify(heap)
        while len(heap) == len(nums):
            n, nMaxi = heapq.heappop(heap)
            res = min(res, maxi - n)

            if n < nMaxi:
                heapq.heappush(heap, [2 * n, nMaxi])
                maxi = max(maxi, 2 * n)
        return res

# TC: O(n + nlogn + nlogn)
# SC: O(n)
