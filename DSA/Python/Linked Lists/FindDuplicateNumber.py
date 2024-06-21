class Solution(object):
    def findDuplicate(self, nums):
        s, f = 0, 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break

        s2 = 0
        while True:
            s = nums[s]
            s2 = nums[s2]
            if s == s2:
                return s

# Beats 70.35% python submissions in runtime
# Beats 78.68% python submissions in memory usage  