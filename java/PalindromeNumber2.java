public class PalindromeNumber2 {
    public boolean isPalindrome(int x) {
        String xStr = String.valueOf(x);
        String xRev = (new StringBuffer(xStr)).reverse().toString();
        return xStr.equals(xRev);
    }
}
