class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splits = s.strip().split(' ')
        return len(splits[-1]) if len(splits) > 0 else 0