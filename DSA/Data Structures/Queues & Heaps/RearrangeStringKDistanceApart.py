from collections import Counter, deque, heapq

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        res = []
        counter = Counter(s)
        maxHeap = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(maxHeap)
        q = deque()

        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            res.append(char)
            q.append((freq + 1, char))

            if len(q) >= k:
                freq, char = q.popleft()
                if freq < 0:
                    heapq.heappush(maxHeap, (freq, char))

        return "".join(res) if len(res) == len(s) else ""

# TC: O(s * log(s))
# SC: O(s)
