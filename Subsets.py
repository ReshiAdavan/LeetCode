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