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

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxi = 0
        char_count = {}

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            max_freq = max(char_count.values())

            while (right - left + 1) - max_freq > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            maxi = max(maxi, right - left + 1)
        return maxi
    
# TC: O(26n) => O(n)
# SC: O(26) => O(1)
