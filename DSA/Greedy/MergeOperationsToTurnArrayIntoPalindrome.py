from typing import List
from collections import deque

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        q = deque(nums)
        operations = 0

        while len(q) >= 2:
            if q[0] > q[-1]:
                firstNum = q.pop()
                secondNum = q.pop()
                q.append(firstNum + secondNum)
                operations += 1
            elif q[0] < q[-1]:
                firstNum = q.popleft()
                secondNum = q.popleft()
                q.appendleft(firstNum + secondNum)
                operations += 1
            else:
                q.pop()
                q.popleft()
        return operations
