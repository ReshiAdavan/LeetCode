class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        stack = []
        flips = 0

        for ch in s:
            # 10
            if stack and stack[-1] == "1" and ch == "0":
                stack.pop()
                flips += 1
            else:
                stack.append(ch)
        return flips

# TC: O(n)
# SC: O(n)
