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
