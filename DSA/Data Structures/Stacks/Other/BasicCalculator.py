class Solution:
    def calculate(self, s: str) -> int:
        cur = 0
        res = 0
        sign = 1
        stack = []

        for ch in s:
            # computation
            if ch.isdigit():
                cur = cur * 10 + int(ch)
            elif ch in ["+", "-"]:
                res += sign * cur
                sign = 1 if ch == "+" else -1
                cur = 0
            # storing state
            elif ch == "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            # applying state
            elif ch == ")":
                res += sign * cur
                res *= stack.pop()
                res += stack.pop()
                cur = 0
            # whitespaces
            else:
                pass
                # nothing
        return res + sign * cur

# TC: O(n)
# SC: O(n)
