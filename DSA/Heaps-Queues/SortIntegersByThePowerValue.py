from collections import heapq


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        heap = []
        for i in range(lo, hi + 1):
            heapq.heappush(heap, [self.power(i), i])

        for _ in range(k):
            _, elem = heapq.heappop(heap)
        return elem

    def power(self, x):
        if x == 1:
            return 0
        if x % 2 == 0:
            return 1 + self.power(x // 2)
        else:
            return 1 + self.power((3 * x) + 1)  

## Heap + Recursiom
# TC: O(n * p + n * logn + k * logn)
# SC: O(n)


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        cache = {1: 0, 2: 1}

        def power(x):
            if x in cache:
                return cache[x]
            if x % 2 == 0:
                cache[x] = 1 + power(x // 2)
                return cache[x]
            else:
                cache[x] = 1 + power((3 * x) + 1)
                return cache[x]

        heap = []
        for i in range(lo, hi + 1):
            heapq.heappush(heap, [power(i), i])

        for _ in range(k):
            _, elem = heapq.heappop(heap)
        return elem

## Heap + Memoization
# TC: O(p' + n * logn + k * logn)
# SC: O(n)
