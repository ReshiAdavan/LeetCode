class Solution(object):
    def isPalindrome(self, s):
        _s = ''.join(ch for ch in s if ch.isalnum())
        _s = _s.lower()
        if len(_s) <= 1:
            return True
        i = 0
        j = len(_s) - 1
        while i < j:
            if _s[i] != _s[j]:
                return False
            i += 1
            j -= 1
        return True

# Beats 54.60% python submissions in runtime
# Beats 63.68% python submissions in memory usage  