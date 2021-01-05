class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        memo = []
        for i in range(m):
            memo.append([0]*n)
        for i in range(m):
            memo[i][0] = 1
        for i in range(n):
            memo[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = memo[i-1][j] + memo[i][j-1]
        return memo[m-1][n-1]
        #return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)


if __name__ == '__main__':
    print(Solution().uniquePaths(3, 2))
    print(Solution().uniquePaths(7, 3))