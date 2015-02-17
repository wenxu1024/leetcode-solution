// Median II
import java.util.*;
public class Solution {
    /**
     * @param nums: A list of integers.
     * @return: the median of numbers
     */
    public int[] medianII(int[] nums) {
        // write your code here
        PriorityQueue<Integer> pmin = new PriorityQueue<Integer> ();
        PriorityQueue<Integer> pmax = new PriorityQueue<Integer> (10, new MaxComparator<Integer>());
        int i, l = nums.length;
        int[] median = new int[l];
        for(i = 0; i < l; i ++) {
            if (pmin.size() == 0 && pmax.size() == 0) {
                pmax.add(new Integer(nums[i]));
            }
            else {
                if (nums[i] > pmax.peek().intValue()) pmin.add(new Integer(nums[i]));
                else pmax.add(new Integer(nums[i]));
                if (pmax.size() < pmin.size()) {
                    Integer temp = pmin.poll();
                    pmax.add(temp);
                }
                else if (pmax.size() > pmin.size() + 1) {
                    Integer temp = pmax.poll();
                    pmin.add(temp);
                }
                else ;
            }
            median[i] = pmax.peek();
        }
        return median;
    }

    public static void main(String[] args) {
	int[] nums = {1, 2, 3, 4, 5};
	int l = nums.length;
	Solution sol = new Solution();
	System.out.println("The answer for " + Arrays.toString(nums) + " is: " + Arrays.toString(sol.medianII(nums)));
    }
    
};

class MaxComparator<Object> implements Comparator<Object> {
    @Override
    public int compare(Object o1, Object o2) {
	Integer i1 = (Integer) o1;
	Integer i2 = (Integer) o2;
	return -i1.compareTo(i2);
    }
}


