public class PalindromeNumber {
    int[] powerTen = {1, 10, 100, 1000, 10000,
            100000, 1000000, 10000000, 100000000,
            1000000000};

    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int numDigits;
        for (numDigits = 9; numDigits >= 0 && x/powerTen[numDigits] == 0; numDigits--);
        while (numDigits > 0) {
            if (x%10 != x/powerTen[numDigits]) {
                return false;
            }
            x %= powerTen[numDigits];
            x /= 10;
            numDigits -= 2;
        }
        return true;
    }
}
