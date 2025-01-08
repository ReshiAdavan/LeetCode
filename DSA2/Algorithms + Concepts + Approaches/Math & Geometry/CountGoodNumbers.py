class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        numOfEvenDigits = (n + 1) // 2
        numOfOddDigits = n // 2

        evenPart = pow(5, numOfEvenDigits, MOD)
        oddPart = pow(4, numOfOddDigits, MOD)

        return (evenPart * oddPart) % MOD

## TC and SC purely comes from computing pow()
# TC: O(log(numOfEvenDigits + numOfOddDigits)) => O(logn)
# SC: O(1)
