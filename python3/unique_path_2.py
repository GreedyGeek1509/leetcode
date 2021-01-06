from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = []
        for i in range(m):
            memo.append([0]*n)
        memo[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                memo[i][0] = memo[i-1][0]
            else:
                memo[i][0] = 0
        for i in range(1, n):
            if obstacleGrid[0][i] == 0:
                memo[0][i] = memo[0][i-1]
            else:
                memo[0][i] = 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    memo[i][j] = memo[i-1][j] + memo[i][j-1]
                else:
                    memo[i][j] = 0
        return memo[m-1][n-1]

