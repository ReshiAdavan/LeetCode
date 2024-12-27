class Solution:
    def partitionString(self, s: str) -> int:
        res = 1
        seen = set()

        for ch in s:
            if ch not in seen:
                seen.add(ch)
            else:
                res += 1
                seen = set(ch)
        return res

# TC: O(n)
# SC: O(n)
