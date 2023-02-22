class Solution(object):
    def subsetsWithDup(self, nums):
        subsetList = []
        subset = []
        
        def DFS(i): 
            if i >= len(nums):
                s = subset[:]
                s.sort()
                if s not in subsetList: 
                    subsetList.append(s)
                return
            subset.append(nums[i])
            DFS(i + 1)
            subset.pop()
            DFS(i + 1)
            
        DFS(0)
        return subsetList

# Beats 61.49% python submissions in runtime
# Beats 73.74% python submissions in memory usage