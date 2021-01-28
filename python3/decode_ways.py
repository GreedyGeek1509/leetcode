class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        length = len(s)
        dp = [0]*length
        dp[0] = 1
        if s[1] == '0':
            if s[0] > '2':
                return 0
            dp[1] = 1
        elif '10' < s[:2] <= '26':
            dp[1] = 2
        else:
            dp[1] = 1

        for i in range(2, length):
            if s[i] == '0':
                if s[i-1] > '2' or s[i-1] < '1':
                    return 0
                dp[i] = dp[i-2]
            elif '10' < s[i-1:i+1] <= '26':
                dp[i] = dp[i-2] + dp[i-1]
            else:
                dp[i] = dp[i-1]
        return dp[length-1]