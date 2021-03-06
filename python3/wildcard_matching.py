class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                memo[(i, j)] = (i == len(s))
                return i == len(s)
            if i == len(s):
                ans = (p[j] == '*') and dp(i, j+1)
                memo[(i, j)] = ans
                return ans
            first_match = p[j] in [s[i], '?', '*']
            if p[j] == '*':
                ans = first_match and (dp(i+1, j+1) or dp(i+1, j) or dp(i, j+1))
            else:
                ans = first_match and dp(i+1, j+1)
            memo[(i, j)] = ans
            return ans

        return dp(0, 0)