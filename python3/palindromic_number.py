# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        stk = []
        dup = x
        while dup != 0:
            stk.append(dup % 10)
            dup = dup//10
        length = len(stk)
        for i in range(length//2):
            if stk.pop() != x % 10:
                return False
            x = x//10
        return True

