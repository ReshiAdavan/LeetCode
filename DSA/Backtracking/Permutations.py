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

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(step):
            if step == len(nums):
                res.append(nums.copy())
                return

            for i in range(step, len(nums)):
                nums[step], nums[i] = nums[i], nums[step]
                dfs(step + 1)
                nums[step], nums[i] = nums[i], nums[step]
            
        dfs(0)
        return res

# Beats 97.94% python submissions in runtime
# Beats 77.54% python submissions in memory usage
