from typing import List
from collections import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        preMinSum, curMinSum = [sum(nums[:n])], sum(nums[:n])
        maxiHeap = [-x for x in nums[:n]]
        heapq.heapify(maxiHeap)

        for i in range(n, 2 * n):
            maxiElement = -heapq.heappop(maxiHeap)
            curMinSum -= maxiElement
            miniElem = min(maxiElement, nums[i])
            curMinSum += miniElem
            preMinSum.append(curMinSum)
            heapq.heappush(maxiHeap, -miniElem)

        postMaxSum, curMaxSum = [sum(nums[2 * n:])], sum(nums[2 * n:])
        miniHeap = [x for x in nums[2 * n:]]
        heapq.heapify(miniHeap)

        for i in range(2 * n - 1, n - 1, -1):
            miniElement = heapq.heappop(miniHeap)
            curMaxSum -= miniElement
            maxiElem = max(miniElement, nums[i])
            curMaxSum += maxiElem
            postMaxSum.append(curMaxSum)
            heapq.heappush(miniHeap, maxiElem)
        postMaxSum = postMaxSum[::-1]

        miniDiff = float("inf")
        for a, b in zip(preMinSum, postMaxSum):
            miniDiff = min(miniDiff, a - b)
        return miniDiff

# TC: O(nlogn)
# SC: O(n)
