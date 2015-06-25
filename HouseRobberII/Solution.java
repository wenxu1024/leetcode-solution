public class Solution {
    public int rob(int[] nums) {
        int l = nums.length;
        if (l == 0) return 0;
        if (l == 1) return nums[0];
        if (l == 2) return Math.max(nums[0], nums[1]);
        return Math.max(robLinear(nums, 2, l - 2) + nums[0], robLinear(nums, 1, l - 1));
    }
    
    public int robLinear(int[] nums, int i, int j) {
        int l = nums.length;
        if (j < i) return 0;
        int[] C = new int[l];
        if (j == i) return nums[i];
        else if (j == i + 1) return Math.max(nums[i], nums[j]);
        else {
            C[i - 1] = 0;
            C[i] = nums[i];
            for(int k = i + 1; k <= j; k ++) {
                C[k] = Math.max(C[k - 1], C[k - 2] + nums[k]);
            }
            return C[j];
        }
    }
}
