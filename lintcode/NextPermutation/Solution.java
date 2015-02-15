import java.util.*;
//Next Permutation

public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A list of integers that's next permuation
     */
    public ArrayList<Integer> nextPermuation(ArrayList<Integer> nums) {
		// write your code
		int n = nums.size();
		int i, k , l;
		k = 0;
		l = 0;
		for(i = n - 2; i > -1; i --) {
		    if (nums.get(i).intValue() < nums.get(i + 1).intValue()) {
		        k = i;
		        break;
		    } //get the largest k satisfying nums[k] < nums[k + 1]
		}
		if (i == - 1) reverseArrayList(nums, 0, n - 1);
		else {
		    for(i = n - 1; i > -1; i --) {
		        if(nums.get(i).intValue() > nums.get(k).intValue()) {
		            l = i;
		            break; //get the largest l satisfying nums[l] > nums[k]
		        }
		    }
		    swap(nums, k, l);
		    reverseArrayList(nums, k + 1, n - 1);
		}
		return nums;
    }
    
    public static void swap(ArrayList<Integer> nums, int i, int j) {
        Integer temp;
        temp = nums.get(i);
        nums.set(i, nums.get(j));
        nums.set(j, temp);
    }
    
    public void reverseArrayList(ArrayList<Integer> nums, int i, int j) {
        int s, t;
        s = i;
        t = j;
        while (s < t) {
            swap(nums, s, t);
            s ++;
            t --;
        }
    }
}



