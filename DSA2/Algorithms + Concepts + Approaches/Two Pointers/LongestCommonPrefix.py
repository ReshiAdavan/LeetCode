from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def LCP(s1, s2) -> str:
            p1, p2 = 0, 0
            res = ""

            while p1 < len(s1) and p2 < len(s2):
                if s1[p1] == s2[p2]:
                    res += s1[p1]
                    p1 += 1
                    p2 += 1
                else:
                    break
            return res

        lcp = strs[0]
        for i in range(len(strs)):
            lcp = LCP(lcp, strs[i])
            if lcp == "":
                return lcp
        return lcp

## Horizontal Scanning
## Let N represent the number of strings in strs and K represent the length of the ith string in strs
# TC: O(N*K)
# SC: O(K) -> O(1) auxiliary and O(K) to store LCP

## Can also use vertical scan, binary search, or divide and conquer