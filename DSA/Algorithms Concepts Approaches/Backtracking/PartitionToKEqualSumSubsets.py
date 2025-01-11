from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False

        sumPerGroup = total // k
        nums.sort(reverse=True)
        used = set()

        def backtrack(i, subsetSum, k):
            if k == 0:
                return True
            if subsetSum == sumPerGroup:
                return backtrack(0, 0, k - 1)

            for j in range(i, len(nums)):
                if j in used or subsetSum + nums[j] > sumPerGroup:
                    continue

                used.add(j)
                if backtrack(j + 1, subsetSum + nums[j], k):
                    return True
                used.remove(j)

                if subsetSum == 0:
                    return False

            return False
        return backtrack(0, 0, k)

# TC: O(nlogn + k * 2^n)
# SC: O(n)