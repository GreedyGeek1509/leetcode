from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 3:
            return length
        result, first, freed_idx, running_num, running_counter = length, True, length, nums[0], 1
        for i in range(1, length):
            if nums[i] == running_num:
                running_counter = running_counter+1
                if running_counter > 2:
                    result = result-1
                    if first:
                        freed_idx = i
                        first = False
                elif freed_idx < i:
                    nums[freed_idx] = running_num
                    freed_idx = freed_idx+1
            else:
                running_num = nums[i]
                running_counter = 1
                if freed_idx < i:
                    nums[freed_idx] = running_num
                    freed_idx = freed_idx+1
        return result