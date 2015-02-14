import java.util.*;
class Solution {
    /**
     * @param nums: The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
    public int binarySearch(int[] nums, int target) {
        //write your code here
        int l;
        l = nums.length;
        return binarySearchHelper(nums, target, 0, l - 1);
    }
    
    public int binarySearchHelper(int[] nums, int target, int i, int j){
        int k = (i + j) / 2;
        if (i == j + 1) return -1;
        if (i == j && target == nums[k]) return k;
        if (target > nums[k]) {
            return binarySearchHelper(nums, target, k + 1, j);
        }
        else if (target < nums[k]) {
            return binarySearchHelper(nums, target, i, k - 1);
        }
        else {
            return binarySearchHelper(nums, target, i, k);
        }
    }
  
    public static void main(String[] args) {
	int[] nums = {1, 2, 3, 3, 4, 5, 10};
        int target = 3;
        Solution sol = new Solution();
        System.out.println("the anser for " + Arrays.toString(nums) + " is: " + sol.binarySearch(nums, target));
    }
}


