class Solution:
    def decodeString(self, s):
        stack, length, result = [], len(s), ""

        for i in range(length): 
            if s[i] != ']': stack.append(s[i])
            else: 
                substr = ""
                while stack[-1] != "[": substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit(): k = stack.pop() + k
                stack.append(int(k) * substr)

        result += ''.join(stack)
        return result

# Beats 71.33% python submissions in runtime
# Beats 82.47% python submissions in memory usage

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == "]":
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr) 
            else:
                stack.append(s[i])
        return "".join(stack)
        
# Time Complexity: O(n)
# Space Complexity: O(n)
# Beats 100% of python users in runtime (it runs in 0ms lol)
# Beats 96.60% of python users in memory usage
