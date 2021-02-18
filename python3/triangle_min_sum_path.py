from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        depth, mini = len(triangle)
        mini = 2**31-1
        min_sum_tree = [[triangle[0][0]]]

        for level in range(1, depth):
            min_sum_tree.append([0]*(level+1))
            for cursor in range(level+1):
                prev_1 = min_sum_tree[level-1][cursor-1] if cursor > 0 else mini
                prev_2 = min_sum_tree[level-1][cursor] if cursor < level else mini
                min_sum_tree[level][cursor] = triangle[level][cursor] + min(prev_1, prev_2)

        return min(min_sum_tree[depth-1])


if __name__ == '__main__':
    print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))