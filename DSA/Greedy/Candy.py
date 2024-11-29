from typing import List
from collections import heapq

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        minHeap = [(rating, index) for index, rating in enumerate(ratings)]
        heapq.heapify(minHeap)

        candies = [0] * n

        while minHeap:
            _, index = heapq.heappop(minHeap)
            left_candy = candies[index - 1] if index > 0 and ratings[index] > ratings[index - 1] else 0
            right_candy = candies[index + 1] if index < n - 1 and ratings[index] > ratings[index + 1] else 0
            candies[index] = max(left_candy, right_candy) + 1

        return sum(candies)

# TC: O(nlogn)
# SC: O(n)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)

# TC: O(n)
# SC: O(n)
