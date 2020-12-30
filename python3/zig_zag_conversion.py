# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or len(s) < 2 or numRows == 1:
            return s
        res = ''
        length = len(s)
        adder = 2*numRows-2
        for i in range(numRows):
            extra_needed = i != 0 and i != numRows-1
            looper = i
            while looper < length or looper-2*i < length:
                if extra_needed and 0 < looper - 2 * i < length:
                    res = res + s[looper-2*i]
                if looper < length:
                    res = res + s[looper]
                looper = looper+adder
        return res
