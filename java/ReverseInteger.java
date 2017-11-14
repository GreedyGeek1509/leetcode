public class ReverseInteger {

    static int reverse(int x) {
        boolean isNegative = (x<0);
        x = Math.abs(x);
        String reverse = new StringBuilder(String.valueOf(x)).reverse().toString();
        if (isNegative) {
            reverse = "-"+reverse;
        }
        try {
            return Integer.parseInt(reverse);
        } catch (NumberFormatException e) {
            return 0;
        }
    }

    public static void main(String[] args) {
        System.out.println(reverse(1534236469));
    }
}
