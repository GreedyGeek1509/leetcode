import java.util.HashMap;
import java.util.Map;

/**
 * https://leetcode.com/problems/two-sum/description/
 */

public class TwoSum {
    static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> diffIndexMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (diffIndexMap.get(target-nums[i]) != null) {
                return new int[]{diffIndexMap.get(target - nums[i]), i};
            }
            diffIndexMap.put(nums[i], i);
        }
        return new int[]{};
    }

    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int result[] = twoSum(nums, target);
        System.out.println(result[0]+", "+result[1]);
    }
}
