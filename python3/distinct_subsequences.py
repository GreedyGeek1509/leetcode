class Solution:
    def numDistinct(self, s: str, t: str):
        s_len, t_len = len(s), len(t)
        dp = {}
        def solve(s_idx: int, t_idx: int) -> int:
            if (s_idx, t_idx) in dp:
                return dp[(s_idx, t_idx)]
            if t_idx == t_len:
                dp[(s_idx, t_idx)] = 1
                return dp[(s_idx, t_idx)]
            if s_idx == s_len:
                dp[(s_idx, t_idx)] = 0
                return dp[(s_idx, t_idx)]
            if s[s_idx] == t[t_idx]:
                ans = solve(s_idx+1, t_idx+1) + solve(s_idx+1, t_idx)
            else:
                ans = solve(s_idx+1, t_idx)
            dp[(s_idx, t_idx)] = ans
            return ans

        return solve(0, 0)