from typing import List
from collections import defaultdict

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minAbsDiff = float("inf")
        absGroups = defaultdict(list)
        arr.sort()

        for i in range(1, len(arr)):
            minAbsDiff = min(minAbsDiff, abs(arr[i] - arr[i - 1]))

        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i - 1]) == minAbsDiff:
                absGroups[minAbsDiff].append([arr[i - 1], arr[i]])

        return absGroups[minAbsDiff]

# TC: O(nlogn)
# SC: O(n)
