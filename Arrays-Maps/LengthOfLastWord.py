class Solution(object):
    def lengthOfLastWord(self, s):
        res = s.split()
        return len(res[-1])

# Beats 89.14% python submissions in runtime
# Beats 74.57% python submissions in memory usage