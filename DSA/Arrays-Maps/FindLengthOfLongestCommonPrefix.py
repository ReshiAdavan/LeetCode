from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        prefixes = set()
        for n in arr1:
            while n and n not in prefixes:
                prefixes.add(n)
                n //= 10

        res = 0
        for m in arr2:
            while m and m not in prefixes:
                m //= 10
            if m in prefixes:
                res = max(res, len(str(m)))
        return res
    
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
