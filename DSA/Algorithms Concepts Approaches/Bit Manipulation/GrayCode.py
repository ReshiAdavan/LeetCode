from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]

        for i in range(n):
            currentLen = len(result)
            for j in range(currentLen - 1, -1, -1):
                result.append(result[j] | (1 << i))

        return result

# TC: O(2^n)
# SC: O(2^n)
