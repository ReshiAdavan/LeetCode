## Recursive Memoization

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        cache, freqMap = {}, {}
        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1
        nums = sorted(list(set(nums)))

        def dfs(i):
            if i >= len(nums):
                return 0

            if i in cache:
                return cache[i]

            # choose to delete and earn
            earn = nums[i]

            nextIndex = i + 1
            while nextIndex < len(nums) and nums[nextIndex] == earn + 1:
                nextIndex += 1

            deleteAndEarn = earn * freqMap[earn] + dfs(nextIndex)

            # skip
            skip = dfs(i + 1)

            # take best of the two
            cache[i] = max(deleteAndEarn, skip)
            return cache[i]
        
        return dfs(0)

# Time Complexity: O(n + m + nlogn) = O(nlogn) 
# Beats 84.42% of python3 users in runtime
# Beats 23.26% of python3 users in memory
