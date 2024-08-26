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

## Dynamic Programming

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freqMap = {}
        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1
        nums = sorted(list(set(nums)))

        earn1, earn2 = 0, 0 
        for i in range(len(nums)):
            curEarn = nums[i] * freqMap[nums[i]]

            if i > 0 and nums[i] == nums[i - 1] + 1:
                temp = earn2
                earn2 = max(curEarn + earn1, earn2)
                earn1 = temp
            else:
                temp = earn2
                earn2 = curEarn + earn2
                earn1 = temp
        return earn2

# Time Complexity: O(n + nlogn) = O(nlogn)
# Beats 81.14% of python3 users in runtime
# Beats 40.12% of python3 users in memory
