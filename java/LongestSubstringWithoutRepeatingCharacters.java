import java.util.HashSet;
import java.util.Set;

/**
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
 */

public class LongestSubstringWithoutRepeatingCharacters {
    static int lengthOfLongestSubstring(String s) {
        if (s == null || s.isEmpty()) {
            return 0;
        }
        int res = 1;
        Set<Character> charSet = new HashSet<>();
        charSet.add(s.charAt(0));
        int currentIndex = 1;
        int len = s.length();
        int previousIndex = 0;
        while (currentIndex < len && len - previousIndex > res) {
            if (charSet.contains(s.charAt(currentIndex))) {
                charSet.remove(s.charAt(previousIndex));
                previousIndex++;
            } else {
                charSet.add(s.charAt(currentIndex));
                res = Math.max(res, currentIndex-previousIndex+1);
                currentIndex++;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        System.out.println(lengthOfLongestSubstring(""));
    }
}
