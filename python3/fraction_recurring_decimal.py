class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ''
        if numerator * denominator < 0:
            res += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        q = numerator//denominator
        res += str(q)
        r = numerator%denominator
        if r > 0:
            res += '.'
        r_idx = {}
        while r:
            if r in r_idx:
                res = res[:r_idx[r]] + '(' + res[r_idx[r]:] + ')'
                break
            r_idx[r] = len(res)
            res += str((r*10)//denominator)
            r = (r*10)%denominator
        return res


if __name__ == '__main__':
    print(Solution().fractionToDecimal(12, 7))