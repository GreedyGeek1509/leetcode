from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict:
            return True
        length = len(s)
        dp = [False]*(length+1)
        dp[0] = True
        dct = set(wordDict)
        for i in range(1, length+1):
            if s[:i] in dct:
                dp[i] = True
                continue
            for j in range(i):
                if dp[j] and s[j:i] in dct:
                    dp[i] = True
                    break

        return dp[length]