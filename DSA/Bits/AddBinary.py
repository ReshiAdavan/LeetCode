class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n, m = len(a) - 1, len(b) - 1
        sumStr = []
        carry = 0

        while n >= 0 or m >= 0 or carry:
            digitA = int(a[n]) if n >= 0 else 0
            digitB = int(b[m]) if m >= 0 else 0

            total = digitA + digitB + carry
            carry = total // 2

            sumStr.append(str(total % 2))
            n -= 1
            m -= 1
        return ("".join(sumStr))[::-1]

# TC: O(N + M)
# SC: O(1) auxiliary and O(N + M) to store the solution
