from typing import List
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        results = [0] * len(deck)
        q = deque(range(len(deck)))

        for card in deck:
            # get the next index we want to add to in results
            i = q.popleft()

            # assign card to that index in results
            results[i] = card

            # for the next index, move to end of queue
            if q:
                q.append(q.popleft())
        return results

# TC: O(nlogn + n)
# SC: O(n)
