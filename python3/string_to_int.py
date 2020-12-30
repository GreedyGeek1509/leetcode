# https://leetcode.com/problems/string-to-integer-atoi/submissions/

class Solution:
    def myAtoi(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        length = len(s)
        cursor = 0
        while cursor < length and s[cursor] == ' ':
            cursor = cursor+1

        negative = False
        result = 0

        if cursor == length:
            return result

        if s[cursor] == '+':
            cursor = cursor+1
        elif s[cursor] == '-':
            negative = True
            cursor = cursor+1

        min_int = -2**31
        max_int = -min_int - 1
        zero_ord = ord('0')

        while cursor < length and '0' <= s[cursor] <= '9':
            result = result*10 + ord(s[cursor]) - zero_ord
            cursor = cursor+1

        if negative:
            result = -result
        if result > max_int:
            return max_int
        if result < min_int:
            return min_int
        return result
