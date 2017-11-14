import java.util.stream.IntStream;

/**
 * https://leetcode.com/problems/zigzag-conversion/description/
 */

public class ZigZagConversion {
    public String convert(String s, int numRows) {
        if (numRows == 1 || s.isEmpty()) {
            return s;
        }
        String res = "";

        int diff = 2*(numRows - 1);
        int index = 0;

        //0th row
        while (index < s.length()) {
            res += s.charAt(index);
            index += diff;
        }

        int midDiff;
        //1 to numRows-2
        for (int i = 1; i < numRows-1; i++) {
            midDiff = diff - 2*i;
            index = i;
            while (index < s.length()) {
                res += s.charAt(index);
                if (index+midDiff < s.length()) {
                    res += s.charAt(index+midDiff);
                }
                index += diff;
            }
        }

        //numRows-1 th row
        index = numRows-1;
        while (index < s.length()) {
            res += s.charAt(index);
            index += diff;
        }
        return res;
    }
}
