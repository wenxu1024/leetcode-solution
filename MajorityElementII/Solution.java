public class Solution {
    public List<Integer> majorityElement(int[] nums) {
        //moore's majority voting algorithm
        List<Integer> res = new ArrayList<Integer> ();
        int candidate1, candidate2, count1, count2;
        candidate1 = -1; candidate2 = -1; count1 = 0; count2 = 0;
        for(int i = 0; i < nums.length; i ++) {
            if (nums[i] == candidate1) count1 ++;
            else if (nums[i] == candidate2) count2 ++;
            else if (count1 == 0) {candidate1 = nums[i]; count1 = 1; }
            else if (count2 == 0) {candidate2 = nums[i]; count2 = 1; }
            else {count1 --; count2 --; }
        }
        count1 = 0;
        count2 = 0;
        for(int i = 0; i < nums.length; i ++) {
            if (nums[i] == candidate1) count1 ++;
            else if (nums[i] == candidate2) count2 ++;
            else;
        }
        if (count1 > nums.length / 3) res.add(candidate1);
        if (count2 > nums.length / 3) res.add(candidate2);
        return res;
    }
}
