from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs, ms = 0, nums[0]
        for n in nums:
            if cs < 0:
                cs = 0
            cs = cs+n
            ms = max(cs, ms)
        return ms