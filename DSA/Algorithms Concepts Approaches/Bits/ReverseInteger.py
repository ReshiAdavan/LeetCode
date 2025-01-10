class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x *= -1

        MAX = 2**31 - 1
        MIN = 2**31
        y = 0

        while x > 0:
            r = x % 10
            x //= 10

            if sign == 1 and (y > MAX // 10 or (y == MAX // 10 and r > MAX % 10)):
                return 0
            if sign == -1 and (y > MIN // 10 or (y == MIN // 10 and r > MIN % 10)):
                return 0

            y = y * 10 + r

        return sign * y

# TC: O(n)
# SC: O(n)
