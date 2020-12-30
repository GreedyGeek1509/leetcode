# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 2:
            return s
        max_so_far = 1
        max_idx = 0
        dp = set()
        length = len(s)
        for i in range(length):
            dp.add((i, i))
        for i in range(length-1):
            if s[i] == s[i+1]:
                max_so_far = 2
                max_idx = i
                dp.add((i, i+1))

        for k in range(3, length+1):
            for left in range(0, length-k+1):
                right = left+k-1
                if s[left] == s[right] and (left+1, right-1) in dp:
                    dp.add((left, right))
                    max_so_far = k
                    max_idx = left
        return s[max_idx:max_idx+max_so_far]