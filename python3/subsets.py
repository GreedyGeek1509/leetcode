from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length, power_set, sofar = len(nums), [], []

        def back_track(idx: int) -> None:
            if idx == length:
                power_set.append(list(sofar))
                return
            sofar.append(nums[idx])
            back_track(idx+1)
            sofar.pop()
            back_track(idx+1)

        back_track(0)
        return power_set


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))