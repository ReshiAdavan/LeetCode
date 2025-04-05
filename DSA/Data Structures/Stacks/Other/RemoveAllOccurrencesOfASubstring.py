class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        k = len(part)
        for char in s:
            stack.append(char)
            if stack and "".join(stack[-k:]) == part:
                for _ in range(k):
                    stack.pop()
        return "".join(stack)

## Let n rep. len(s) and k rep. len(part)
# TC: O(n * k)
# SC: O(n)
