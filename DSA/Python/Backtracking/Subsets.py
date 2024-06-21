class Solution(object):
    def subsets(self, nums):
        subsetList = []
        subset = []

        def DFS(i):
            if i >= len(nums):
                subsetList.append(subset[:])
                return
            subset.append(nums[i])
            DFS(i + 1)
            subset.pop()
            DFS(i + 1)

        DFS(0)
        return subsetList   

# Beats 87.58% python submissions in runtime
# Beats 70.43% python submissions in memory usage

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        subset = []

        def dfs(step):
            if step >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[step])
            dfs(step + 1)

            subset.pop()
            dfs(step + 1)

        dfs(0)
        return res

# Beats 90.55% python submissions in runtime
# Beats 77.72% python submissions in memory usage