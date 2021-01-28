from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0, 1]

        for i in range(1, n):
            rl = len(res)
            for j in reversed(range(rl)):
                res.append(res[j] ^ (1 << i))
        return res


if __name__ == '__main__':
    print(Solution().grayCode(3))