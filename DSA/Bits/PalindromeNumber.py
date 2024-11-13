class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        res = 0
        while res < x:
            LSD = x % 10
            res = res * 10 + LSD
            x //= 10
        return x == res or x == res // 10

# TC: O(n)
# SC: O(1)