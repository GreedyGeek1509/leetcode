class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = dict()

        def dp(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                memo[(i, j)] = i == len(s)
                return memo[(i, j)]
            first_match = i < len(s) and p[j] in [s[i], '.']
            if j <= len(p)-2 and p[j+1] == '*':
                memo[(i, j)] = (first_match and dp(i+1, j)) or dp(i, j+2)
                return memo[(i, j)]
            else:
                memo[(i, j)] = first_match and dp(i+1, j+1)
                return memo[(i, j)]

        return dp(0, 0)
