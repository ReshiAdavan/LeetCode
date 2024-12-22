from typing import List
from collections import Counter, heapq, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [[-count, task] for task, count in counter.items()]
        heapq.heapify(heap)
        q = deque()
        time = 0

        while heap or q:
            time += 1

            if heap:
                count, char = heapq.heappop(heap)
                if count < -1:
                    q.append([char, count + 1, time + n])

            if q and q[0][2] == time:
                char, count, _ = q.popleft()
                heapq.heappush(heap, [count, char])

        return time

# TC: O(nlogn)
# SC: O(n)
