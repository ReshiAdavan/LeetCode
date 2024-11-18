from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = 1
        left = 0
        right = k - 1

        for i in range(1, right + 1):
            if nums[i] == nums[i - 1] + 1:
                count += 1

        while right < len(nums):
            res.append(nums[right] if count == k else -1)

            right += 1
            if right >= len(nums):
                break

            if nums[right] == nums[right - 1] + 1:
                count += 1

            if nums[left + 1] == nums[left] + 1:
                count -= 1
            left += 1

        return res

# TC: O(n)
# SC: O(n)