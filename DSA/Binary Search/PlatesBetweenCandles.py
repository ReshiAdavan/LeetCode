from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        lefts = []
        rights = []
        prefixes = []
        curSum = 0
        flag = False

        for index, char in enumerate(s):
            if char == "|" and not flag:
                lefts.append(index)
                flag = True
            elif char == "|" and flag:
                lefts.append(index)
                rights.append(index)
                prefixes.append(curSum)
            elif char == "*" and len(lefts):
                curSum += 1

        if len(lefts) > len(rights):
            lefts.pop()

        answer = []
        for l, r in queries:
            leftIdx = bisect_right(lefts, l - 1)
            rightIdx = bisect_left(rights, r + 1) - 1

            if leftIdx >= len(lefts) or rightIdx < 0 or leftIdx > rightIdx:
                answer.append(0)
            else:
                answer.append(prefixes[rightIdx] - (prefixes[leftIdx - 1] if leftIdx > 0 else 0))
        return answer

## Let N represent # of chars in s and Q represent # of queries 
# TC: O(N + QlogN)
# SC: O(N)
