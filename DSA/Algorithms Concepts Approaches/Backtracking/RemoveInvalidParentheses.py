from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        minr = self.minRemovals(s)
        res = set()

        def backtrack(i, open, curr, removals):
            if i >= len(s):
                if open == 0 and removals == minr:
                    res.add(curr)
                return

            char = s[i]

            # remove char
            if char in "()" and removals < minr:
                backtrack(i + 1, open, curr, removals + 1)

            # keep char
            if char == "(":
                backtrack(i + 1, open + 1, curr + char, removals)
            elif char == ")":
                if open > 0:
                    backtrack(i + 1, open - 1, curr + char, removals)
            else:
                backtrack(i + 1, open, curr + char, removals)

        backtrack(0, 0, "", 0)
        return list(res) if res else [""]

    def minRemovals(self, s: str) -> int:
        count, removals1 = 0, 0
        for char in s:
            if char == "(":
                count += 1
            elif char == ")":
                if count == 0:
                    removals1 += 1
                else:
                    count -= 1

        count, removals2 = 0, 0
        for char in reversed(s):
            if char == ")":
                count += 1
            elif char == "(":
                if count == 0:
                    removals2 += 1
                else:
                    count -= 1

        return removals1 + removals2

# TC: O(N + 2^N)
# SC: O(N)
