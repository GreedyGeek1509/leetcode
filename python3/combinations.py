from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums_so_far = []

        def back_track(len_so_far: int, current_idx: int) -> None:
            if len_so_far == k:
                res.append(list(nums_so_far))
                return
            if n - current_idx + 1 < k - len_so_far:
                return
            nums_so_far.append(current_idx)
            back_track(len_so_far+1, current_idx+1)
            nums_so_far.pop()
            back_track(len_so_far, current_idx+1)

        back_track(0, 1)
        return res


if __name__ == '__main__':
    sol = Solution().combine(4, 2)
    for i in sol:
        print(i)
