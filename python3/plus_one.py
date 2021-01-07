from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = [0]*(len(digits)+1)
        carry = 0
        idx = len(digits)
        first = True
        for d in digits[::-1]:
            sm = d+carry
            if first:
                sm = sm+1
                first = False
            res[idx] = (sm%10)
            carry = sm//10
            idx = idx-1
        if carry != 0:
            res[0] = carry
        else:
            res.pop(0)
        return res