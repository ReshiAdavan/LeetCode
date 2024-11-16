from collections import heapq, Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        freqMap = Counter(hand)
        minH = list(freqMap.keys())
        heapq.heapify(minH)

        while minH:
            topElem = minH[0]
            for i in range(topElem, topElem + groupSize):
                if i not in freqMap:
                    return False
                freqMap[i] -= 1
                if freqMap[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True

# TC: O(nlogn)
# SC: O(n)
