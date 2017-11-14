/**
 * https://leetcode.com/problems/longest-palindromic-substring/description/
 */

public class LongestPalindromicSubstring {
    static String longestPalindrome(String s) {
        int len = s.length();
        int start=0, maxLength = 1;
        int l,h;

        for(int i=1; i<len; i++) {
            l = i-1;
            h = i;
            while (l >= 0 && h < len && s.charAt(l) == s.charAt(h)) {
                if (maxLength < (h-l+1)) {
                    start = l;
                    maxLength = h-l+1;
                }
                l--;
                h++;
            }

            l = i-1;
            h = i+1;
            while (l >= 0 && h < len && s.charAt(l) == s.charAt(h)) {
                if (maxLength < (h-l+1)) {
                    start = l;
                    maxLength = h-l+1;
                }
                l--;
                h++;
            }
        }
        return s.substring(start, start+maxLength);
    }

    public static void main(String[] args) {
        System.out.println(longestPalindrome("bb"));
    }
}
