/***
 * https://leetcode.com/problems/string-to-integer-atoi/description/
 */

public class StringToInteger {
    public int myAtoi(String str) {
        if (null == str) {
            return 0;
        }
        str = str.trim();
        if ("".equals(str)) {
            return 0;
        }
        int res = 0, i = 0, limit = -Integer.MAX_VALUE;
        int len = str.length();
        boolean isNegative = false;
        if (str.charAt(0) < '0') {
            if (str.charAt(0) == '-') {
                isNegative = true;
                limit = Integer.MIN_VALUE;
            } else if (str.charAt(0) != '+') {
                return 0;
            }
            i++;
        }
        int nearLimit = limit/10;
        int digit;
        while (i < len && str.charAt(i) >= '0' && str.charAt(i) <= '9') {
            if (res < nearLimit) {
                return isNegative ? Integer.MIN_VALUE :Integer.MAX_VALUE;
            }
            res *= 10;
            digit = Character.digit(str.charAt(i++), 10);
            if (res < limit + digit) {
                return isNegative ? Integer.MIN_VALUE : Integer.MAX_VALUE;
            }
            res -= digit;
        }
        return isNegative ? res : -res;
    }
}