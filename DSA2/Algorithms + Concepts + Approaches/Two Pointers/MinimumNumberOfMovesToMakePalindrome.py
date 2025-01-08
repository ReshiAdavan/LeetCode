class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        left, right = 0, len(s) - 1
        swaps = 0

        while left < right:
            if s[left] == s[right]:
                left, right = left + 1, right - 1
            else:
                # match left char
                k = right
                while k > left and s[k] != s[left]:
                    k -= 1

                # if no match
                if k == left:
                    swaps += 1
                    s[left], s[left + 1] = s[left + 1], s[left]

                # if match
                else:
                    while k < right:
                        s[k], s[k + 1] = s[k + 1], s[k]
                        k += 1
                        swaps += 1
                    left, right = left + 1, right - 1
        return swaps

# TC: O(n^2) worst case
# SC: O(n)

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        swaps = 0
        while s:
            i = s.index(s[-1])
            if i == len(s) - 1:
                swaps += i / 2
            else:
                swaps += i
                s.pop(i)
            s.pop()
        return int(swaps)

# TC: O(n^2)
# SC: O(n)
