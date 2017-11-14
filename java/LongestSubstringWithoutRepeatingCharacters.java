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
        int maxLength = 1;
        Set<Character> charSet = new HashSet<>();
        charSet.add(s.charAt(0));
        int currentIndex = 1;
        int len = s.length();
        int previousIndex = 0;
        while (currentIndex < len && len - previousIndex > maxLength) {
            if (charSet.contains(s.charAt(currentIndex))) {
                charSet.remove(s.charAt(previousIndex));
                previousIndex++;
            } else {
                charSet.add(s.charAt(currentIndex));
                maxLength = Math.max(maxLength, currentIndex-previousIndex+1);
                currentIndex++;
            }
        }
        return maxLength;
    }

    public static void main(String[] args) {
        System.out.println(lengthOfLongestSubstring(""));
    }
}
