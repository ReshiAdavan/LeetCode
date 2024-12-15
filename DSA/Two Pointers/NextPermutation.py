from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = None
        for i in range(len(nums) - 2, -1, -1):
            if nums[i + 1] > nums[i]:
                pivot = i
                break
        # if break never happens, runs this condition
        # if the entire array is sorted in desc order
        else:
            nums.reverse()
            return

        swap = len(nums) - 1
        while nums[swap] <= nums[pivot]:
            swap -= 1

        nums[pivot], nums[swap] = nums[swap], nums[pivot]
        nums[pivot + 1:] = reversed(nums[pivot + 1:])
        return

# TC: O(n)
# SC: O(1)
