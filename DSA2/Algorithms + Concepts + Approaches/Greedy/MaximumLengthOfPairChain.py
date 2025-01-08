from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        maxPairLengthChain = 1
        end = pairs[0][1]

        for i in range(1, len(pairs)):
            if end < pairs[i][0]:
                maxPairLengthChain += 1
                end = pairs[i][1]
        return maxPairLengthChain

# TC: O(nlogn)
# SC: O(n)
