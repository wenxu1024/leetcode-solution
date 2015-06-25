import java.util.*;

public class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        int n = nums.length;
        Pair[] plist = new Pair[n];
        for(int i = 0; i < n; i ++) {
            Pair p = new Pair(nums[i], i);
            plist[i] = p;
        }
        Arrays.sort(plist);
        for(int i = 0; i < n - 1; i ++) {
            for(int j = i + 1; j < n; j ++) {
                if (plist[j].num <=plist[i].num + t && Math.abs(plist[j].index - plist[i].index) <= k) {
                    return true;
                }
                else if (plist[j].num - plist[i].num > t) break;
                else continue;
            }
        }
        return false;
    }


    public static void main(String[] args) {
	int[] nums = {-1, 2147483647};
	int k = 1;
	int t = 2147483647;
	Solution sol = new Solution();
	System.out.println(sol.containsNearbyAlmostDuplicate(nums, k, t));
    }
}

class Pair implements Comparable<Pair> {
    public int num;
    public int index;
    
    public Pair(int num, int index) {
        this.num = num;
        this.index = index;
    }
    
    @Override
    public int compareTo(Pair p) {
        return Integer.compare(this.num, p.num);
    }

}
