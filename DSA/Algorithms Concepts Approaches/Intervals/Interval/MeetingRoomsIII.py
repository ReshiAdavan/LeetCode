from typing import List
from collections import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        roomsCount = [0] * n
        availableRooms = list(range(n))
        occupiedRooms = []

        for start, end in meetings:
            # free rooms once they become available
            while occupiedRooms and occupiedRooms[0][0] <= start:
                _, room = heapq.heappop(occupiedRooms)
                heapq.heappush(availableRooms, room)

            # if there are available rooms, allocate a meeting
            if availableRooms:
                room = heapq.heappop(availableRooms)
                heapq.heappush(occupiedRooms, [end, room])

            # allocate a meeting at the time once a meeting becomes available
            else:
                endTime, room = heapq.heappop(occupiedRooms)
                heapq.heappush(occupiedRooms, [endTime + (end - start), room])
            roomsCount[room] += 1

        return roomsCount.index(max(roomsCount))

# N = # of rooms, M = # of meetings
# TC: O(mlogm + mlogn)
# SC: O(n)
