from collections import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        maxHeap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, [count, char])

        while maxHeap:
            freq, char = heapq.heappop(maxHeap)

            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break

                freq2, char2 = heapq.heappop(maxHeap)
                res.append(char2)
                if freq2 < -1:
                    heapq.heappush(maxHeap, [freq2 + 1, char2])
                heapq.heappush(maxHeap, [freq, char])

            else:
                res.append(char)
                if freq < -1:
                    heapq.heappush(maxHeap, [freq + 1, char])

        return "".join(res)

# TC: O((a + b + c) * log(a + b + c))
# SC: O(a + b + c)
