class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        N, M = len(num1) - 1, len(num2) - 1
        carry = 0
        res = ""

        while N >= 0 or M >= 0:
            i, j = 0, 0
            if N >= 0:
                i = ord(num1[N]) - 48
                N -= 1

            if M >= 0:
                j = ord(num2[M]) - 48
                M -= 1
            tmp = i + j + carry
            if tmp > 9:
                carry = 1
            else:
                carry = 0
            res = str(tmp)[-1] + res
        if carry:
            res = "1" + res
        return res
    
# TC: O(N + M)
# SC: O(1)
