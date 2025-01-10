from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        lower = 0
        upper = len(citations)
        HIndex = lower

        while lower <= upper:
            middle = (lower + upper) // 2
            if self.validIndex(citations, middle):
                HIndex = middle
                lower = middle + 1
            else:
                upper = middle - 1
        return HIndex

    def validIndex(self, citations: List[int], index: int) -> bool:
        count = 0
        for citation in citations:
            if citation >= index:
                count += 1
        return count >= index

# TC: O(n*logn)
# SC: O(1) auxillary
