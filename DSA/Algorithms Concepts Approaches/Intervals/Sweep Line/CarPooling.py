from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pickupTimes, dropoffTimes = [], []
        for numPassengers, fromi, toi in trips:
            pickupTimes.append([fromi, numPassengers])
            dropoffTimes.append([toi, -numPassengers])

        pickupTimes.sort()
        dropoffTimes.sort()

        p, d = 0, 0
        cap = 0
        while p < len(pickupTimes):
            if pickupTimes[p][0] < dropoffTimes[d][0]:
                cap += pickupTimes[p][1]
                p += 1
            else:
                cap += dropoffTimes[d][1]
                d += 1
            if cap > capacity:
                return False
        return True

# TC: O(NlogN)
# SC: O(N)
