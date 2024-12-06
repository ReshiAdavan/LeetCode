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

            # move j pointer back if we can and if chars dont match
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            
            # increment if they do match
            if combined[i] == combined[j]:
                j += 1

            lps[i] = j

        # longest palindromic prefix that is also a suffix length
        paliLen = lps[-1]

        # prepend the reversed leftover characters to s
        return s[paliLen:][::-1] + s

## knuth-morris-pratt (KMP) Algorithm -> LPS
# TC: O(n)
# SC: O(n)

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        combinedStr = s + "#" + s[::-1]
        n = len(combinedStr)
        z = [0 for _ in range(n)]
        left = right = paliLen = 0

        for i in range(1, n):
            # If the current index i lies within the Z-box, use previously computed values
            if i <= right:
                z[i] = min(right - i + 1, z[i - left])

            # Expand the match between the prefix of combined-string and the substring starting at i by incrementing z[i]
            while i + z[i] < n and combinedStr[z[i]] == combinedStr[i + z[i]]:
                z[i] += 1

            # Update the Z-box boundaries (l, r) if the new match goes beyond the current boundary
            if i + z[i] - 1 > right:
                left, right = i, i + z[i] - 1

        # Z-value that matches the suffix length (n - i) is the longest palindromic prefix of s
        for i in range(n):
            if z[i] == n - i:
                paliLen = z[i]
                break
        
        # prepend the reversed leftover characters to s
        return s[paliLen:][::-1] + s


## Z Algorithm
# TC: O(n)
# SC: O(n)
