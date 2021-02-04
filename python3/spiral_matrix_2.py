from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = []
        for i in range(n):
            result.append([0]*n)

        r, c, m, num = 0, 0, n, 1
        while r < m and c < n:
            for i in range(c, n):
                result[r][i] = num
                num += 1
            r = r + 1

            for i in range(r, m):
                result[i][n-1] = num
                num += 1
            n -= 1

            if r < m:
                for i in range(n-1, c-1, -1):
                    result[m-1][i] = num
                    num += 1
                m -= 1

            if c < n:
                for i in range(m-1, r-1, -1):
                    result[i][c] = num
                    num += 1
                c += 1
        return result
