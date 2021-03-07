from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        left_max, right_max = [0]*n, [0]*n
        left_max[0] = height[0]
        right_max[n-1] = height[n-1]

        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i-1])
            right_max[n-1-i] = max(height[n-1-i], right_max[n-i])

        volume = 0
        for i in range(n):
            mini = min(left_max[i], right_max[i])
            volume += (mini - height[i])

        return volume