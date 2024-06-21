class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1:
            return len(s)
        p, L, i = [s[0]], 1, 1 
        while i < len(s):
            if s[i] not in p:
                p.append(s[i])
                i += 1
            else:
                p.pop(0)
            if L < len(p):
                L += 1
        return L

# Beats 49.39% python submissions in runtime
# Beats 53.56% python submissions in memory usage  