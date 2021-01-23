from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        length = len(nums)

        def find_pivot(beg: int, end: int) -> int:
            if not 0 <= beg <= end < length:
                return -1
            mid = (beg + end) // 2
            if mid+1 < length and nums[mid] > nums[mid+1]:
                return mid
            if mid > 0 and nums[mid-1] > nums[mid]:
                return mid-1
            p1 = find_pivot(beg, mid-1)
            if p1 != -1:
                return p1
            return find_pivot(mid+1, end)

        def binary_search(beg: int, end: int) -> bool:
            if beg > end:
                return False
            mid = (beg + end)//2
            if nums[mid] == target:
                return True
            if target < nums[mid]:
                return binary_search(beg, mid-1)
            return binary_search(mid+1, end)

        pivot = find_pivot(0, length-1)
        return binary_search(0, pivot) or binary_search(pivot+1, length-1)

if __name__ == '__main__':
    print(Solution().search([5, 5, 6, 1, 2, 2, 3, 3, 3, 4, 4, 5], 4))