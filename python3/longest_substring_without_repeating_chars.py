# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) < 2:
            return len(s) if s else 0
        length = len(s)
        mem = {s[0]: 0}
        left, right, max_so_far = 0, 1, 1
        while right < length:
            if s[right] in mem and mem[s[right]] >= left:
                max_so_far = max(max_so_far, right-left)
                left = mem[s[right]]+1
            else:
                max_so_far = max(max_so_far, right-left+1)
            mem[s[right]] = right
            right = right+1
        return max_so_far
