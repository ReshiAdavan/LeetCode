class Solution(object):
    def longestPalindrome(self, s):
        stringLength = len(s)
        if stringLength == 1: 
            return s
        LPS = ""
        LPSLength = 0

        for i in range(stringLength):
            l, r = i, i
            while l >= 0 and r < stringLength and s[l] == s[r]:
                if (r - l + 1) > LPSLength:
                    LPS = s[l : r + 1]
                    LPSLength = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < stringLength and s[l] == s[r]:
                if (r - l + 1) > LPSLength:
                    LPS = s[l : r + 1]
                    LPSLength = r - l + 1
                l -= 1
                r += 1

        return LPS

# Beats 89.24% python submissions in runtime
# Beats 99.86% python submissions in memory usage
