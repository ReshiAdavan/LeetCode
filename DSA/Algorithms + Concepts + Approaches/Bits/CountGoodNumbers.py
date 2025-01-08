class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        def mod_exp(x, y, mod):
            result = 1
            base = x % mod
            while y > 0:
                if y & 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                y >>= 1
            return result

        numOfEvenDigits = (n + 1) // 2
        numOfOddDigits = n // 2

        evenPart = mod_exp(5, numOfEvenDigits, MOD)
        oddPart = mod_exp(4, numOfOddDigits, MOD)

        return (evenPart * oddPart) % MOD

# TC: O(log(numOfEvenDigits + numOfOddDigits)) => O(logn)
# SC: O(1)
