class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lookup = {}
        for i, c in enumerate(s):
            lookup[c] = i

        vis = set()
        stack = []

        for i, char in enumerate(s):
            if char in vis:
                continue

            while stack and stack[-1][0] > char and i < lookup[stack[-1][0]]:
                lastChar, _ = stack.pop()
                vis.remove(lastChar)

            stack.append([char, i])
            vis.add(char)

        res = []
        for char, _ in stack:
            res.append(char)
        return "".join(res)

# TC: O(n)
# SC: O(n)
