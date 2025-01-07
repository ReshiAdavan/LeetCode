class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        prefix, suffix = p.split("*")
        if len(prefix) + len(suffix) > len(s):
            return False

        for i in range(len(s) - (len(prefix) + len(suffix)) + 1):
            if s[i: i + len(prefix)] == prefix:
                rem = s[i + len(prefix):]
                if len(rem) >= len(suffix) and (not len(suffix) or suffix in rem):
                    return True
        return False

# TC: O(n * m)
# SC: O(1)
