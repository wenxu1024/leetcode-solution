import java.util.*;

public class Solution {
    public int findKthLargest(int[] nums, int k) {
        int l = nums.length;
        int rank = l - k + 1;
        return findRankHelper(nums, 0, l - 1, rank);
    }
    
    
    public int partition(int[] nums, int i, int j) {
        //randomly select a pivot point between i.. j and partition the whole array
        Random rnd = new Random();
        int index = rnd.nextInt(j - i + 1) + i;
//	System.out.println(index);
        //swap index and ith element
        int tmp;
        tmp = nums[index];
        nums[index] = nums[i];
        nums[i] = tmp;
        int s, t;
        s = i + 1;
        t = i + 1;
        while(t < j + 1) {
            if(nums[t] > nums[i]) t ++;
            else {
                tmp = nums[s];
                nums[s] = nums[t];
                nums[t] = tmp;
                s ++;
                t ++;
            }
        }
        tmp = nums[s - 1];
        nums[s - 1] = nums[i];
        nums[i] = tmp;
        return s - 1;
    }
    
    public int findRankHelper(int[] nums, int i, int j, int k) {
        int p = partition(nums, i, j);
        if (p - i + 1 == k) return nums[p];
        else if (p - i + 1 > k) return findRankHelper(nums, i, p - 1, k);
        else return findRankHelper(nums, p + 1, j, k - p + i - 1);
    }

    public static void main(String[] args) {
	int[] nums = {3,2,1,5,6,4};
	int k = 2;
	System.out.println(Arrays.toString(nums));
	Solution sol = new Solution();
	System.out.println(sol.partition(nums, 0, nums.length - 1));
	System.out.println(Arrays.toString(nums));
	System.out.println(sol.findKthLargest(nums, k));
    }
}
