from collections import Counter, heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, ch] for ch, cnt in count.items()]
        heapq.heapify(maxHeap)

        res = ""
        prev = None
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            ct, ch = heapq.heappop(maxHeap)
            res += ch
            ct += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if ct != 0:
                prev = [ct, ch]
        return res
    
# Time Complexity: O(nlogn)
# Space Complexity: O(n)

from collections import Counter, heapq, deque

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        maxHeap = [(-f, c) for c, f in counter.items()]
        heapq.heapify(maxHeap)

        q = deque()
        res = []

        while maxHeap:
            f, c = heapq.heappop(maxHeap)
            res.append(c)
            q.append([f + 1, c])

            if len(q) >= 2:
                f, c = q.popleft()

                if f < 0:
                    heapq.heappush(maxHeap, (f, c))

        return "".join(res) if len(res) == len(s) else ""
    
# TC: O(nlogn)
# SC: O(n)
