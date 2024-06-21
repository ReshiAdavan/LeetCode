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