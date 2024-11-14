class Solution(object):
    def isValid(self, s):
        S, M, i = [], [], 0
        H = {'(': ")", '[': "]", '{': "}"}
        while i < len(s):
            if s[i] in H:
                S.append(s[i])
                M.append(H[s[i]])
            else:
                if len(M) == 0:
                    return False
                if s[i] != M[-1]:
                    return False
                else:
                    S.pop()
                    M.pop()
            i += 1
        if len(S) != 0 and len(M) != 0:
            return False
        return True

# Beats 91.81% python submissions in runtime
# Beats 12.49% python submissions in memory usage

class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {")": "(", "]": "[", "}": "{"}
        stack = []
        for ch in s:
            # opening brackets
            if ch not in bracketMap:
                stack.append(ch)

            # closing brackets
            else:
                if not stack:
                    return False
                prevCh = stack.pop()
                if prevCh != bracketMap[ch]:
                    return False
        return True if len(stack) == 0 else False
