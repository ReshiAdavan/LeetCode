from typing import List
from collections import defaultdict

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        low, high = min(nums), max(nums)
        B = defaultdict(list)

        for num in nums:
            if num == high:
                index = n - 1
            else:
                index = ((num - low) * (n - 1)) // (high - low)
            B[index].append(num)

        buckets = []
        for i in range(n):
            if B[i]:
                buckets.append([min(B[i]), max(B[i])])

        output = 0
        for i in range(1, len(buckets)):
            output = max(output, (buckets[i][0] - buckets[i - 1][1]))

        return output

# TC: O(n)
# SC: O(n)
