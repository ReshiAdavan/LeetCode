class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
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

# TC: O(n + nlogn + n) = O(nlogn)
# SC: O(n)
