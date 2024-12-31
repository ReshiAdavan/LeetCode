from typing import List
from collections import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minHeap = []
        for i in range(min(k, len(nums1))):
            heapq.heappush(minHeap, [nums1[i] + nums2[0], i, 0])

        res = []
        while minHeap and k > 0:
            _, i, j = heapq.heappop(minHeap)
            res.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(minHeap, [nums1[i] + nums2[j + 1], i, j + 1])

            k -= 1
        return res

# TC: O(min(k, n) * log(min(k, n)) + min(k, (n + m)) * log(min(k, (n + m))))
# SC: O(min(k, n) + min(k, (n + m)))

## To simplify the TC and SC, it truly depends on k, hence:
# TC: O(k * log(k))
# SC: O(k)
