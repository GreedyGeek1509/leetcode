from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        mini, start_idx, current = 0, 0, 0
        for i in range(len(gas)):
            current += (gas[i] - cost[i])
            if current < mini:
                mini = current
                start_idx = i+1
        return start_idx%len(gas) if current >= 0 else -1