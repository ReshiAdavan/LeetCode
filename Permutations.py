class Solution(object):
    def permute(self, nums):
        permsList = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            num = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(num)
            permsList.extend(perms)
            nums.append(num)
        return permsList

# Beats 93.59% python submissions in runtime
# Beats 16.29% python submissions in memory usage