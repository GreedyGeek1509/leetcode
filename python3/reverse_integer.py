# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x
        min_int = -2**31
        max_int = -min_int - 1
        negative = False
        if x < 0:
            negative = True
            x = -x
        result = 0
        while x > 0:
            result = result*10 + x % 10
            x = x//10
        if negative:
            return -result if -result >= min_int else 0
        return result if result <= max_int else 0


if __name__ == '__main__':
    print(Solution().reverse(-1234))