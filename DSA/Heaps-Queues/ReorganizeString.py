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
    
# Time Complexity: O(n)
# Space Complexity: O(n)