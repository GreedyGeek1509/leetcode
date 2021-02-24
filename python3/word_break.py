from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = []
        for i in range(length):
            dp.append([False]*length)
        # fill for length 1 substrings
        for i in range(length):
            dp[i][i] = s[i] in wordDict

        for sublength in range(2, length+1):
            for start_idx in range(length-sublength+1):
                end_idx = start_idx + sublength - 1
                dp[start_idx][end_idx] = s[start_idx:end_idx+1] in wordDict
                for k in range(start_idx, end_idx):
                    if not dp[start_idx][end_idx]:
                        dp[start_idx][end_idx] = dp[start_idx][k] and dp[k+1][end_idx]
                    else:
                        break

        return dp[0][length-1]