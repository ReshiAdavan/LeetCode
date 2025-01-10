from typing import List

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = 0
        for bit in data: 
            if bit == 1: ones += 1
        if ones == 0: return 0

        l, r, zeroCounter = 0, ones - 1, 0
        for i in range(l, r + 1):
            if data[i] == 0:
                zeroCounter += 1

        mini = zeroCounter
        while r < len(data):
            if data[l] == 0:
                zeroCounter -= 1
            l += 1
            r += 1
            if r >= len(data):
                return mini
            else:
                if data[r] == 0:
                    zeroCounter += 1
                mini = min(mini, zeroCounter)
        return mini

# Time Complexity: O(N)
# Space Complexity: O(1)
# Beats 43.93% of python users in runtime
# Beats 92.49% of python users in memory usage
