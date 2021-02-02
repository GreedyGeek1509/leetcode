class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        # i being the number of nodes in the bst
        for i in range(2, n+1):
            # j being the root of the bst with i nodes
            for j in range(1, i+1):
                dp[i] = dp[i] + (dp[j-1]*dp[i-j])
        return dp[n]

