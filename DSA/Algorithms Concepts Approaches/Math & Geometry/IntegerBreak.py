class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1

        threes = n // 3
        remainder = n % 3

        if remainder == 0:
            return 3 ** threes
        elif remainder == 1:
            return 4 * 3 ** (threes - 1)
        return 3 ** threes * 2

# Idea: Products are maximized when the factors are near the perfect square for n > 4
# Since there can be k >= 2 integers involved in the product, we want to maximize k and 
# break n into k 2's and 3's; 3's are preferred over 2's since 3^2 > 2^3

# Arguably it depends on the exnpontiation operation with base 3 and that takes mlogn,
# where m represents number of bits in n, and m ~ n here
# TC: O(1)

# SC: O(1)
