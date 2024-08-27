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

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        cur = []
        nums.sort()

        def dfs(step):
            if step >= len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[step])
            dfs(step + 1)
            cur.pop()
                        
            k = step
            while k < len(nums) - 1:
                if nums[k] == nums[k + 1]:
                    k += 1
                else:
                    break
            step = k
            dfs(step + 1)

        dfs(0)
        return res

# Beats 98.03% python submissions in runtime
# Beats 90.36% python submissions in memory usage
