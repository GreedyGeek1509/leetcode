/**
 * https://leetcode.com/problems/add-two-numbers/description/
 */

class ListNode {
     int val;
     ListNode next;
     ListNode(int x) { val = x; }
}

public class AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode lp1, ListNode lp2) {
        int sum = lp1.val + lp2.val;
        lp1 = lp1.next;
        lp2 = lp2.next;
        int carry = sum/10;
        ListNode result = new ListNode(sum%10);
        ListNode lp3 = result;
        while (lp1 != null || lp2 != null) {
            sum = lp1 == null ? 0:lp1.val;
            sum += lp2 == null ? 0:lp2.val;
            sum += carry;
            carry = sum/10;
            lp3.next = new ListNode(sum%10);
            lp3 = lp3.next;
            lp1 = lp1 == null ? null:lp1.next;
            lp2 = lp2 == null ? null:lp2.next;
        }
        if (carry > 0) {
            lp3.next = new ListNode(carry%10);
            if (carry > 10) {
                lp3 = lp3.next;
                lp3.next = new ListNode(carry/10);
            }
        }
        return result;
    }
}
