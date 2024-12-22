class Solution(object):
    def isSubsequence(self, s, t): # s is a subsequence of t
        s_len, t_len = len(s), len(t) 
        if s_len > t_len: 
            return False
        if s_len == 0:
            return True
        val = 0
        for i in range(0, t_len):
            if val < s_len:
                if s[val] == t[i]:
                    val += 1
        return val == s_len

# Beats 97.39% python submissions in runtime
# Beats 8.98% python submissions in memory usage