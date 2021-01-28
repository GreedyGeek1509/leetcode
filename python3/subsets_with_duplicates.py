from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        power_set, result = set(), list()
        nums.sort()
        length = len(nums)

        def back_track(cursor: int, rl: List[int]):
            if cursor == length:
                t = tuple(rl)
                if t not in power_set:
                    power_set.add(t)
                    result.append(list(rl))
                return
            rl.append(nums[cursor])
            back_track(cursor+1, rl)
            rl.pop()
            back_track(cursor+1, rl)

        back_track(0, [])
        return result