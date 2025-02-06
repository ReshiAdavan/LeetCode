from typing import List

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        prefix = [0]
        mask = 0

        for char in s:
            mask ^= 1 << (ord(char) - ord('a'))
            prefix.append(mask)

        results = []
        for l, r, k in queries:
            curMask = prefix[r + 1] ^ prefix[l]
            oddCount = bin(curMask).count('1')
            results.append(oddCount // 2 <= k)
        return results

# TC: O(N + Q)
# SC: O(N)
