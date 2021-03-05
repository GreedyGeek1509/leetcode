from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]):
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if 0 <= j < len(nums) and nums[j] != nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        i = 0
        while i < len(nums):
            if nums[i] != i+1:
                break
            else:
                i += 1
        return i+1