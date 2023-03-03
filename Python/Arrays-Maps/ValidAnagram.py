class Solution(object):
    def isAnagram(self, s, t):
        if len(t) != len(s):
            return False
        S, T = {}, {}
        i = 0
        while i < len(t):
            T[t[i]] = 1 + T.get(t[i], 0)
            S[s[i]] = 1 + S.get(s[i], 0)
            i += 1
        return S == T
    
# Beats 62.39% python submissions in runtime
# Beats 97.75% python submissions in memory usage  