import java.util.*;

//Maximum Subarray Solution

public class Solution {
    /**
     * @param nums: A list of integers
     * @param k: An integer denote to find k non-overlapping subarrays
     * @return: An integer denote the sum of max k non-overlapping subarrays
     */
    public int maxSubArray(ArrayList<Integer> nums, int k) {
        // write your code
        ArrayList<Integer> sum = new ArrayList<Integer> ();
        int i, j, s, t, diff, min, c = 0, l = nums.size();
        sum.add(new Integer(0));
        for (i = 0; i < l; i ++) {
            c += nums.get(i).intValue();
            sum.add(new Integer(c));
        } // build sum ArrayList
        
	System.out.println(sum);
        int[][][] max = new int[l + 1][l + 1][k + 1];
        for (i = 0; i < l; i++) {
            for(j = i + 1;j < l + 1; j++) {
                max[i][j][1] = sum.get(i + 1).intValue() - sum.get(i).intValue();
                min = sum.get(i).intValue();
                for(t = i + 1; t <= j; t++) {
                    if (sum.get(t).intValue() < min) min = sum.get(t).intValue();
                    else {
                        diff = sum.get(t).intValue() - min;
                        max[i][j][1] = Math.max(max[i][j][1], diff);
                    }
                }
            }
        }
	System.out.println(max[0][l][1]);
        
        for (t = 2; t < k + 1; t++ ) {
            for (i = 0; i < l + 1 - t; i++) {
                for (j = i + t; j < l + 1; j++) {
                    if (t == j - i) max[i][j][t] = sum.get(j).intValue() - sum.get(i).intValue();
                    else {
                        max[i][j][t] = -9999;
                        for(s = i + t ; s < j; s ++) {
                            max[i][j][t] = Math.max(max[i][j][t], max[i][s][t - 1] + max[s][j][1]);
                        }
                    }
                }
            }
        }
        return max[0][l][k];
    }

    public static void main(String[] args) {
	ArrayList<Integer> nums = new ArrayList<Integer> ();
	nums.add(new Integer(-1));
	nums.add(new Integer(-2));
	nums.add(new Integer(-3));
	nums.add(new Integer(-100));
	nums.add(new Integer(-1));
	nums.add(new Integer(-50));
	int k = 2;
	Solution sol = new Solution();
	System.out.println(sol.maxSubArray(nums, k));
    }
};



