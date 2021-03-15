from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        def find_min(left: int, right: int):
            if left == right or nums[left] < nums[right]:
                return nums[left]
            mid = (left + right)//2
            mid_1 = n-1 if mid == 0 else mid-1
            if nums[mid] < nums[mid_1]:
                return nums[mid]
            if mid+1 < n and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if mid != left and nums[left] > nums[mid_1]:
                return find_min(left, mid_1)
            return find_min(mid+1, right)
        return find_min(0, n-1)

if __name__ == '__main__':
    print(Solution().findMin([11,13,15,17]))