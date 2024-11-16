class Solution(object):
    def checkInclusion(self, s1, s2):
        S1, S2 = [0] * 26, [0] * 26

        for c in s1:
            S1[ord(c) - ord('a')] += 1

        l = 0

        for r in range(len(s2)):
            if r - l + 1 <= len(s1):
                S2[ord(s2[r]) - ord('a')] += 1
                if S1 == S2:
                    return True
            else:
                S2[ord(s2[l]) - ord('a')] -= 1
                l += 1
                S2[ord(s2[r]) - ord('a')] += 1
                if S1 == S2:
                    return True
        return False

# Beats 99.59% python submissions in runtime
# Beats 19.62% python submissions in memory usage  

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        S1 = Counter(s1)
        window = {}
        left = 0

        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right], 0) + 1

            if right - left + 1 > len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1

            if S1 == window:
                return True
        return False

    
# TC: O(26n)
# SC: O(n) => Sure its O(26) b/c of the bound on alphabet size but it depends on size of s2

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqCountS1 = Counter(s1)
        freqCountWindow = {}
        matches = 0
        left = 0

        for right in range(len(s2)):
            freqCountWindow[s2[right]] = freqCountWindow.get(s2[right], 0) + 1

            if s2[right] in freqCountS1 and freqCountWindow[s2[right]] == freqCountS1[s2[right]]:
                matches += 1

            if right - left + 1 > len(s1):
                if s2[left] in freqCountS1 and freqCountWindow[s2[left]] == freqCountS1[s2[left]]:
                    matches -= 1
                freqCountWindow[s2[left]] -= 1
                if freqCountWindow[s2[left]] == 0:
                    del freqCountWindow[s2[left]]
                left += 1

            if matches == len(freqCountS1):
                return True

        return False

# TC: O(n)
# SC: O(26) => Sure its O(26) b/c of the bound on alphabet size but it depends on size of s2