class Solution:
    def countSubstrings(self, s: str) -> int:
        def palindromes(left, right):
            count = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            return count

        ans = 0
        for i in range(len(s)):
            ans += palindromes(i, i)
            ans += palindromes(i, i + 1)
        return ans

## Expand-Around-Center Technique
# TC: O(n^2)
# SC: O(1)
