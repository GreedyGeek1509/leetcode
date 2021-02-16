from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if numRows == 0:
            return res
        res.append([1])
        for i in range(1, numRows):
            prev = res[i-1]
            current = [1]
            for j in range(1, len(prev)):
                current.append(prev[j-1] + prev[j])
            current.append(1)
            res.append(current)
        return res