class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        lower, upper = 1, maxSum
        result = maxSum

        def helper(target):
            total = sumFormula(target)
            leftLength = index + 1
            rightLength = n - index
            leftOffset = rightOffset = 0
            
            if leftLength < target:
                leftOffset = -sumFormula(target-leftLength)
            else:
                leftOffset = leftLength - target 
            
            if rightLength < target:
                rightOffset = -sumFormula(target-rightLength)
            else:
                rightOffset = rightLength - target

            ans = total + leftOffset + total + rightOffset - mid
            return ans <= maxSum

        def sumFormula(n):
            return n * (n + 1) // 2

        while lower <= upper: 
            mid = (lower + upper) // 2
            if helper(mid):
                result = mid
                lower = mid + 1
            else:
                upper = mid - 1
        return result

# Time Complexity: O(log(maxSum))
# Space Complexity: O(1)
# Beats 100% of python users in runtime (it runs in 1ms lol)
# Beats 57.56% of python users in memory usage
