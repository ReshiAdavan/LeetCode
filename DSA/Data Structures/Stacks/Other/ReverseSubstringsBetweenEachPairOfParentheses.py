class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ")":
                substr = ""
                while stack[-1] != "(":
                    elem = stack.pop()
                    if len(elem) > 1:
                        elem = elem[::-1]
                    substr += elem
                stack.pop()
                stack.append(substr)
            else:
                stack.append(ch)
        return "".join(stack)

# TC: O(n^2)
# SC: O(n)

class Solution:
    def reverseParentheses(self, s: str) -> str:
        pair = {}
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i

        result = []
        i = 0
        direction = 1

        while i < len(s):
            if s[i] in '()':
                i = pair[i]
                direction *= -1
            else:
                result.append(s[i])
            i += direction
        return ''.join(result)

# TC: O(n)
# SC: O(n)