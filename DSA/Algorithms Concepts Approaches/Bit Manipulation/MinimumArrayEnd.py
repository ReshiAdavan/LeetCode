class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        for _ in range(n - 1):
            res = (res + 1) | x
        return res
    
# TC: O(n)
# SC: O(1)

## I personally dont understand this optimized solution, but it basically has to do with the fact that
## we dont need to necessairily count by 1, and we can keep the bits enforced by x static, and can separately modify, 
## the other bits until we get our answer.
##
## This solution, although using a loop, doesnt require us to iterate up to n times, but at most 65 times b/c we iterate
## until overflow of an integer in python (aka 64), hence why TC is log 2-based n 

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        i_x = 1
        i_n = 1

        while i_n < n:
            if i_x & x == 0:
                if i_n & (n - 1):
                    res |= i_x
                i_n <<= 1
            i_x <<= 1
        return res

# TC: O(log_2(n))
# SC: O(1)
