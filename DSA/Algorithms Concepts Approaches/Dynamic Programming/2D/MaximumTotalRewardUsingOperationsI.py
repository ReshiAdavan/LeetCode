from typing import List

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        cache = {}

        def memo(i, curSum):
            if (i, curSum) in cache:
                return cache[(i, curSum)]
            if i >= len(rewardValues):
                return curSum

            if rewardValues[i] > curSum:
                cache[(i, curSum)] = max(
                    memo(i + 1, curSum + rewardValues[i]),
                    memo(i + 1, curSum)
                )
            else:
                cache[(i, curSum)] = memo(i + 1, curSum)
            return cache[(i, curSum)]

        return memo(0, 0)

## Top-down memoization; MLE
## Let N rep. # of reward values, M rep. sum(reward values)
# TC: O(N*M)
# SC: O(N*M)

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        dp = {0}

        for reward in rewardValues:
            newRewards = set()
            for prevReward in dp:
                if reward > prevReward:
                    newRewards.add(prevReward + reward)
            dp.update(newRewards)
        return max(dp)

## Bottom-up DP
# TC: O(N*M)
# SC: O(M)
