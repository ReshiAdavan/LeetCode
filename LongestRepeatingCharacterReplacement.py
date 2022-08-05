class Solution(object):
    def characterReplacement(self, s, k):
        if len(s) <= 1: 
            return len(s)
        
        count, result = {}, 0
        l, maxi= 0, 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxi = max(maxi, count[s[r]])

            if (r - l + 1) - maxi > k:
                count[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)
        return result

# Beats 82.28% python submissions in runtime
# Beats 10.21% python submissions in memory usage 