from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        counter = [0]*3
        for num in nums:
            counter[num] = counter[num]+1

        idx = 0
        for i in range(3):
            for j in range(counter[i]):
                nums[idx] = i
                idx = idx+1