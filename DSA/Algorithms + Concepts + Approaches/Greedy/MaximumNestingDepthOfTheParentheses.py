class Solution:
    def maxDepth(self, s: str) -> int:
        curBracketDepth = 0
        maxiDepth = 0

        for ch in s:
            if ch == "(":
                curBracketDepth += 1
            elif ch == ")":
                curBracketDepth -= 1
            maxiDepth = max(maxiDepth, curBracketDepth)
        return maxiDepth

# TC: O(n)
# SC: O(1)
