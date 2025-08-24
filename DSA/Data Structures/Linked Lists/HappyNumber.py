class Solution:
    def isHappy(self, n: int) -> bool:
        def computeNextNum(y):
            x = 0
            while y:
                lastDigit = y % 10
                x += lastDigit ** 2
                y //= 10
            return x

        slow = fast = n
        while True:
            slow = computeNextNum(slow)
            fast = computeNextNum(computeNextNum(fast))

            if fast == 1:
                return True
            if slow == fast:
                return False

# TC: O(log n)
# SC: O(1)
