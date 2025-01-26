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