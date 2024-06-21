class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        mini, maxi = 1, 1

        for n in nums:
            tmp = maxi * n
            maxi = max(n * maxi, n * mini, n)
            mini = min(tmp, n * mini, n)
            res = max(res, maxi)
        return res

# Beats 86.06% of users with Python3 in runtime
# Beats 85.72% of users with Python3 in memory