class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        res = 0

        for char in s:
            if char == "(":
                count += 1
            elif count > 0:
                count -= 1
            else:
                res += 1

        count = 0

        for char in reversed(s):
            if char == ")":
                count += 1
            elif count > 0:
                count -= 1
            else:
                res += 1

        return res

# TC: O(n)
# SC: O(1)
