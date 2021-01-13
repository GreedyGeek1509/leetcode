from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        length = m*n

        def get_row(mid: int) -> int:
            return mid//n

        def get_col(mid: int) -> int:
            return mid - n * (mid // n)

        beg, end = 0, length-1
        while 0 <= beg <= end < length:
            mid = (beg+end)//2
            row, col = get_row(mid), get_col(mid)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                beg = mid + 1
            else:
                end = mid - 1
        return False
