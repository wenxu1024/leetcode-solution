import java.util.*;

public class Solution {
    public void rotate(int[] nums, int k) {
        int l = nums.length;
        int[] copy = new int[l];
	k = k % l;
        for(int i = 0; i < l; i ++) copy[i] = nums[i];
        for(int i = 0; i < k; i ++) {
            nums[i] = copy[l - k + i];
        }
        for(int i = k; i < l; i ++){
            nums[i] = copy[i - k];
        }
        return;
    }
	
    public static void main(String[] args) {
	int[] nums = {1,2,3,4,5,6,7};
	int n = 7;
	int k = 3;
	System.out.println(Arrays.toString(nums));
	Solution s = new Solution();
	s.rotate(nums, k);
	System.out.println(Arrays.toString(nums));
    }
}
