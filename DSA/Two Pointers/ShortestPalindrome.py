class Solution:
    def shortestPalindrome(self, s: str) -> str:
        left = 0
        right = len(s) - 1

        while right > left:
            if self.isPalindromic(s[left: right + 1]):
                break
            else:
                right -= 1

        return (s[right + 1:])[::-1] + s[left:]

    def isPalindromic(self, s: str) -> bool:
        return s == s[::-1]

## Brute Force Two Pointer
# TC: O(n^2)
# SC: O(1)

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        prefix = 0 # integer conversion of prefix string in s
        suffix = 0 # integer conversion of suffix string in s
        base = 29 # base of the int number we are working with (use nearest larger prime)
        lastIndex = 0 # last index until we generate palindrome
        power = 1 # var for math comp
        mod = 10**9 + 7 # prevent overflow

        for i, c in enumerate(s):
            char = ord(c) - ord('a') + 1 # compute integer value of char

            prefix = (prefix * base) % mod # advance prefix
            prefix = (prefix + char) % mod # populate bit (left shift)
            suffix = (suffix + char * power) % mod # populate bit (right shift)
            power = (power * base) % mod # (advance power for suffix op)

            if prefix == suffix: # check if palindrome
                lastIndex = i
        return (s[lastIndex + 1:])[::-1] + s

## Rabin-Karp Algorithm
# TC: O(n)
# SC: O(1)

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        combined = s + "#" + s[::-1]
        lps = [0] * len(combined)

        for i in range(1, len(combined)):
            j = lps[i - 1]

            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]

            if combined[i] == combined[j]:
                j += 1

            lps[i] = j

        paliLen = lps[-1]
        return s[paliLen:][::-1] + s

## knuth-morris-pratt (KMP) Algorithm -> LPS
# TC: O(n)
# SC: O(n)
