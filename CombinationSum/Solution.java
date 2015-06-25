//combination sum3

import java.util.*;

public class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        return combinationSum3Helper(k, n, 1);
    }
    
    public List<List<Integer> > combinationSum3Helper(int k, int n, int m) {
        // only integers between m and 9 (inclusive) are allowed
        if (k == 0 && n == 0) {
            List<List<Integer> > res = new ArrayList<List<Integer> >();
            List<Integer> empty = new ArrayList<Integer> ();
            res.add(empty);
            return res;
        }
        else if (k == 0 && n != 0 || k > 9 - m + 1) {
            List<List<Integer> > res = new ArrayList<List<Integer> > ();
            return res;
        }
        else {
            List<List<Integer> > tmp;
            List<List<Integer> > res = new ArrayList<List<Integer> > ();
            tmp = combinationSum3Helper(k - 1, n - m, m + 1);
            for(int i = 0; i < tmp.size(); i ++) {
                tmp.get(i).add(0, m);
                res.add(tmp.get(i));
            }
            tmp = combinationSum3Helper(k, n, m + 1);
            for(int i = 0; i < tmp.size(); i ++) {
                res.add(tmp.get(i));
            }
            return res;
        }
        
    }


    public static void main(String[] args) {
	int k = 3;
	int n = 9;
	Solution sol = new Solution();
	System.out.println(sol.combinationSum3(k, n));
    }
}
