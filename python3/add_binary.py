class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bin_map = {
            0: (0, 0),
            1: (0, 1),
            2: (1, 0),
            3: (1, 1)
        }
        carry = 0
        i, j = len(a)-1, len(b)-1
        res = ''
        while i >= 0 or j >= 0 or carry > 0:
            v1 = int(a[i]) if i >= 0 else 0
            v2 = int(b[j]) if j >= 0 else 0
            sm = v1 + v2 + carry
            carry = bin_map[sm][0]
            res = str(bin_map[sm][1]) + res
            i = i-1
            j = j-1
        return res