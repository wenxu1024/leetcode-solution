import java.util.*;
import java.lang.*;
import java.lang.Integer;
//Solution.java for subarray sum closest to 0

public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number 
     *          and the index of the last number
     */
    public ArrayList<Integer> subarraySumClosest(int[] nums) {
        // write your code here
        int l = nums.length;
        if (l == 1) {
            ArrayList<Integer> res = new ArrayList<Integer> ();
            res.add(new Integer(0));
            res.add(new Integer(0));
            return res;
        }
        Pair<Integer, Integer> [] sum = new Pair[l];
        int k = 0, min, i, c = 0;
        for (i = 0; i < l; i ++) {
            c += nums[i];
            sum[i] = new Pair(new Integer(c), new Integer(i));
        }
        Arrays.sort(sum, new PairComparator());
//      System.out.println(Arrays.toString(sum));
//      return null;
        min = 9999;
        for (i = 0; i < l - 1; i ++) {
           int diff = sum[i].x.intValue() - sum[i + 1].x.intValue();
           if (Math.abs(diff) < min) {
                min = Math.abs(diff);
                k = i;
           }
        }
        Integer lo = sum[k].y;
        Integer hi = sum[k + 1].y;
        if (lo.intValue() > hi.intValue()) {Integer temp = lo; lo = hi; hi = temp;}
        ArrayList<Integer> res = new ArrayList<Integer> ();
        res.add(new Integer(lo.intValue() + 1));
        res.add(hi);
        return res;
    }

    public static void main(String[] args) {
	int[] nums = {-3, 1, 1, -3, 5};
	Solution sol = new Solution();
	System.out.println("the answer for " + Arrays.toString(nums) + " is: " + sol.subarraySumClosest(nums));
    }

};

class Pair<X, Y> {
    public final  X x;
    public final Y y;
    public Pair(X x, Y y) {
        this.x = x;
        this.y = y;
    }

    public String toString() {
        String s = "x: " + x + " y: " + y;
        return s;
    }
};

class PairComparator implements Comparator<Pair> {
    @Override
    public int compare(Pair a, Pair b) {
        Integer ia = (Integer) a.x;
        Integer ib = (Integer) b.x;
        return ia.compareTo(ib);
    }
};



